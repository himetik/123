"""Contains all commands"""


import click
from app.sentence_extractor import get_sentence_by_id


@click.command()
@click.argument('id', type=int)
def num(id):
    sentence = get_sentence_by_id(id)
    if sentence:
        click.echo(sentence)
    else:
        click.echo(f"Sentence with ID {id} not found.")
