import click
from app.sentence_extractor import get_sentence_by_id, get_random_sentence, get_random_sentence_by_word
from app.sentence_validator import validate_sentence
from app.sentence_database_insertion_handler import insert_sentence


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
        click.echo(f"Sentence containing the word '{word}' not found.")


@click.command()
def put():
    while True:
        sentence_text = input("Enter a sentence (or 'q' to quit): ")
        if sentence_text.lower() == 'q':
            break

        try:
            validation_result = validate_sentence(sentence_text)
            
            if validation_result:
                insert_result = insert_sentence(sentence_text)
                if insert_result:
                    click.echo("Sentence added.")
                else:
                    click.echo("Failed to add sentence (it may already exist).")
            else:
                click.echo("The sentence did not pass validation.")
        except Exception as e:
            click.echo(f"Error processing the sentence: {e}")

    print("Program finished.")
