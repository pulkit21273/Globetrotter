from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    score = Column(Integer, default=0)

    # Relationships
    games = relationship("Game", backref="user", cascade="all, delete-orphan")
    invitations_sent = relationship("Invitation", foreign_keys="[Invitation.inviter_id]", backref="inviter")
