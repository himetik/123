import re
from typing import List, Callable
from app.sentence_moderator import moderate_profanity


class SentenceValidationError(Exception):
    pass


class SentenceValidator:
    def __init__(self):
        self.rules: List[Callable[[str], None]] = [
            self._check_not_empty,
            self._check_length,
            self._check_capitalization,
            self._check_ending_punctuation,
            self._check_no_newlines,
            self._check_letter_percentage,
            self._check_allowed_characters,
            self._check_word_count,
            self._check_no_extra_spaces,
            self._check_profanity
        ]

    def validate(self, sentence: str) -> bool:
        for rule in self.rules:
            rule(sentence)
        return True

    def _check_not_empty(self, sentence: str) -> None:
        if not sentence:
            raise SentenceValidationError("Sentence must not be empty.")

    def _check_length(self, sentence: str) -> None:
        if len(sentence) < 6:
            raise SentenceValidationError("Sentence must be at least 6 characters long.")
        if len(sentence) > 180:
            raise SentenceValidationError("Sentence must not exceed 180 characters.")

    def _check_capitalization(self, sentence: str) -> None:
        if not sentence[0].isupper():
            raise SentenceValidationError("Sentence must start with a capital letter.")

    def _check_ending_punctuation(self, sentence: str) -> None:
        if not re.search(r'[.!?]$', sentence):
            raise SentenceValidationError("Sentence must end with '.', '!', or '?'.")

    def _check_no_newlines(self, sentence: str) -> None:
        if '\n' in sentence:
            raise SentenceValidationError("Sentence must not contain newline characters.")

    def _check_letter_percentage(self, sentence: str) -> None:
        letter_count = sum(1 for char in sentence if char.isalpha())
        if letter_count < len(sentence) / 2:
            raise SentenceValidationError("Sentence must contain at least 50% letters.")

    def _check_allowed_characters(self, sentence: str) -> None:
        if not re.match(r'^[A-Za-z0-9\s.!?,;:\'-]+$', sentence):
            raise SentenceValidationError("Sentence must only contain English letters, numbers, and basic punctuation.")

    def _check_word_count(self, sentence: str) -> None:
        if len(sentence.split()) < 2:
            raise SentenceValidationError("Sentence must consist of at least 2 words.")

    def _check_no_extra_spaces(self, sentence: str) -> None:
        if '  ' in sentence:
            raise SentenceValidationError("Sentence must not contain extra spaces.")

    def _check_profanity(self, sentence: str) -> None:
        has_profanity, profanities = moderate_profanity(sentence)
        if has_profanity:
            raise SentenceValidationError(f"Sentence contains profanity: {', '.join(profanities)}.")


def validate_sentence(sentence: str) -> bool:
    validator = SentenceValidator()
    return validator.validate(sentence)
