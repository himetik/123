"""Contains all commands"""


import click
from app.sentence_extractor import get_sentence_by_id, get_random_sentence, get_random_sentence_by_word
from app.sentence_validator import validate_sentence, SentenceValidationError


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


@click.command()
@click.argument('word', type=str)
def word(word):
    sentence = get_random_sentence_by_word(word)
    if sentence:
        click.echo(sentence)
    else:
        click.echo(f"Sentence containing word '{word}' not found")


@click.command()
def put():
    while True:
        statement = click.prompt("Enter a statement to validate (or '\quit' to exit)")

        if statement.lower() == '\quit':
            click.echo("Exiting the validation process.")
            break

        try:
            validate_sentence(statement)
            click.echo(f'"{statement}" is valid.')
        except SentenceValidationError as e:
            click.echo(f"Error: {e}")

        click.echo()
