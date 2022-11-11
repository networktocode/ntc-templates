#!/usr/bin/env python

"""Run tests against all the *.raw files."""
import glob
import os

import pytest
import yaml

from ntc_templates.parse import parse_output


def return_test_files():
    """Return a list of all the *.raw files to run tests against."""
    platform_dirs = glob.glob("tests/*")
    platforms = (glob.glob(f"{platform}/*") for platform in platform_dirs)
    template_dirs = (item for sublist in platforms for item in sublist)
    test_commands = (glob.glob(f"{template_dir}/*.raw") for template_dir in template_dirs)

    return (item for sublist in test_commands for item in sublist)


@pytest.fixture(scope="function", params=return_test_files())
def load_template_test(request):
    """Return each *.raw file to run tests on."""
    return request.param


def raw_template_test(raw_file):
    """Return structured data along with reference data."""
    parsed_file = f"{raw_file[:-4]}.yml"
    parts = os.path.normpath(raw_file).split(os.sep)
    platform = parts[1]
    command = " ".join(parts[2].split("_"))
    with open(raw_file, "r", encoding="utf-8") as data:
        rawoutput = data.read()
    structured = parse_output(platform=platform, command=command, data=rawoutput)
    with open(parsed_file, "r", encoding="utf-8") as data:
        parsed_data = yaml.safe_load(data.read())

    return structured, parsed_data["parsed_sample"]


def test_raw_data_against_mock(load_template_test):
    processed, reference = raw_template_test(load_template_test)

    correct_number_of_entries_test(processed, reference)
    all_entries_have_the_same_keys_test(processed, reference)
    correct_data_in_entries_test(processed, reference)


def correct_number_of_entries_test(processed, reference):
    """Test that the number of entries returned are the same as the control.

    This will create a test for each of the files in the test_collection
    variable.
    """
    assert len(processed) == len(reference)


def all_entries_have_the_same_keys_test(processed, reference):
    """Test that the keys of the returned data are the same as the control.

    This will create a test for each of the files in the test_collection
    variable.
    """
    for count, value in enumerate(processed):
        proc = set(value.keys())
        ref = set(reference[count].keys())
        diff = proc.symmetric_difference(ref)
        assert not diff, "Key diffs: " + ", ".join(diff)


def correct_data_in_entries_test(processed, reference):
    """Test that the actual data in each entry is the same as the control.

    This will create a test for each of the files in the test_collection
    variable.
    """
    # Can be uncommented if we don't care that the parsed data isn't
    # in the same order as the raw data
    # reference = sorted(reference)
    # processed = sorted(processed)

    for count, value in enumerate(reference):
        for key in value.keys():
            assert processed[count][key] == value[key], f"entry #{count}, key: {key}"
