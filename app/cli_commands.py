import click
from app.sentence_extractor import get_random_sentence, get_random_sentence_by_word
from app.sentence_validator import SentenceValidationError, SentenceValidator
from app.sentence_inserter import insert_sentence
from app.text_loader import TextLoader
from app.text_separator import SentenceSplitter


def echo_sentence(sentence, not_found_message):
    click.echo(sentence if sentence else not_found_message)


@click.group()
def cli():
    pass


@cli.command()
def random():
    sentence = get_random_sentence()
    echo_sentence(sentence, "No sentences available.")


@cli.command()
@click.argument('word', type=str)
def word(word):
    try:
        sentence = get_random_sentence_by_word(word)
        echo_sentence(sentence, f"Sentence containing the word '{word}' not found.")
    except ValueError as e:
        click.echo(str(e))


@cli.command()
def bulk():
    loader = TextLoader()
    splitter = SentenceSplitter()
    validator = SentenceValidator()

    text = loader.load_bulk_text()
    if not text:
        click.echo("Error: The loaded text is empty. Please check the input data.")
        return

    sentences = splitter.split_text(text)
    valid_sentences = [sentence for sentence in sentences if _is_valid_sentence(sentence, validator)]

    if not valid_sentences:
        click.echo("No valid sentences found to save.")
        return

    _display_valid_sentences(valid_sentences)
    if _confirm_save():
        _save_sentences(valid_sentences)


def _is_valid_sentence(sentence, validator):
    try:
        validator.validate(sentence)
        return True
    except SentenceValidationError:
        return False


def _display_valid_sentences(sentences):
    click.echo("The following valid sentences have been found:")
    for sentence in sentences:
        click.echo(f"- {sentence}")


def _confirm_save():
    return click.confirm("Do you want to save these sentences to the database?")


def _save_sentences(sentences):
    for sentence in sentences:
        insert_sentence(sentence)
    click.echo("Sentences have been successfully saved to the database.")
