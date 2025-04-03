from database.db import engine
from sqlalchemy.orm import sessionmaker
from sanic.response import json
from models import Destination, Clue, Trivia, FunFact, User, GameSession
import random
from sqlalchemy import func
from datetime import datetime


Session = sessionmaker(bind=engine)
session = Session()

class GameController:

    @classmethod
    async def get_or_create_game_session(cls, user_id):
        active_session = session.query(GameSession).filter_by(
            user_id=user_id,
            is_completed = False
        ).order_by(GameSession.completed_at.desc()).first()

        if active_session:
            return active_session
        
        new_session = GameSession(user_id=user_id)
        session.add(new_session)
        session.commit()
        return new_session

    @classmethod
    async def generate_fetch_question_payload(cls, destination):

        clues = session.query(Clue).filter_by(destination_id=destination.id).all()
        clues_list = [{"id": clue.id, "text": clue.text} for clue in clues]

        options = session.query(Destination.id, (Destination.city + ', ' + Destination.country).label('option')) \
                        .filter(Destination.id != destination.id) \
                        .order_by(func.random()) \
                        .limit(3).all()

        options_list = [{"id": option.id, "option": option.option} for option in options]

        correct_option = {"id": destination.id, "option": destination.city + ', ' + destination.country}
        options_list.append(correct_option)

        random.shuffle(options_list)

        return {
            "clues_list": clues_list,
            "options": options_list
        }
    
    @classmethod
    async def calculate_user_score(cls, user_id, is_correct, no_of_hints_used, game_session_id, clue_id):
        user = session.query(User).filter_by(id=user_id).first()
        game_session = session.query(GameSession).filter_by(id=game_session_id, user_id=user_id).first()

        if not user or not game_session:
            return json({"error":"user or game session not found"})
        
        clue = session.query(Clue).filter_by(id=clue_id).first()

        if clue.destination_id not in game_session.already_seen_destinations_ids:
            game_session.already_seen_destinations_ids.append(clue.destination_id)


        question_score=0
        if is_correct:
            if no_of_hints_used == 0:
                score_value=10
                question_score = 10
            elif no_of_hints_used == 1:
                score_value=5
                question_score = 5
            user.correct_answers += 1 

            user.score+=score_value
            user.correct_answers+=1
            game_session.session_score+=score_value

        else:
            user.score(max(0, user.score-5))
            user.incorrect_answers+=1
            game_session.session_score=max(0,game_session.session_score-5)
            question_score=-5

        # game_session.current_question += 1

        if game_session.current_question==10:
            game_session.is_completed = True
            game_session.completed_at = datetime.utcnow()

        session.commit()

        return {
            "user_score":user.score,
            "game_session": game_session.session_score
        }

    # @classmethod
    # async def calculate_user_score(cls, user_id, is_correct, no_of_hints_used):
    #     user = session.query(User).filter_by(id=user_id).first()
    #     if not user:
    #         return json({"error": "User not found"}, status=404)

    #     question_score = 0

    #     if is_correct:
    #         if no_of_hints_used == 0:
    #             user.score += 10  # Full score for first attempt
    #             question_score = 10
    #         elif no_of_hints_used == 1:
    #             user.score += 5   # Partial score if 2 clues were used
    #             question_score = 5
    #         user.correct_answers += 1 
    #     else:
    #         user.score = max(0, user.score - 5)  # Deduct 5 but ensure score is non-negative
    #         user.incorrect_answers += 1
    #         question_score = -5

    #     session.commit()

    #     return {
    #         "question_score": question_score,
    #         "user_score": user.score,
    #         "correct_answers": user.correct_answers,
    #         "incorrect_answers": user.incorrect_answers
    #     }
