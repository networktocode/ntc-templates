from copy import deepcopy

import pytest
from ruamel.yaml.compat import StringIO

import development_scripts


@pytest.fixture(scope="module")
def yaml_comments_file():
    with open("tests/mocks/load/yaml_comments.yml", encoding="utf-8") as fh:
        return development_scripts.YAML_OBJECT.load(fh)


@pytest.fixture
def copy_yaml_comments(yaml_comments_file):
    return deepcopy(yaml_comments_file)


def test_ensure_spacing_for_multiline_comment():
    remark = "comment 11\n#        comment 12\n#comment 13\n"
    remark_formatted = development_scripts.ensure_spacing_for_multiline_comment(remark)
    assert remark_formatted == "comment 11\n# comment 12\n# comment 13"


def test_ensure_space_after_octothorpe(copy_yaml_comments):
    comment = copy_yaml_comments.ca.items["b"][2]
    development_scripts.ensure_space_after_octothorpe(comment)
    assert comment.value == "# comment 2\n# comment 3\n"


def test_ensure_space_comments(copy_yaml_comments):
    comments = copy_yaml_comments.ca.items
    comment_values = comments.values()
    development_scripts.ensure_space_comments(comment_values)
    assert comments["a"][2].value == "# comment 1\n"
    assert comments["b"][2].value == "# comment 2\n# comment 3\n"
    assert comments["d"][3][0].value == "# comment 7\n"


def test_update_yaml_comments(copy_yaml_comments):
    development_scripts.update_yaml_comments(copy_yaml_comments)
    string_yaml = StringIO()
    development_scripts.YAML_OBJECT.dump(copy_yaml_comments, string_yaml)
    actual = string_yaml.getvalue()
    with open("tests/mocks/expected/yaml_comments.yml", encoding="utf-8") as fh:
        expected = fh.read()
    assert actual == expected
