import spacy
import os
from dotenv import load_dotenv
from typing import Set, Tuple, List


load_dotenv()


def load_profanities(filepath: str) -> Set[str]:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return set(line.strip().lower() for line in f)
    except FileNotFoundError:
        print(f"Файл {filepath} не найден. Используется пустой список нецензурных слов.")
        return set()


profanity_file = os.getenv("PROFANITY_FILE", ".profanities")
profanity_list = load_profanities(profanity_file)


nlp = spacy.load("en_core_web_sm")


def moderate_profanity(text: str) -> Tuple[bool, List[str]]:
    doc = nlp(text.lower())
    profanity_found = [token.text for token in doc if token.lemma_ in profanity_list]
    return bool(profanity_found), profanity_found
