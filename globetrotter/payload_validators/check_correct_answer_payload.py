from pydantic import BaseModel, validator, Field


class CheckCorrectAnswerPayload(BaseModel):
    user_id: int
    clue_id: int
    selected_option_id: int
    no_of_hints_used: int = Field(default=0)

    @validator("clue_id", "selected_option_id")
    def validate_non_negative(cls, v, field):
        if not isinstance(v, int):
            raise ValueError(f"{field.name} must be an integer")
        if v < 0:
            raise ValueError(f"{field.name} must be a non-negative integer")
        return v
