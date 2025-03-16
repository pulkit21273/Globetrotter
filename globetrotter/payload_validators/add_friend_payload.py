from pydantic import BaseModel, validator, constr, ValidationError
from typing import Optional

class AddFriendPayload(BaseModel):
    user_id: int
    friend_username: constr(min_length=4, max_length=20)  # Limiting username length between 8 and 20 characters

    @validator('user_id')
    def validate_user_id(cls, v):
        if not v:
            raise ValueError("User ID can't be empty")
        if not isinstance(v, int):
            raise ValueError("User ID must be an integer")
        return v

    @validator('friend_username')
    def validate_friend_username(cls, v):
        if not v:
            raise ValueError("Friend username can't be empty")
        if not isinstance(v, str):
            raise ValueError("Friend username must be a string")
        return v
