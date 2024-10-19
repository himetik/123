import click
from typing import Any
from .commands import num, random, word


@click.group()
def cli() -> None:
    pass


def register_commands() -> None:
    commands = [num, random, word]
    for command in commands:
        cli.add_command(command)


register_commands()


if __name__ == '__main__':
    cli()
