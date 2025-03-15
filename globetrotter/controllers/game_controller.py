from database.db import engine
from sqlalchemy.orm import sessionmaker
from sanic.response import json
from models import Destination, Clue, Trivia, FunFact
import random
from sqlalchemy import func


Session = sessionmaker(bind=engine)
session = Session()

class GameController:

    @classmethod
    async def generate_fetch_question_payload(cls, destination):

        clues = session.query(Clue).filter_by(destination_id=destination.id).all()
        clues_list = [{"id": clue.id, "text": clue.text} for clue in clues]

        trivia = session.query(Trivia).filter_by(destination_id=destination.id).all()
        trivia_list = [t.text for t in trivia]

        fun_facts = session.query(FunFact).filter_by(destination_id=destination.id).all()
        fun_facts_list = [f.text for f in fun_facts]

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
            "trivia": trivia_list,
            "funfact": fun_facts_list,
            "options": options_list
        }
