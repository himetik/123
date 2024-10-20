import click
from app.sentence_extractor import get_sentence_by_id, get_random_sentence, get_random_sentence_by_word
from app.sentence_validator import SentenceValidationError, SentenceValidator
from app.sentence_inserter import insert_sentence
from app.text_loader import TextLoader
from app.text_separator import SentenceSplitter


def echo_sentence(sentence, not_found_message):
    click.echo(sentence if sentence else not_found_message)


@click.command()
@click.argument('id', type=int)
def id(id):
    sentence = get_sentence_by_id(id)
    echo_sentence(sentence, f"Sentence with ID {id} not found.")


@click.command()
def random():
    sentence = get_random_sentence()
    echo_sentence(sentence, "No sentences available.")


@click.command()
@click.argument('word', type=str)
def word(word):
    try:
        sentence = get_random_sentence_by_word(word)
        echo_sentence(sentence, f"Sentence containing the word '{word}' not found.")
    except ValueError as e:
        click.echo(str(e))


@click.command()
def bulk():
    loader = TextLoader()
    splitter = SentenceSplitter()

    text = loader.load_bulk_text()

    if not text:
        click.echo("Error: The loaded text is empty. Please check the input data.")
        return

    sentences = splitter.split_text(text)
    validator = SentenceValidator()
    valid_sentences = []

    for sentence in sentences:
        try:
            validator.validate(sentence)
            valid_sentences.append(sentence)
        except SentenceValidationError:
            continue

    click.echo("The following valid sentences have been found:")
    for sentence in valid_sentences:
        click.echo(f"- {sentence}")

    if not valid_sentences:
        click.echo("No valid sentences found to save.")
        return

    confirmation = input("Do you want to save these sentences to the database? (y/n): ")
    if confirmation.lower() == 'y':
        for sentence in valid_sentences:
            insert_sentence(sentence)
        click.echo("Sentences have been successfully saved to the database.")
    else:
        click.echo("The sentences were not saved.")

    click.echo("Bulk processing finished.")
