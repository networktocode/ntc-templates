#!/usr/bin/env python

"""Run tests against all the *.textfsm template files."""
import glob
import re

import pytest


# https://github.com/google/textfsm/wiki/TextFSM#value-definitions
OPTION_KEYWORDS = ["Filldown", "Key", "Required", "List", "Fillup"]
CG_REGEX = rf"^Value\s+(?:(?:(?:{'|'.join(OPTION_KEYWORDS)}),?)+\s+)?(\S+)"


def return_template_files():
    """Return a list of all the *.textfsm template files."""
    return glob.glob("./ntc_templates/templates/*.textfsm")


@pytest.fixture(scope="function", params=return_template_files())
def load_template_files(request):
    """Return each *.textfsm file to run the capture group test on."""
    return request.param


def return_template_capture_groups(template_file):
    """Return a list of capture groups in a template."""
    with open(template_file, encoding="utf-8") as fh:
        file = fh.read()
        return re.findall(CG_REGEX, file, re.MULTILINE)


def test_uppercase_capture_group(load_template_files):
    """Test that the capture groups are uppercase."""
    capture_groups = return_template_capture_groups(load_template_files)

    for group in capture_groups:
        assert group.isupper()
