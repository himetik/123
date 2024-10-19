"""Contains all commands"""


import click
from app.sentence_extractor import get_sentence_by_id, get_random_sentence


@click.command()
@click.argument('id', type=int)
def num(id):
    sentence = get_sentence_by_id(id)
    if sentence:
        click.echo(sentence)
    else:
        click.echo(f"Sentence with ID {id} not found.")


@click.command()
def random():
    sentence = get_random_sentence()
    if sentence:
        click.echo(sentence)
    else:
        click.echo("No sentences available.")
