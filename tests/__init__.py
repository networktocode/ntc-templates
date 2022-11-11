"""tests."""

import os
import csv

from ntc_templates.parse import _get_template_dir


def load_index_data():
    """Load data from index file."""
    with open(f"{_get_template_dir()}{os.sep}index", encoding="utf-8") as indexfs:
        data = csv.reader(indexfs)
        return [row for row in data if len(row) > 2 and row[0] != "Template"]
