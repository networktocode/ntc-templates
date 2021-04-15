"""Ensure that testcases exist for all templates."""
import os
import glob
import re
import pytest

from tests import load_index_data


TEST_DIRECTORIES = os.listdir("tests")


def extract_index_data():
    """Used to parametrize and report each test case with the necessary data."""
    index = sorted(load_index_data())
    mock_directories = []
    for row in index:
        # Trim template name to only parts making up platform and command directories
        template = row[0].strip()
        template_short = template.split(".textfsm")[0]
        # Get RegEx pattern to strip platform from template name
        platform = row[2].strip()
        # The platform attribute is a RegEx pattern,
        # so need to loop through each platform looking to find a match
        # in order to accurately derive platform name
        for directory in TEST_DIRECTORIES:
            if re.match(rf"{platform}", directory):
                platform = directory
                break
        cut = len(platform) + 1
        command = template_short[cut:]
        mock_directories.append(f"tests/{platform}/{command}")
    return mock_directories


@pytest.mark.parametrize("mock_directory", extract_index_data())
def test_verify_parsed_and_reference_data_exists(mock_directory):
    """Verify that at least one test exists for all entries in the index file."""
    cases = f"{mock_directory}/*.raw"
    test_list = glob.glob(cases)
    assert len(test_list) != 0, f"Could not find tests for {mock_directory}.textfsm"
