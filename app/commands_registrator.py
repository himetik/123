"""Commands registration"""


import click
from .commands import num, random


@click.group()
def cli():
    pass


cli.add_command(num)
cli.add_command(random)

if __name__ == '__main__':
    cli()
