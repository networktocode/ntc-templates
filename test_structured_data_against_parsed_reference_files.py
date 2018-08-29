#!/usr/bin/env python

"""Run tests against all the *.raw files."""
import glob
import pytest
import yaml
try:
    import clitable
except:
    import textfsm.clitable as clitable


def return_test_files():
    """Return a list of all the *.raw files to run tests against."""
    platform_dirs = glob.glob('tests/*')

    platforms = []
    for platform in platform_dirs:
        platforms.append(glob.glob('%s/*' % platform))

    template_dirs = [item for sublist in platforms for item in sublist]

    test_commands = []
    for template_dir in template_dirs:
        test_commands.append(glob.glob('%s/*.raw' % template_dir))

    return [item for sublist in test_commands for item in sublist]


def clitable_to_dict(cli_table):
    """Convert TextFSM cli_table object to list of dictionaries."""
    objs = []
    for row in cli_table:
        temp_dict = {}
        for index, element in enumerate(row):
            temp_dict[cli_table.header[index].lower()] = element
        objs.append(temp_dict)

    return objs


def get_structured_data(platform, command, rawoutput):
    """Return the structured data."""
    cli_table = clitable.CliTable('index', 'templates')

    attrs = dict(
        Command=command,
        Platform=platform
    )
    cli_table.ParseCmd(rawoutput, attrs)
    structured_data = clitable_to_dict(cli_table)

    return structured_data

# Populate test_collection with a list of all the .raw template files we want
# to run tests against
test_collection = return_test_files()


@pytest.fixture(scope='function', params=test_collection)
def load_template_test(request):
    """Return each *.raw file to run tests on."""
    return request.param


def raw_template_test(raw_file):
    """Return structured data along with reference data."""
    parsed_file = '%s.parsed' % raw_file[:-4]
    parts = raw_file.split('/')
    platform = parts[1]
    command = ' '.join(parts[2].split('_'))
    with open(raw_file, 'r') as data:
        rawoutput = data.read()
    structured = get_structured_data(platform, command, rawoutput)
    with open(parsed_file, 'r') as data:
        parsed_data = yaml.load(data.read())

    return structured, parsed_data['parsed_sample']


def test_correct_number_of_entries(load_template_test):
    """Test that the number of entries returned are the same as the control.

    This will create a test for each of the files in the test_collection
    variable.
    """
    processed, reference = raw_template_test(load_template_test)

    assert len(processed) == len(reference)


def test_that_all_entries_have_the_same_keys(load_template_test):
    """Test that the keys of the returned data are the same as the control.

    This will create a test for each of the files in the test_collection
    variable.
    """
    processed, reference = raw_template_test(load_template_test)

    for i in range(len(processed)):
        assert sorted(processed[i].keys()) == sorted(reference[i].keys())


def test_correct_data_in_entries(load_template_test):
    """Test that the actual data in each entry is the same as the control.

    This will create a test for each of the files in the test_collection
    variable.
    """
    processed, reference = raw_template_test(load_template_test)

    # Can be uncommented if we don't care that the parsed data isn't
    # in the same order as the raw data
    # reference = sorted(reference)
    # processed = sorted(processed)

    for i in range(len(reference)):
        for key in reference[i].keys():
            assert processed[i][key] == reference[i][key]


def test_that_all_entries_dicts_match(load_template_test):
    """Test that the values of the dicts returned are the same as the control.

    This test swaps place with the processed and reference variable so it's not run
    in the same order as test_correct_data_in_entries to catch dicts with extra keys

    This will create a test for each of the files in the test_collection
    variable.
    """
    processed, reference = raw_template_test(load_template_test)

    # Can be uncommented if we don't care that the parsed data isn't
    # in the same order as the raw data
    # reference = sorted(reference)
    # processed = sorted(processed)

    for i in range(len(processed)):
        assert processed[i] == reference[i]
