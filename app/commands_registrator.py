"""Commands registration"""


import click
from .commands import num


@click.group()
def cli():
    pass


cli.add_command(num)


if __name__ == '__main__':
    cli()
