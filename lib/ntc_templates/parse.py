"""ntc_templates.parse."""
import os
from textfsm import clitable


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
