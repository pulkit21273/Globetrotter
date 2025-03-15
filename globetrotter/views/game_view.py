from sanic import Blueprint
from sanic.response import json
from sqlalchemy.orm import sessionmaker
from database.db import engine
from models import Destination, Clue, Trivia, FunFact
from controllers import GameController
from sqlalchemy import func
from payload_validators import FetchQuestionPayload
from decorators import handle_exceptions


Session = sessionmaker(bind=engine)
session = Session()

game_bp = Blueprint('game_bp', url_prefix='/game')


@game_bp.route("/question", methods=["POST"])
@handle_exceptions
async def fetch_question(request):
    payload = FetchQuestionPayload(**request.json)
    already_done_destination_ids = payload.destination_ids

    destination = session.query(Destination).filter(Destination.id.notin_(already_done_destination_ids)).order_by(func.random()).first()

    if not destination:
        return json({"error": "No available destinations found"}, status=404)
    
    payload = await GameController.generate_fetch_question_payload(destination=destination)
    return json(payload)

