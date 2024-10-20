from sqlalchemy import func
from sqlalchemy.exc import NoResultFound
from app.db_connection import get_db_session
from app.models import Sentence


def _execute_query(query_func):
    with get_db_session() as session:
        try:
            return query_func(session)
        except NoResultFound:
            return None


def get_sentence_by_id(sentence_id: int) -> Sentence:
    def query(session):
        result = session.query(Sentence).filter(Sentence.id == sentence_id).one()
        if not result:
            raise ValueError(f"Sentence with id {sentence_id} not found")
        return result

    return _execute_query(query)


def get_random_sentence() -> Sentence | None:
    return _execute_query(lambda session: session.query(Sentence).order_by(func.random()).first())


def get_random_sentence_by_word(word: str) -> str:
    def query(session):
        random_sentence = session.query(Sentence)\
            .filter(Sentence.sentence.ilike(f'%{word}%'))\
            .order_by(func.random())\
            .first()
        if not random_sentence:
            raise ValueError(f"No sentences found containing the word '{word}'")
        return random_sentence.sentence

    return _execute_query(query)
