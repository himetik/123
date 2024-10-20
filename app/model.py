from sqlalchemy import Column, Integer, Text
from app.db_connection import Base


class Sentence(Base):
    __tablename__ = 'sentences'
    id = Column(Integer, primary_key=True)
    sentence = Column(Text)

    def __repr__(self):
        return f"{self.sentence}"
