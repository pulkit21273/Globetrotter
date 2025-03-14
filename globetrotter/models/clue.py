from sqlalchemy import Column, Integer, String, ForeignKey
from database.db import Base

class Clue(Base):
    __tablename__ = "clues"

    id = Column(Integer, primary_key=True, autoincrement=True)
    destination_id = Column(Integer, ForeignKey("destinations.id"), nullable=False)
    text = Column(String, nullable=False)
