#!/usr/bin/env python
import os
import re
import glob
import numbers
import argparse

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as DQ
from ntc_templates.parse import parse_output


FILE_PATH = os.path.abspath(__file__)
FILE_DIR = os.path.dirname(FILE_PATH)
TEST_DIR = "{0}/tests".format(FILE_DIR)
YAML_OBJECT = YAML()
YAML_OBJECT.explicit_start = True
YAML_OBJECT.indent(sequence=4, offset=2)
YAML_OBJECT.block_style = True
RE_MULTILINE_REMARK = re.compile(r"(.*\n\s*#)(.*)")


def ensure_spacing_for_multiline_comment(remark):
    """
    Finds all comments and ensures a single space after "#" symbol.

    Args:
        remark (str): The remark of a comment from a ``ruamel.yaml.token.CommentToken``.

    Returns:
        str: The ``remark`` formatted with a single space after comment start, "#"

    Example:
        >>> remark = "comment 11\n#        comment 12\n#comment 13\n"
        >>> remark_formatted = ensure_spacing_for_multiline_comment(remark)
        >>> # Formatting has normalized each comment to have a single space after the "#"
        >>> remark_formatted
        'comment 11\n# comment 12\n# comment 13'
        >>>
    """
    remarks = re.findall(RE_MULTILINE_REMARK, remark)
    # remarks that don't have a subsequent comment are not captured by regex
    if not remarks:
        remarks = (("", remark),)
    # Example remarks: [('comment \n#', '      comment2 '), ('\n  #', 'comment3 # 9')]
    remark_formatted = "".join([entry[0] + " " + entry[1].strip() for entry in remarks])
    return remark_formatted


def ensure_space_after_octothorpe(comment):
    """
    Ensures a single space is between the "#" and first letter of a comment.

    Args:
        comment (ruamel.yaml.token.CommentToken): The comment to update.

    Returns:
        None: The comment is updated in place.

    Example:
        >>> yml = ruamel.yaml.YAML()
        >>> with open("test.yml", encoding="utf-8") as fh:
        ...     print(fh.read())
        ...     fh.seek(0)
        ...     data = yml.load(fh)
        ...
        ---
        a: 5 # comment 1
        b: 6 #comment 2
        #comment 3
        c:
          - 7 #comment 4
        #comment 5
          - 8
        #comment 6
        d:
          #comment 7
          e: a #comment 8
          f:
            - 9
            #comment 9
            - 10
            - a:
                a: 8
                #comment 10
                b: 1
            - b: 1
            - 9
        #comment 11
        #        comment 12
        #comment 13

        >>> type(data)
        <class 'ruamel.yaml.comments.CommentedMap'>
        >>> comment = data.ca.items["b"][2]
        >>> comment
        CommentToken('#comment 2\n#comment 3\n', line: 2, col: 5)
        >>> ensure_space_after_octothorpe(comment)
        >>> # Both comments within the CommentToken object
        >>> # now have a space between the "#" and the first symbol
        >>> comment
        CommentToken('# comment 2\n# comment 3\n', line: 2, col: 5)
        >>>
    """
    if comment is not None:
        # Comments can start with whitespace,
        # so partition is used to preserve that in the final result
        space, octothorpe, remark = comment.value.partition("#")
        remark_formatted = ensure_spacing_for_multiline_comment(remark)
        comment.value = f"{space}# {remark_formatted.lstrip()}\n"


def ensure_space_comments(comments):
    """
    Ensures there is a space after the "#" in comments.

    Args:
        comments (iter): The comments from ruamel.yaml.YAML() object.

    Returns:
         None: Comments are update in place.

    Example:
        >>> yml = ruamel.yaml.YAML()
        >>> with open("test.yml", encoding="utf-8") as fh:
        ...     print(fh.read())
        ...     fh.seek(0)
        ...     data = yml.load(fh)
        ...
        ---
        a: 5 # comment 1
        b: 6 #comment 2
        #comment 3
        c:
          - 7 #comment 4
        #comment 5
          - 8
        #comment 6
        d:
          #comment 7
          e: a #comment 8
          f:
            - 9
            #comment 9
            - 10
            - a:
                a: 8
                #comment 10
                b: 1
            - b: 1
            - 9
        #comment 11
        #        comment 12
        #comment 13

        >>> type(data)
        <class 'ruamel.yaml.comments.CommentedMap'>
        >>> comments = data.ca.items.values()
        >>> comments
        dict_values([
            [None, None, CommentToken('# comment 1\n', line: 1, col: 5), None],
            [None, None, CommentToken('#comment 2\n#comment 3\n', line: 2, col: 5), None],
            [None, None, None, [CommentToken('#comment 7\n', line: 10, col: 2)]]
        ])
        >>> ensure_space_comments(comments)
        >>> # Every comment now has a space between the "#" and the first symbol
        >>> comments
        dict_values([
            [None, None, CommentToken('# comment 1\n', line: 1, col: 5), None],
            [None, None, CommentToken('# comment 2\n# comment 3\n', line: 2, col: 5), None],
            [None, None, None, [CommentToken('# comment 7\n', line: 10, col: 2)]]
        ])
        >>>
    """
    comment_objects = (comment for comment_list in comments for comment in comment_list)
    for comment in comment_objects:
        # Some comments are nested inside an additional list
        if not isinstance(comment, list):
            ensure_space_after_octothorpe(comment)
        else:
            for cmt in comment:
                ensure_space_after_octothorpe(cmt)


