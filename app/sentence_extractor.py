"""Extracts sentences from the database"""


from sqlalchemy import Column, Integer, Text
from app.db_connection import get_db_session, Base


class Sentence(Base):
    __tablename__ = 'sentences'

    id = Column(Integer, primary_key=True)
    sentence = Column(Text)

    def __repr__(self):
        return f"{self.sentence}"


def get_sentence_by_id(sentence_id):
    with get_db_session() as session:
        sentence = session.query(Sentence).filter(Sentence.id == sentence_id).first()
        if sentence is None:
            raise ValueError(f"Sentence with id {sentence_id} not found")
        return sentence
