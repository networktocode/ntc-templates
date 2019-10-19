try:
    from textfsm import clitable
except:
    import clitable

from ntc_templates.parse import _get_template_dir

def test_index():
    template_dir = _get_template_dir()
    cli_table = clitable.CliTable('index', template_dir)
    headers = list(cli_table.index.index.header)
    assert cli_table.index.index.size > 0
    assert len(headers) > 0
    assert "Platform" in headers
    assert "Command" in headers
