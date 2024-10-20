from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from app.db_connection import Base


class Sentence(Base):
    __tablename__ = 'sentences'

    id = Column(Integer, primary_key=True)
    sentence = Column(Text, nullable=False, unique=True, index=True)

    def __repr__(self):
        return f"<Sentence(id={self.id}, sentence='{self.sentence[:50]}...', created_at={self.created_at})>"

    def __str__(self):
        return self.sentence
