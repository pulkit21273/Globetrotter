from pydantic import BaseModel, validator, ValidationError
from typing import Optional

class GetUserPayload(BaseModel):
    user_id: Optional[int]  # This makes user_id optional

    @validator('user_id')
    def validate_id(cls, v):
        if v is None:
            raise ValueError("ID can't be empty or None")

        if v <= 0:
            raise ValueError("ID must be a positive integer")

        return v
