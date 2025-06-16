#!/usr/bin/env python

"""Run tests against all the *.textfsm template files."""
import glob
import re

import pytest


# https://github.com/google/textfsm/wiki/TextFSM#value-definitions
OPTION_KEYWORDS = ["Filldown", "Key", "Required", "List", "Fillup"]
RE_CAPGRP = re.compile(rf"^Value\s+(?:(?:(?:{'|'.join(OPTION_KEYWORDS)}),?)+\s+)?(\S+)", re.MULTILINE)  # noqa: E231


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
        return RE_CAPGRP.findall(file)


def test_uppercase_capture_group(load_template_files):
    """Test that the capture groups are uppercase."""
    capture_groups = return_template_capture_groups(load_template_files)

    # catch non-functional regexes and re function syntax which match nothing
    assert capture_groups != [], "No capture groups were matched, check regex function syntax/usage"

    for group in capture_groups:
        if "bogus" in load_template_files:
            # The bogus file intentionally has lowercase/titlecase capture groups
            #   (for that file it should always evaluate to false)
            assert group.isupper() is False, "Error: Bogus test case should never evaluate to True"
        else:
            # Otherwise capture groups are uppercase and compliant with the project guidelines
            assert group.isupper(), "Capture groups need to be uppercase per project guidelines"
