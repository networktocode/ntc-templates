"""Tests that original from the developer test suite."""
import os
import glob
import numbers
import re
from copy import deepcopy

import pytest

from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as DQ

from ntc_templates.parse import parse_output

FILE_PATH = os.path.abspath(__file__)
FILE_DIR = os.path.dirname(FILE_PATH)
TEST_DIR = f"{FILE_DIR}/tests"
YAML_OBJECT = YAML()
YAML_OBJECT.explicit_start = True
YAML_OBJECT.indent(sequence=4, offset=2)
YAML_OBJECT.block_style = True
RE_MULTILINE_REMARK = re.compile(r"(.*\n\s*#)(.*)")


def ensure_spacing_for_multiline_comment(remark):
    r"""
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
    r"""
    Ensures a single space is between the "#" and first letter of a comment.

    Args:
        comment (ruamel.yaml.token.CommentToken): The comment to update.

    Returns:
        None: The comment is updated in place.

    Example:
        >>> from ruamel.yaml import YAML
        >>> yml = YAML()
        >>> with open("test.yml", encoding="utf-8") as fh:  # doctest: +SKIP
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

        >>> type(data)  # doctest: +SKIP
        <class 'ruamel.yaml.comments.CommentedMap'>
        >>> comment = data.ca.items["b"][2]  # doctest: +SKIP
        >>> comment  # doctest: +SKIP
        CommentToken('#comment 2\n#comment 3\n', line: 2, col: 5)
        >>> ensure_space_after_octothorpe(comment)  # doctest: +SKIP
        >>> # Both comments within the CommentToken object
        >>> # now have a space between the "#" and the first symbol
        >>> comment  # doctest: +SKIP
        CommentToken('# comment 2\n# comment 3\n', line: 2, col: 5)
        >>>
    """
    if comment is not None:
        # Comments can start with whitespace,
        # so partition is used to preserve that in the final result
        space, _, remark = comment.value.partition("#")
        remark_formatted = ensure_spacing_for_multiline_comment(remark)
        comment.value = f"{space}# {remark_formatted.lstrip()}\n"


def ensure_space_comments(comments):
    r"""
    Ensures there is a space after the "#" in comments.

    Args:
        comments (iter): The comments from ruamel.yaml.YAML() object.

    Returns:
         None: Comments are update in place.

    Example:
        >>> from ruamel.yaml import YAML
        >>> yml = YAML()
        >>> with open("test.yml", encoding="utf-8") as fh: # doctest: +SKIP
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

        >>> type(data) # doctest: +SKIP
        <class 'ruamel.yaml.comments.CommentedMap'>
        >>> comments = data.ca.items.values() # doctest: +SKIP
        >>> comments # doctest: +SKIP
        dict_values([
            [None, None, CommentToken('# comment 1\n', line: 1, col: 5), None],
            [None, None, CommentToken('#comment 2\n#comment 3\n', line: 2, col: 5), None],
            [None, None, None, [CommentToken('#comment 7\n', line: 10, col: 2)]]
        ])
        >>> ensure_space_comments(comments) # doctest: +SKIP
        >>> # Every comment now has a space between the "#" and the first symbol
        >>> comments # doctest: +SKIP
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
    Ensures comments have a space after the "#" on itself and its entries.

    Args:
        yaml_object (ruamel.yaml.comments.CommentedMap | ruamel.yaml.comments.CommentedSeq): The list or dict object.

    Returns:
        None: Comments are updated in place.

    Example:
        >>> from ruamel.yaml import YAML
        >>> yml = YAML()
        >>> with open("test.yml", encoding="utf-8") as fh: # doctest: +SKIP
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

        >>> type(data) # doctest: +SKIP
        <class 'ruamel.yaml.comments.CommentedMap'>
        >>> update_yaml_comments(data) # doctest: +SKIP
        >>> with open("test.yml", "w", encoding="utf-8") as fh: # doctest: +SKIP
        ...     yml.dump(data, fh)
        ...
        >>>
        # Notice that comments now have a space between the hash and first symbol.
        >>> with open("test.yml", encoding="utf-8") as fh: # doctest: +SKIP
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
        if isinstance(entry, (dict, list)):
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
        >>> transform_file(filepath)
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
        >>> transform_file(dirpath) # doctest: +SKIP
        # Each filename is printed to the terminal
        >>>
    """
    # This commented out code was used for mass renaming of files;
    # it is probably not needed anymore
    # for file in glob.iglob("{0}/*.parsed".format(dirpath)):
    #     os.rename(file, file.replace(file[-6:], "yml"))
    for file in glob.iglob(f"{dirpath}/*.yml"):
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
    _, platform = os.path.split(platform_dir)

    command_without_underscores = command.replace("_", " ")
    filename_without_extension, _ = filename.rsplit(".", 1)

    return platform, command_without_underscores, filename_without_extension


def build_parsed_data_from_output(filepath, test_dir=TEST_DIR):
    """
    Generates a YAML file from the file containing the raw command output.

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
        >>> root_dir = "tests/cisco_ios/dir"
        >>> os.listdir(root_dir) # doctest: +SKIP
        ['cisco_ios_dir.raw']
        >>> filepath = "tests/cisco_ios/dir/cisco_ios_dir.raw"
        >>> build_parsed_data_from_output(filepath) # doctest: +SKIP
        >>> os.listdir(root_dir) # doctest: +SKIP
        ['cisco_ios_dir.raw', 'cisco_ios_dir.yml']
        >>>
    """
    platform, command, filename = parse_test_filepath(filepath)
    with open(filepath, encoding="utf-8") as output_file:
        output_data = output_file.read()

    structured_data = parse_output(platform, command, output_data)

    command_with_underscores = command.replace(" ", "_")
    yaml_file = f"{test_dir}/{platform}/{command_with_underscores}/{filename}.yml"
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
        >>> build_parsed_data_from_dir(dirpath) # doctest: +SKIP
        # Each filename is printed to the terminal
        >>>
    """
    for file in glob.iglob(f"{dirpath}/*.raw"):
        print(file)
        build_parsed_data_from_output(file, test_dir)


