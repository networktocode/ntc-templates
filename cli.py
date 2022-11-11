"""CLI for acitool."""
import click

from tests.test_development_scripts import (
    build_parsed_data_from_dir,
    build_parsed_data_from_output,
    transform_file,
    transform_glob,
)


@click.group()
def base():
    """Base entry for click."""


@click.command()
@click.option(
    "-f",
    "--file",
    "file",
    type=str,
    help="File that you are targetting.",
)
def clean_yaml_file(file):
    """Transform a yaml file to expected output."""
    transform_file(file)


@click.command()
@click.option(
    "-f",
    "--folder",
    "folder",
    type=str,
    help="Folder that you are targetting.",
)
def clean_yaml_folder(folder):
    """Transform a yaml file to expected output to a folder."""
    transform_glob(folder)


@click.command()
@click.option(
    "-f",
    "--file",
    "file",
    type=str,
    help="File that you are targetting.",
)
def gen_yaml_file(file):
    """Generate a yaml file from raw a data file."""
    build_parsed_data_from_output(file, "./tests/")


@click.command()
@click.option(
    "-f",
    "--folder",
    "folder",
    type=str,
    help="Folder that you are targetting.",
)
def gen_yaml_folder(folder):
    """Generate a yaml file from folder of raw data files."""
    build_parsed_data_from_dir(folder, "./tests/")


base.add_command(clean_yaml_file)
base.add_command(clean_yaml_folder)
base.add_command(gen_yaml_file)
base.add_command(gen_yaml_folder)

if __name__ == "__main__":
    base()
