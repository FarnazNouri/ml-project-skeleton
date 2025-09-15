"""Console script for mlProject."""

import typer
from rich.console import Console

from mlProject import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for mlProject."""
    console.print("Replace this message by putting your code into "
               "mlProject.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
