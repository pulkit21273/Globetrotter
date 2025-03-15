from sanic import Blueprint, response
from sanic.response import json
from sqlalchemy.orm import sessionmaker
from database.db import engine
from models import Destination, Clue, Trivia, FunFact, User
from controllers import GameController
from sqlalchemy import func
from payload_validators import FetchQuestionPayload, CheckCorrectAnswerPayload
from decorators import handle_exceptions

Session = sessionmaker(bind=engine)
session = Session()

game_bp = Blueprint("game_bp", url_prefix="/game")


@game_bp.middleware("response")
async def add_cors_headers(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"


async def handle_options(request):
    return response.empty()


@game_bp.route("/question", methods=["POST", "OPTIONS"])
@handle_exceptions
async def fetch_question(request):
    if request.method == "OPTIONS":
        return await handle_options(request)

    payload = FetchQuestionPayload(**request.json)
    already_done_destination_ids = payload.destination_ids

    destination = session.query(Destination).filter(
        Destination.id.notin_(already_done_destination_ids)
    ).order_by(func.random()).first()

    if not destination:
        return json({"error": "No available destinations found"}, status=404)

    payload = await GameController.generate_fetch_question_payload(destination=destination)
    return json(payload)


@game_bp.route("/correct_answer", methods=["POST", "OPTIONS"])
@handle_exceptions
async def check_correct_answer(request):
    if request.method == "OPTIONS":
        return await handle_options(request)

    payload = CheckCorrectAnswerPayload(**request.json)
    user_id = payload.user_id
    clue_id = payload.clue_id
    selected_option_id = payload.selected_option_id
    no_of_hints_used = payload.no_of_hints_used

    clue = session.query(Clue).filter_by(id=clue_id).first()
    if not clue:
        return json({"error": "Invalid clue ID"}, status=400)

    is_correct = clue.destination_id == selected_option_id
    score_update = await GameController.calculate_user_score(
        user_id=user_id, is_correct=is_correct, no_of_hints_used=no_of_hints_used
    )

    fun_fact = session.query(FunFact).filter_by(destination_id=clue.destination_id).first()

    return json({
        "selected_option_id": selected_option_id,
        "correct_option_id": clue.destination_id,
        "correct": is_correct,
        "fun_fact": fun_fact.text if fun_fact else None,
        **score_update
    })


@game_bp.route("/hint", methods=["GET", "OPTIONS"])
@handle_exceptions
async def get_hint(request):
    if request.method == "OPTIONS":
        return await handle_options(request)

    clue_id = request.args.get("clue_id")
    clue = session.query(Clue).filter_by(id=clue_id).first()
    if not clue:
        return json({"error": "Invalid clue ID"}, status=400)

    trivia = session.query(Trivia).filter_by(destination_id=clue.destination_id).first()
    return json({"trivia": trivia.text if trivia else None})


@game_bp.route("/score", methods=["GET", "OPTIONS"])
@handle_exceptions
async def get_user_score(request):
    if request.method == "OPTIONS":
        return await handle_options(request)

    user_id = request.args.get("user_id")
    user = session.query(User).filter_by(id=user_id).first()

    return json({
        "correct_answers": user.correct_answers if user else 0,
        "incorrect_answers": user.incorrect_answers if user else 0,
        "total_score": user.score if user else 0,
    })
