"""Ensure that testcases exist for all templates."""
import os
import glob
import re
import pytest

from tests import load_index_data


def extract_index_data():
    """Used to parametrize and report each test case
    with the necessary data
    """
    index = sorted(load_index_data())
    refined_index = []
    for row in index:
        template = row[0].strip()
        template_short = template.split(".template")[0]
        platform = row[2].strip()
        for directory in os.listdir("tests"):
            if re.match(platform, directory):
                platform_directory = directory
                break
        cut = len(platform_directory) + 1
        command = template_short[cut:]
        refined_index.append((platform_directory, command, template))
    return refined_index


@pytest.mark.parametrize("platform_directory,command,template", extract_index_data())
def test_verify_parsed_and_reference_data_exists(platform_directory, command, template):
    """Verify that at least one test exists for all entries in the index file.
    """
    cases = "tests/{0}/{1}/*.raw".format(platform_directory, command)
    test_list = glob.glob(cases)
    assert len(test_list) != 0, "Could not find tests for {0}".format(template)
