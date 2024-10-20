import click
from .cli_commands import id, random, word, put, bulk


@click.group()
def cli() -> None:
    pass


def register_commands() -> None:
    commands = [id, random, word, put, bulk]
    for command in commands:
        cli.add_command(command)


register_commands()


if __name__ == '__main__':
    cli()
