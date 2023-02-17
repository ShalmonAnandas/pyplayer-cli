#!/usr/bin/env python
"""Command-line interface."""
import click
from rich import traceback


@click.command()
@click.version_option(version="1.1.0", message=click.style("pyplayer-cli Version: 1.1.0"))
def main() -> None:
    """pyplayer-cli."""


if __name__ == "__main__":
    traceback.install()
    main(prog_name="pyplayer-cli")  # pragma: no cover

#initial commit from college computer