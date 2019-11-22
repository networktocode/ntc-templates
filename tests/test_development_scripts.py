import os
import glob
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


@pytest.fixture
def teardown_normalize_file():
    filepaths = {}

    def _teardown_normalize_file(filepath):
        with open(filepath, encoding="utf-8") as fh:
            contents = fh.read()

        filepaths[filepath] = contents

    yield _teardown_normalize_file

    for filepath, contents in filepaths.items():
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(contents)


@pytest.fixture(scope="module")
def expected_file():
    expected_path = "tests/mocks/expected/parsed_sample.yml"
    with open(expected_path, encoding="utf-8") as fh:
        return fh.read()


@pytest.fixture(scope="module")
def expected_mac_file():
    expected_path = "tests/mocks/expected/show_mac.yml"
    with open(expected_path, encoding="utf-8") as fh:
        return fh.read()


@pytest.fixture
def teardown_delete_file():
    filepaths = []

    def _teardown_delete_file(filepath):
        filepaths.append(filepath)

    yield _teardown_delete_file

    for file in filepaths:
        os.remove(file)


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


def test_transform_file(teardown_normalize_file, expected_file):
    load_file = "tests/mocks/load/parsed_sample.yml"
    teardown_normalize_file(load_file)
    development_scripts.transform_file(load_file)
    with open(load_file, encoding="utf-8") as actual:
        assert actual.read() == expected_file


def test_transform_glob(teardown_normalize_file, expected_file):
    glob_dir = "tests/mocks/load/gl*"
    parsed_files = glob.glob(f"{glob_dir}/*.yml")
    for file in parsed_files:
        teardown_normalize_file(file)

    development_scripts.transform_glob(glob_dir)
    for file in parsed_files:
        with open(file, encoding="utf-8") as actual:
            assert actual.read() == expected_file


def test_ensure_yaml_standards(teardown_normalize_file, expected_file):
    load_file = "tests/mocks/load/parsed_sample.yml"
    teardown_normalize_file(load_file)
    with open(load_file, encoding="utf-8") as fh:
        load_yaml = development_scripts.YAML_OBJECT.load(fh)

    development_scripts.ensure_yaml_standards(load_yaml, load_file)
    with open(load_file, encoding="utf-8") as actual:
        assert actual.read() == expected_file


def test_parse_test_filepath():
    filepath = "tests/cisco_ios/show_version/cisco_ios_show_version.raw"
    platform, command, filename = development_scripts.parse_test_filepath(filepath)
    assert platform == "cisco_ios"
    assert command == "show version"
    assert filename == "cisco_ios_show_version"


def test_build_parsed_data_from_output(teardown_delete_file, expected_mac_file):
    load_file = "tests/mocks/cisco_ios/show_mac-address-table/show_mac1.raw"
    yaml_file = f"{load_file[:-3]}yml"
    teardown_delete_file(yaml_file)
    development_scripts.build_parsed_data_from_output(load_file, test_dir="tests/mocks")
    with open(yaml_file, encoding="utf-8") as actual:
        assert actual.read() == expected_mac_file


def test_build_parsed_data_from_dir(teardown_delete_file, expected_mac_file):
    glob_dir = "tests/mocks/cisco_ios/show_mac-*"
    command_files = glob.iglob(f"{glob_dir}/*.raw")
    parsed_files = [f"{file[:-3]}yml" for file in command_files]
    for file in parsed_files:
        teardown_delete_file(file)

    development_scripts.build_parsed_data_from_dir(glob_dir, test_dir="tests/mocks")
    for file in parsed_files:
        with open(file, encoding="utf-8") as actual:
            assert actual.read() == expected_mac_file
