#!/usr/bin/env python
import os
import re
import glob
import numbers
import argparse

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as DQ
from textfsm import clitable
from ntc_templates.parse import _clitable_to_dict


FILE_PATH = os.path.abspath(__file__)
FILE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = "{0}/templates".format(FILE_DIR)
TEST_DIR = "{0}/tests".format(FILE_DIR)


def transform_parsed(filepath=None, dirpath=None):
    if filepath is not None:
        ensure_yaml_standards(filepath)
    else:
        for file in glob.iglob("{0}/*.parsed".format(dirpath)):
            os.rename(file, file.replace(file[-6:], "yml"))
        for file in glob.iglob("{0}/*.yml".format(dirpath)):
            print(file)
            ensure_yaml_standards(file)


def ensure_yaml_standards(yaml_file, parsed_obj=None):
    yaml_obj = YAML()
    if parsed_obj is None:
        with open(yaml_file, encoding="utf-8") as parsed_file:
            parsed_data = parsed_file.read()
            parsed_obj = yaml_obj.load(parsed_data.replace("\n\n", "\n"))

    for entry in parsed_obj["parsed_sample"]:
        for key, value in entry.items():
            if isinstance(value, (str, numbers.Number)):
                entry[key] = DQ(value)
            else:
                entry[key] = [DQ(val) for val in value]

    yaml_obj.explicit_start = True
    yaml_obj.indent(sequence=4, offset=2)
    yaml_obj.block_style = True

    with open(yaml_file, "w") as parsed_file:
        yaml_obj.dump(parsed_obj, parsed_file)


def build_parsed_data_from_output(
    test_filename, command, platform,
):
    """
    TODO: Adjust parse_command function to accept templates directory
          instead of always using _get_template_dir
    """
    command_with_underscores = command.replace(" ", "_")
    test_dir = "{0}/{1}/{2}".format(TEST_DIR, platform, command_with_underscores)
    output_file = "{0}/{1}.raw".format(test_dir, test_filename)
    with open(output_file, encoding="utf-8") as fh:
        output_data = fh.read()

    cli_table = clitable.CliTable("index", TEMPLATE_DIR)
    attrs = {"Command": command, "Platform": platform}
    try:
        cli_table.ParseCmd(output_data, attrs)
        structured_data = _clitable_to_dict(cli_table)
    except clitable.CliTableError as e:
        raise Exception(
            'Unable to parse command "{0}" on platform {1} - {2}'.format(command, platform, str(e))
        )
    yml_file = "{0}/{1}.yml".format(test_dir, test_filename)
    ensure_yaml_standards(yml_file, {"parsed_sample": structured_data})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ensures YAML files match project standards")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--filepath", type=str, help="The path to a YAML file.")
    group.add_argument("-t", "--test_filename", type=str, help="The name of the test files.")
    group.add_argument(
        "-d",
        "--dirpath",
        type=str,
        help='The directory path to look for all files ending in ".parsed"',
    )
    parser.add_argument("-c", "--command", type=str, help="The command issued to get output.")
    parser.add_argument("-p", "--platform", type=str, help="The platform per the index file.")

    args = parser.parse_args()
    filepath = args.filepath
    dirpath = args.dirpath
    test_filename = args.test_filename
    command = args.command
    platform = args.platform
    if test_filename is None:
        transform_parsed(filepath, dirpath)
    else:
        build_parsed_data_from_output(test_filename, command, platform)
