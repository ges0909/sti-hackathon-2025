from typing import Optional

from pydantic import BaseModel, field_validator

from employee.schemas import Gender


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int
    gender: Gender | None = None

    @field_validator("gender", mode="before")
    @classmethod
    def validate_gender(cls, v: str | None) -> Optional[Gender]:
        if v is None:
            return None
        try:
            return Gender(v.lower())
        except ValueError as error:
            valid_options = [g.value for g in Gender]
            raise ValueError(
                f"Invalid gender '{v}'. Valid options: {', '.join(valid_options)}"
            ) from error


class UpdateUserRequest(BaseModel):
    last_name: str
    first_name: str | None = None
    email: str | None = None
    age: int | None = None
    gender: Gender | None = None

    @field_validator("gender", mode="before")
    @classmethod
    def validate_gender(cls, v: str | None) -> Optional[Gender]:
        if v is None:
            return None
        try:
            return Gender(v.lower())
        except ValueError as error:
            valid_options = [g.value for g in Gender]
            raise ValueError(
                f"Invalid gender '{v}'. Valid options: {', '.join(valid_options)}"
            ) from error
