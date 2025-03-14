from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)

    # Relationships
    clues = relationship("Clue", backref="destination", cascade="all, delete-orphan")
    fun_facts = relationship("FunFact", backref="destination", cascade="all, delete-orphan")
    trivia = relationship("Trivia", backref="destination", cascade="all, delete-orphan")
