"""Module for sentence database operations."""


from sqlalchemy import func, Column, Integer, Text
from sqlalchemy.exc import NoResultFound
from app.db_connection import get_db_session, Base


class Sentence(Base):
    __tablename__ = 'sentences'
    id = Column(Integer, primary_key=True)
    sentence = Column(Text)

    def __repr__(self):
        return f"{self.sentence}"


def get_sentence_by_id(sentence_id: int) -> Sentence:
    with get_db_session() as session:
        try:
            return session.query(Sentence).filter(Sentence.id == sentence_id).one()
        except NoResultFound:
            raise ValueError(f"Sentence with id {sentence_id} not found")


def get_random_sentence() -> Sentence | None:
    with get_db_session() as session:
        return session.query(Sentence).order_by(func.random()).first()


def get_random_sentence_by_word(word: str) -> str:
    with get_db_session() as session:
        random_sentence = session.query(Sentence)\
            .filter(Sentence.sentence.ilike(f'% {word} %'))\
            .order_by(func.random())\
            .first()
        
        if not random_sentence:
            raise ValueError(f"No sentences found containing the word '{word}'")
        
        return random_sentence.sentence
