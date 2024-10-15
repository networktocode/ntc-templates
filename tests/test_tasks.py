"""Test functions for tasks.py."""

import pytest

from tasks import strtobool


@pytest.mark.parametrize(
    "test_case, expected",
    [
        ("y", True),
        ("yes", True),
        ("true", True),
        ("t", True),
        ("on", True),
        ("1", True),
        ("n", False),
        ("no", False),
        ("false", False),
        ("f", False),
        ("off", False),
        ("0", False),
    ],
)
def test_strtobool(test_case, expected):
    """Test strtobool function."""
    assert strtobool(test_case) == expected


def test_strtobool_error():
    """Test generation of the error message."""
    with pytest.raises(ValueError) as excinfo:
        strtobool("invalid")
    assert "Invalid truth value invalid" in str(excinfo.value)
