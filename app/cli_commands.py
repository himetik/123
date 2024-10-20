import click
from app.sentence_extractor import get_sentence_by_id, get_random_sentence, get_random_sentence_by_word
from app.sentence_validator import validate_sentence, SentenceValidationError, SentenceValidator
from app.sentence_inserter import insert_sentence
from app.text_loader import TextLoader
from app.text_validator import TextValidator
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
def put():
    while True:
        sentence_text = input("Enter a sentence (or 'q' to quit): ")
        if sentence_text.lower() == 'q':
            break

        try:
            if validate_sentence(sentence_text):
                if insert_sentence(sentence_text):
                    click.echo("Sentence added.")
                else:
                    click.echo("Failed to add sentence (it may already exist).")
            else:
                click.echo("The sentence did not pass validation.")
        except Exception as e:
            click.echo(f"Error processing the sentence: {e}")

    click.echo("Program finished.")


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

    for sentence in sentences:
        try:
            validator.validate(sentence)
            click.echo(f"{sentence}")
        except SentenceValidationError:
            continue

    click.echo("Bulk processing finished.")
