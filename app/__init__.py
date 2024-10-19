"""Commands registration"""


import click
from .commands import ok


@click.group()
def cli():
    pass


cli.add_command(ok)