def update_yaml_comments(yaml_object):
    """
    Ensures comments have a space after the "#" on itself and its entries

    Args:
        yaml_object (ruamel.yaml.comments.CommentedMap | ruamel.yaml.comments.CommentedSeq): The list or dict object.

    Returns:
        None: Comments are updated in place.

    Example:
        >>> yml = ruamel.yaml.YAML()
        >>> with open("test.yml", encoding="utf-8") as fh:
        ...     print(fh.read())
        ...     fh.seek(0)
        ...     data = yml.load(fh)
        ...
        ---
        a: 5 # comment 1
        b: 6 #comment 2
        #comment 3
        c:
          - 7 #comment 4
        #comment 5
          - 8
        #comment 6
        d:
          #comment 7
          e: a #comment 8
          f:
            - 9
            #comment 9
            - 10
            - a:
                a: 8
                #comment 10
                b: 1
            - b: 1
            - 9
        #comment 11
        #        comment 12
        #comment 13

        >>> type(data)
        <class 'ruamel.yaml.comments.CommentedMap'>
        >>> update_yaml_comments(data)
        >>> with open("test.yml", "w", encoding="utf-8") as fh
        ...     yml.dump(data, fh)
        ...
        >>>
        # Notice that comments now have a space between the hash and first symbol.
        >>> with open("test.yml", encoding="utf-8") as fh:
        ...     print(fh.read())
        ...
        a: 5 # comment 1
        b: 6 # comment 2
        #comment 3
        c:
        - 7   # comment 4
        #comment 5
        - 8
        # comment 6
        d:
          # comment 7
          e: a # comment 8
          f:
          - 9
            # comment 9
          - 10
          - a:
              a: 8
                # comment 10
              b: 1
          - b: 1
          - 9
        # comment 11
        # comment 12
        # comment 13

        >>>
    """
    comments = yaml_object.ca.items.values()
    ensure_space_comments(comments)
    try:
        yaml_object_values = yaml_object.values()
    except AttributeError:
        yaml_object_values = yaml_object

    for entry in yaml_object_values:
        if isinstance(entry, dict) or isinstance(entry, list):
            update_yaml_comments(entry)


def transform_file(filepath):
    """
    Loads YAML file and formats to adhere to yamllint config.

    Args:
        filepath (str): The full path to a YAML file.

    Returns:
        None: File I/O is performed to ensure YAML file adheres to yamllint config.

    Example:
        >>> filepath = "tests/cisco_ios/show_version/cisco_ios_show_version.yml"
        >>> transform_parsed(filepath)
        >>>
    """
    with open(filepath, encoding="utf-8") as parsed_file:
        parsed_object = YAML_OBJECT.load(parsed_file)

    ensure_yaml_standards(parsed_object, filepath)


def transform_glob(dirpath):
    """
    Globs for YAML files and formats to adhere to yamllint config.

    Every file in ``dirpath`` ending in ``.yml`` will be formatted according to
    yamllint config. Since this is using glob, the directory string passed in can
    also include glob syntax (see ``Example``)

    Args:
        dirpath (str): The path to search for files with ``.yml`` extension.

    Returns:
        None: File I/O is performed to ensure YAML files adhere to yamllint config.

    Example:
        >>> dirpath = "tests/*/*"
        >>> transform_parsed(dirpath)
        # Each filename is printed to the terminal
        >>>
    """
    # This commented out code was used for mass renaming of files;
    # it is probably not needed anymore
    # for file in glob.iglob("{0}/*.parsed".format(dirpath)):
    #     os.rename(file, file.replace(file[-6:], "yml"))
    for file in glob.iglob("{0}/*.yml".format(dirpath)):
        print(file)
        transform_file(file)


