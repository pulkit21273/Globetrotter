from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY, Boolean, DateTime
from database.db import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class GameSession(Base):
    __tablename__ = "game_sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    already_seen_destinations_ids = Column((Integer), default=[]) 
    current_question = Column(Integer, default=1)
    current_q_id = Column(Integer, default=0)
    is_completed = Column(Boolean, default=False)
    completed_at = Column(DateTime, default=datetime.utcnow)
    session_score = Column(Integer, default=0)

    user = relationship("User", backref="game_sessions")


    # destination_id = Column(Integer, ForeignKey("destinations.id", ondelete="CASCADE"), nullable=False)
    # text = Column(String, nullable=False)
