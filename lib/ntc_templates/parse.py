"""ntc_templates.parse."""
import os

# Due to TextFSM library issues on Windows, it is better to not fail on import
# Instead fail at runtime (i.e. if method is actually used).
try:
    from textfsm import clitable

    HAS_CLITABLE = True
except ImportError:
    HAS_CLITABLE = False


def _get_template_dir():
    package_dir = os.path.dirname(__file__)
    template_dir = os.path.join(package_dir, "templates")
    if not os.path.isdir(template_dir):
        project_dir = os.path.dirname(os.path.dirname(os.path.dirname(template_dir)))
        template_dir = os.path.join(project_dir, "templates")

    return template_dir


def _clitable_to_dict(cli_table):
    """Convert TextFSM cli_table object to list of dictionaries."""
    objs = []
    for row in cli_table:
        temp_dict = {}
        for index, element in enumerate(row):
            temp_dict[cli_table.header[index].lower()] = element
        objs.append(temp_dict)

    return objs


def parse_output(platform=None, command=None, data=None):
    """Return the structured data based on the output from a network device."""

    if not HAS_CLITABLE:
        msg = """
The TextFSM library is not currently supported on Windows. If you are NOT using Windows
you should be able to 'pip install textfsm' to fix this issue. If you are using Windows
then you will need to install the patch referenced here:

https://github.com/google/textfsm/pull/82

"""
        raise ImportError(msg)

    template_dir = _get_template_dir()
    cli_table = clitable.CliTable("index", template_dir)

    attrs = {"Command": command, "Platform": platform}
    try:
        cli_table.ParseCmd(data, attrs)
        structured_data = _clitable_to_dict(cli_table)
    except clitable.CliTableError as e:
        raise Exception(
            'Unable to parse command "{0}" on platform {1} - {2}'.format(
                command, platform, str(e)
            )
        )
        # Invalid or Missing template
        # module.fail_json(msg='parsing error', error=str(e))
        # rather than fail, fallback to return raw text
        # structured_data = [data]

    return structured_data
