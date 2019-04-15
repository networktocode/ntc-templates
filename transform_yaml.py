#!/usr/bin/env python
import os
import re
import glob
import numbers
import argparse

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as DQ


def transform_parsed(filepath=None, dirpath=None):
    if filepath is not None:
        ensure_yaml_standards(filepath)
    else:
        for file in glob.iglob("{0}/*.parsed".format(dirpath)):
            os.rename(file, file.replace(file[-6:], "yml"))
        for file in glob.iglob("{0}/*.yml".format(dirpath)):
            print(file)
            ensure_yaml_standards(file)


def ensure_yaml_standards(yaml_file):
    with open(yaml_file) as parsed_file:
        parsed_data = parsed_file.read()

    yaml_obj = YAML()
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ensures YAML files match project standards"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--filepath", type=str, help="The path to a YAML file.")
    group.add_argument(
        "-d",
        "--dirpath",
        type=str,
        help='The directory path to look for all files ending in ".parsed"',
    )
    args = parser.parse_args()

    transform_parsed(args.filepath, args.dirpath)
