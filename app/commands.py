"""Contains all commands"""


import click


@click.command()
def ok():
    click.echo('ok')
