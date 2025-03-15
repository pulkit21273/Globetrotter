from sanic import Blueprint, response
from sanic.response import json
from models import User
from controllers import UserController
from payload_validators import CreateUserPayload, GetUserPayload, AddFriendPayload
from decorators import handle_exceptions

user_bp = Blueprint('user_bp', url_prefix='/users')

@user_bp.options("/create_user")
async def handle_options(request):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
    }
    return response.empty(headers=headers)


@user_bp.route('/create_user', methods=['POST'])
@handle_exceptions
async def create_user(request):
    payload = CreateUserPayload(**request.json)
    username = payload.username
    response = await UserController.create_user_manager(username=username)
    return response


@user_bp.route('/get_user', methods=['GET'])
@handle_exceptions
async def get_user(request):
    payload = GetUserPayload(user_id=request.args.get('id'))
    user_id = payload.user_id
    response = await UserController.get_user_manager(user_id)
    return response


@user_bp.route('/add_friend', methods=['POST'])
@handle_exceptions
async def add_friend(request):
    payload = AddFriendPayload(**request.json)
    user_id = payload.user_id
    friend_username = payload.friend_username
    response = await UserController.add_friend_manager(user_id=user_id, friend_username=friend_username)
    return response
    