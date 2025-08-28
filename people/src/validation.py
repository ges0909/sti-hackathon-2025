from pydantic import BaseModel, field_validator
from models import Gender


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int
    gender: str | None = None

    @field_validator('gender')
    def validate_gender(cls, v: str | None) -> Gender | None:
        if v is None:
            return None
        try:
            return Gender[v.upper()]
        except KeyError:
            valid_options = [g.value for g in Gender]
            raise ValueError(f"Invalid gender '{v}'. Valid options: {', '.join(valid_options)}")


class UpdateUserRequest(BaseModel):
    last_name: str
    first_name: str | None = None
    email: str | None = None
    age: int | None = None
    gender: str | None = None

    @field_validator('gender')
    def validate_gender(cls, v: str | None) -> Gender | None:
        if v is None:
            return None
        try:
            return Gender[v.upper()]
        except KeyError:
            valid_options = [g.value for g in Gender]
            raise ValueError(f"Invalid gender '{v}'. Valid options: {', '.join(valid_options)}")
