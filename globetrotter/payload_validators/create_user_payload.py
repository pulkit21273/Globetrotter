from pydantic import BaseModel, validator, ValidationError, constr
from typing import Optional

class CreateUserPayload(BaseModel):
    username: constr(min_length=4, max_length=20)  # Limiting username length between 8 and 20 characters

    @validator('username')
    def validate_username(cls, v):
        if not isinstance(v, str):
            raise ValueError("Username must be a string")
        if len(v) == 0:
            raise ValueError("Username cannot be empty")
        return v
