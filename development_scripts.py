#!/usr/bin/env python
import os
import re
import glob
import numbers
import argparse

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as DQ
from textfsm import clitable
from lib.ntc_templates.parse import parse_output


FILE_PATH = os.path.abspath(__file__)
FILE_DIR = os.path.dirname(FILE_PATH)
TEST_DIR = "{0}/tests".format(FILE_DIR)
YAML_OBJECT = YAML()
YAML_OBJECT.explicit_start = True
YAML_OBJECT.indent(sequence=4, offset=2)
YAML_OBJECT.block_style = True



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


def build_parsed_data_from_output(filepath):
    """
    Generates a YAML file from the file containing the command output.

    The command output should be stored in a file in the appropriate directory;
    for example, ``tests/cisco_ios/show_version/cisco_ios_show_version.raw``
    This uses ``lib.ntc_templates.parse.parse_output``, so the template must
    be in the ``templates/`` directory, and ``templates/index`` must be updated
    with the correct entry for the template.

    Args:
        filepath (str): The path to the file containing sample command output.

    Returns
        None: File I/O is performed to generate a YAML file pased on command output.

    Example:
        >>> filepath = "tests/cisco_ios/show_version/cisco_ios_show_version.raw"
        >>> build_parsed_data_from_output(filepath)
        >>> 
    """
    platform, command, filename = parse_test_filepath(filepath)
    with open(filepath, encoding="utf-8") as output_file:
        output_data = output_file.read()

    structured_data = parse_output(platform, command, output_data)

    command_with_underscores = command.replace(" ", "_")
    yaml_file = "{0}/{1}/{2}/{3}.yml".format(
        TEST_DIR, platform, command_with_underscores, filename
    )
    ensure_yaml_standards({"parsed_sample": structured_data}, yaml_file)



def build_parsed_data_from_dir(dirpath):
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
        build_parsed_data_from_output(file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ensures YAML files match project standards")
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
        help="The path to the file containing command output."
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
