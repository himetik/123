import click
from .cli_commands import random, word, bulk


@click.group()
def cli() -> None:
    pass


def register_commands() -> None:
    commands = [random, word, bulk]
    for command in commands:
        cli.add_command(command)


register_commands()


if __name__ == '__main__':
    cli()
