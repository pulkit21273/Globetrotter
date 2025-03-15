from sanic import Blueprint, response
from sanic.response import json
from models import User
from controllers import UserController
from payload_validators import CreateUserPayload, GetUserPayload, AddFriendPayload
from decorators import handle_exceptions

user_bp = Blueprint('user_bp', url_prefix='/users')

@user_bp.middleware("response")
async def add_cors_headers(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

async def handle_options(request):
    return response.empty()


@user_bp.route("/create_user", methods=["POST", "OPTIONS"])
@handle_exceptions
async def create_user(request):
    if request.method == "OPTIONS":
        return await handle_options(request)

    payload = CreateUserPayload(**request.json)
    username = payload.username
    return await UserController.create_user_manager(username=username)


@user_bp.route("/get_user", methods=["GET", "OPTIONS"])
@handle_exceptions
async def get_user(request):
    if request.method == "OPTIONS":
        return await handle_options(request)

    payload = GetUserPayload(user_id=request.args.get("id"))
    user_id = payload.user_id
    return await UserController.get_user_manager(user_id)


@user_bp.route("/add_friend", methods=["POST", "OPTIONS"])
@handle_exceptions
async def add_friend(request):
    if request.method == "OPTIONS":
        return await handle_options(request)

    payload = AddFriendPayload(**request.json)
    user_id = payload.user_id
    friend_username = payload.friend_username
    return await UserController.add_friend_manager(user_id=user_id, friend_username=friend_username)
