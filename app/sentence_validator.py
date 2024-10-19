import re


class SentenceValidationError(Exception):
    pass


def validate_sentence(sentence: str) -> None:

    if not sentence:
        raise SentenceValidationError("Sentence must not be empty.")

    if len(sentence) < 6:
        raise SentenceValidationError("Sentence must be at least 6 characters long.")

    if len(sentence) > 180:
        raise SentenceValidationError("Sentence must not exceed 180 characters.")

    if not sentence[0].isupper():
        raise SentenceValidationError("Sentence must start with a capital letter.")

    if not re.search(r'[.!?]$', sentence):
        raise SentenceValidationError("Sentence must end with '.', '!', or '?'.")

    if '\n' in sentence:
        raise SentenceValidationError("Sentence must not contain newline characters.")

    letter_count = sum(1 for char in sentence if char.isalpha())
    total_count = len(sentence)

    if letter_count < total_count / 2:
        raise SentenceValidationError("Sentence must contain at least 50% letters.")

    if not re.match(r'^[A-Za-z0-9\s.!?,;:-]+$', sentence):
        raise SentenceValidationError("Sentence must only contain English letters, numbers, and basic punctuation.")

    if len(sentence.split()) < 2:
        raise SentenceValidationError("Sentence must consist of at least 2 words.")

    if '  ' in sentence:
        raise SentenceValidationError("Sentence must not contain extra spaces.")
