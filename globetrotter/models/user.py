from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import validates
from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    
    correct_answers = Column(Integer, default=0)
    incorrect_answers = Column(Integer, default=0)
    score = Column(Integer, default=0)

    friends = Column(JSON, default=[])

    @validates("correct_answers", "incorrect_answers")
    def update_score(self, key, value):
        setattr(self, key, value)
        self.score = self.correct_answers - self.incorrect_answers
        return value
