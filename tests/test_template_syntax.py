#!/usr/bin/env python

"""Run syntax tests against all the *.textfsm template files."""

import glob
import re

import pytest
import textfsm

# Rules and comments inside a state must be indented with exactly 2 spaces.
RE_INDENTED_LINE = re.compile(r"^([ \t]+)(\S)")
VALID_INDENTED_LINES = {("  ", "^"), ("  ", "#")}
# States that are valid without being referenced by another rule.
IMPLICIT_STATES = {"Start", "End", "EOF"}


def return_template_files():
    """Return a list of all the *.textfsm template files."""
    return glob.glob("./ntc_templates/templates/*.textfsm")


@pytest.fixture(scope="function", params=return_template_files())
def load_template_files(request):
    """Return each *.textfsm file to run the syntax tests on."""
    return request.param


def test_template_compiles(load_template_files):
    """Test that each template compiles with the textfsm parser.

    Compilation catches invalid rule indentation, references to undefined
    states, a missing Start state, and duplicate state names.
    """
    with open(load_template_files, encoding="utf-8") as fh:
        textfsm.TextFSM(fh)


def test_rule_indentation(load_template_files):
    """Test that every rule or comment line is indented with exactly 2 spaces."""
    bad_lines = []
    with open(load_template_files, encoding="utf-8") as fh:
        for line_num, line in enumerate(fh, start=1):
            match = RE_INDENTED_LINE.match(line)
            if match and (match.group(1), match.group(2)) not in VALID_INDENTED_LINES:
                bad_lines.append(line_num)

    assert not bad_lines, f"Rules must be indented with exactly 2 spaces, see line(s): {bad_lines}"


def test_no_unused_states(load_template_files):
    """Test that every defined state is reachable from another rule."""
    with open(load_template_files, encoding="utf-8") as fh:
        fsm = textfsm.TextFSM(fh)

    referenced_states = {rule.new_state for rules in fsm.states.values() for rule in rules}
    unused_states = set(fsm.states) - IMPLICIT_STATES - referenced_states

    assert not unused_states, f"State(s) defined but never referenced by a rule: {sorted(unused_states)}"