@pytest.fixture(scope="module")
def yaml_comments_file():
    """Yaml comments tests."""
    with open("tests/mocks/load/yaml_comments.yml", encoding="utf-8") as file_handler:
        return YAML_OBJECT.load(file_handler)


@pytest.fixture
def copy_yaml_comments(yaml_comments_file):
    """Helper to copy yaml comments."""
    return deepcopy(yaml_comments_file)


@pytest.fixture
def teardown_normalize_file():
    """Test fixture to normalize a file."""
    filepaths = {}

    def _teardown_normalize_file(filepath):
        with open(filepath, encoding="utf-8") as file_handler:
            contents = file_handler.read()

        filepaths[filepath] = contents

    yield _teardown_normalize_file

    for filepath, contents in filepaths.items():
        with open(filepath, "w", encoding="utf-8") as file_handler:
            file_handler.write(contents)


@pytest.fixture(scope="module")
def expected_file():
    """Test fixture to find the expected yaml file."""
    expected_path = "tests/mocks/expected/parsed_sample.yml"
    with open(expected_path, encoding="utf-8") as file_handler:
        return file_handler.read()


@pytest.fixture(scope="module")
def expected_mac_file():
    """Test fixture to find the expected mac yaml file."""
    expected_path = "tests/mocks/expected/show_mac.yml"
    with open(expected_path, encoding="utf-8") as file_handler:
        return file_handler.read()


@pytest.fixture
def teardown_delete_file():
    """Test fixture to delete a file."""
    filepaths = []

    def _teardown_delete_file(filepath):
        filepaths.append(filepath)

    yield _teardown_delete_file

    for file in filepaths:
        os.remove(file)


def test_ensure_spacing_for_multiline_comment():
    remark = "comment 11\n#        comment 12\n#comment 13\n"
    remark_formatted = ensure_spacing_for_multiline_comment(remark)
    assert remark_formatted == "comment 11\n# comment 12\n# comment 13"


def test_ensure_space_after_octothorpe(copy_yaml_comments):
    comment = copy_yaml_comments.ca.items["b"][2]
    ensure_space_after_octothorpe(comment)
    assert comment.value == "# comment 2\n# comment 3\n"


def test_ensure_space_comments(copy_yaml_comments):
    comments = copy_yaml_comments.ca.items
    comment_values = comments.values()
    ensure_space_comments(comment_values)
    assert comments["a"][2].value == "# comment 1\n"
    assert comments["b"][2].value == "# comment 2\n# comment 3\n"
    assert comments["d"][3][0].value == "# comment 7\n"


def test_update_yaml_comments(copy_yaml_comments):
    update_yaml_comments(copy_yaml_comments)
    string_yaml = StringIO()
    YAML_OBJECT.dump(copy_yaml_comments, string_yaml)
    actual = string_yaml.getvalue()
    with open("tests/mocks/expected/yaml_comments.yml", encoding="utf-8") as file_handler:
        expected = file_handler.read()
    assert actual == expected


def test_transform_file(teardown_normalize_file, expected_file):
    load_file = "tests/mocks/load/parsed_sample.yml"
    teardown_normalize_file(load_file)
    transform_file(load_file)
    with open(load_file, encoding="utf-8") as actual:
        assert actual.read() == expected_file


def test_transform_glob(teardown_normalize_file, expected_file):
    glob_dir = "tests/mocks/load/gl*"
    parsed_files = glob.glob(f"{glob_dir}/*.yml")
    for file in parsed_files:
        teardown_normalize_file(file)

    transform_glob(glob_dir)
    for file in parsed_files:
        with open(file, encoding="utf-8") as actual:
            assert actual.read() == expected_file


def test_ensure_yaml_standards(teardown_normalize_file, expected_file):
    load_file = "tests/mocks/load/parsed_sample.yml"
    teardown_normalize_file(load_file)
    with open(load_file, encoding="utf-8") as file_handler:
        load_yaml = YAML_OBJECT.load(file_handler)

    ensure_yaml_standards(load_yaml, load_file)
    with open(load_file, encoding="utf-8") as actual:
        assert actual.read() == expected_file


def test_parse_test_filepath():
    filepath = "tests/cisco_ios/show_version/cisco_ios_show_version.raw"
    platform, command, filename = parse_test_filepath(filepath)
    assert platform == "cisco_ios"
    assert command == "show version"
    assert filename == "cisco_ios_show_version"


def test_build_parsed_data_from_output(teardown_delete_file, expected_mac_file):
    load_file = "tests/mocks/cisco_ios/show_mac-address-table/show_mac1.raw"
    yaml_file = f"{load_file[:-3]}yml"
    teardown_delete_file(yaml_file)
    build_parsed_data_from_output(load_file, test_dir="tests/mocks")
    with open(yaml_file, encoding="utf-8") as actual:
        assert actual.read() == expected_mac_file


def test_build_parsed_data_from_dir(teardown_delete_file, expected_mac_file):
    glob_dir = "tests/mocks/cisco_ios/show_mac-*"
    command_files = glob.iglob(f"{glob_dir}/*.raw")
    parsed_files = [f"{file[:-3]}yml" for file in command_files]
    for file in parsed_files:
        teardown_delete_file(file)

    build_parsed_data_from_dir(glob_dir, test_dir="tests/mocks")
    for file in parsed_files:
        with open(file, encoding="utf-8") as actual:
            assert actual.read() == expected_mac_file
