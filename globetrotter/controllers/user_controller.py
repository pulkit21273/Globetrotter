from models import User
from database.db import engine
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.orm import sessionmaker
from sanic.response import json

Session = sessionmaker(bind=engine)
session = Session()

class UserController:

    @classmethod
    async def create_user_manager(cls, username):
        """Create a user if username is unique."""
        if username:
            existing_user = session.query(User).filter_by(username=username).first()

            if existing_user:
                return json({
                    "message": "User already exists",
                    "id": existing_user.id,
                    "username": existing_user.username
                })

            new_user = User(username=username)
            session.add(new_user)
            session.commit()

            return json({
                "id": new_user.id,
                "username": new_user.username
            })
        else:
            return json({"error": "Username is required"}, status=400)


    @classmethod
    async def get_user_manager(cls, user_id):
        """Retrieve a user based on user_id."""
        if user_id:
            user = session.query(User).filter_by(id=user_id).first()

            if user:
                return json({
                    "id": user.id,
                    "username": user.username,
                    "correct_answers": user.correct_answers,
                    "incorrect_answers": user.incorrect_answers,
                    "score": user.score,
                    "friends": user.friends
                })

            return json({"error": "User not found"}, status=404)

        return json({"error": "User ID is required"}, status=400)


    @classmethod
    async def add_friend_manager(cls, user_id, friend_username):
        """Add a friend to the user, creating the friend if necessary."""

        if user_id and friend_username:
            user = session.query(User).filter_by(id=user_id).first()

            if not user:
                return json({"error": "User not found"}, status=404)

            friend = session.query(User).filter_by(username=friend_username).first()

            if not friend:
                create_response = await cls.create_user_manager(friend_username)

                if create_response.status != 200:
                    return create_response

                friend = session.query(User).filter_by(username=friend_username).first()

            if friend.id in user.friends:
                return json({"message": "You are already friends"}, status=400)
            
            user.friends.append(friend.id)
            friend.friends.append(user.id)

            flag_modified(user, 'friends')
            flag_modified(friend, 'friends')
            session.commit()

            return json({
                "message": "Friend added successfully",
                "user_id": user.id,
                "friend_username": friend.username,
                "friends": user.friends
            })

        return json({"error": "User ID and friend username are required"}, status=400)
