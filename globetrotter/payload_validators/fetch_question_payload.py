from pydantic import BaseModel, validator, conlist
from typing import List, Optional


class FetchQuestionPayload(BaseModel):
    destination_ids: conlist(int, min_items=0) 
    user_id: int
    game_session_id: int

    @validator("destination_ids")
    def validate_destination_ids(cls, v):
        if len(v)==0:
            return v
        if v and not all(isinstance(id, int) for id in v):
            raise ValueError("Each ID in the list must be an integer")
        return v