def ensure_yaml_standards(parsed_object, output_path):
    """
    Ensures YAML files adhere to yamllint config as defined in this project.

    Args:
        parsed_object (dict): The TextFSM/CliTable data converted to a list of dicts.
            The list of dicts must be the value of a dictionary key, ``parsed_sample``.
        output_path (str): The filepath to write the ``parsed_object`` to.

    Returns:
        None: File I/O is performed to write ``parsed_object`` to ``output_path``.
    """
    for entry in parsed_object["parsed_sample"]:
        # TextFSM conversion will allways be a list of dicts
        for key, value in entry.items():
            # TextFSM capture groups always return strings or lists
            # This also accounts for numbers incase the YAML was done by hand
            if isinstance(value, (str, numbers.Number)):
                entry[key] = DQ(value)
            else:
                entry[key] = [DQ(val) for val in value]
    try:
        update_yaml_comments(parsed_object)
    except AttributeError:
        pass

    with open(output_path, "w", encoding="utf-8") as parsed_file:
        YAML_OBJECT.dump(parsed_object, parsed_file)


def parse_test_filepath(filepath):
    """
    Parses fullpath of test file to obtain platform, command, and filename info.

    Args:
        filepath (str): The path to a test file from platform directory or earlier.

    Returns:
        tuple: Strings of platform, command, and the filename without the extension.

    Example:
        >>> filepath = "tests/cisco_ios/show_version/cisco_ios_show_version.raw"
        >>> platform, command, filename = parse_test_filepath(filepath)
        >>> print(platform)
        cisco_ios
        >>> print(command)
        show version
        >>> print(filename)
        cisco_ios_show_version
        >>>
    """
    command_dir, filename = os.path.split(filepath)
    platform_dir, command = os.path.split(command_dir)
    test_dir, platform = os.path.split(platform_dir)

    command_without_underscores = command.replace("_", " ")
    filename_without_extension, extension = filename.rsplit(".", 1)

    return platform, command_without_underscores, filename_without_extension


def build_parsed_data_from_output(filepath, test_dir=TEST_DIR):
    """
    Generates a YAML file from the file containing the command output.

    The command output should be stored in a file in the appropriate directory;
    for example, ``tests/cisco_ios/show_version/cisco_ios_show_version.raw``
    This uses ``lib.ntc_templates.parse.parse_output``, so the template must
    be in the ``templates/`` directory, and ``templates/index`` must be updated
    with the correct entry for the template.

    Args:
        filepath (str): The path to the file containing sample command output.
        test_dir (str): The root directory to story the resulting YAML file.

    Returns
        None: File I/O is performed to generate a YAML file pased on command output.

    Example:
        >>> root_dir = "tests/cisco_ios/show_version"
        >>> os.listdir(root_dir)
        ['cisco_ios_show_version.raw']
        >>> filepath = "tests/cisco_ios/show_version/cisco_ios_show_version.raw"
        >>> build_parsed_data_from_output(filepath)
        >>> os.listdir(root_dir)
        ['cisco_ios_show_version.raw', 'cisco_ios_show_version.yml']
        >>>
    """
    platform, command, filename = parse_test_filepath(filepath)
    with open(filepath, encoding="utf-8") as output_file:
        output_data = output_file.read()

    structured_data = parse_output(platform, command, output_data)

    command_with_underscores = command.replace(" ", "_")
    yaml_file = "{0}/{1}/{2}/{3}.yml".format(
        test_dir, platform, command_with_underscores, filename
    )
    ensure_yaml_standards({"parsed_sample": structured_data}, yaml_file)


def build_parsed_data_from_dir(dirpath, test_dir=TEST_DIR):
    """
    Globs for files ending in ``.raw`` and generates YAML files based on TextFSM ouptut.

    Every file in ``dirpath`` ending in ``.raw`` will be parsed with TextFSM and written
    to a YAML file following the yamllint config standards. Since this is using glob, the
    directory string passed in can also include glob syntax.

    Args:
        dirpath (str): The path to search for files with ``.raw`` extension.

    Returns:
        None: File I/O is performed to ensure YAML files exist for each test output file.

    Example:
        >>> dirpath = "tests/cisco_ios/show_mac-address-table"
        >>> build_parsed_data_from_dir(dirpath)
        # Each filename is printed to the terminal
        >>>
    """
    for file in glob.iglob("{0}/*.raw".format(dirpath)):
        print(file)
        build_parsed_data_from_output(file, test_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ensures YAML files match project standards"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-y", "--yaml_file", type=str, help="The path to a YAML file.")
    group.add_argument(
        "-yd",
        "--yaml_dir",
        type=str,
        help='The directory path to look for all files ending in ".yml"',
    )
    group.add_argument(
        "-c",
        "--command_file",
        type=str,
        help="The path to the file containing command output.",
    )
    group.add_argument(
        "-cd",
        "--command_dir",
        type=str,
        help='The directory path to look for all files ending in ".raw"',
    )

    args = parser.parse_args()
    yaml_file = args.yaml_file
    yaml_dir = args.yaml_dir
    command_file = args.command_file
    command_dir = args.command_dir

    if yaml_file is not None:
        transform_file(yaml_file)
    elif yaml_dir is not None:
        transform_glob(yaml_dir)
    elif command_file is not None:
        build_parsed_data_from_output(command_file)
    else:
        build_parsed_data_from_dir(command_dir)
