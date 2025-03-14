from sqlalchemy import Column, Integer, String, ForeignKey
from database.db import Base

class FunFact(Base):
    __tablename__ = "fun_facts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    destination_id = Column(Integer, ForeignKey("destinations.id"), nullable=False)
    text = Column(String, nullable=False)
