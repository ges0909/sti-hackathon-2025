from typing import Annotated
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    first_name: Annotated[str, Field(min_length=1, max_length=255)]
    last_name: Annotated[str, Field(min_length=1, max_length=255)]
    email: EmailStr
    age: Annotated[int, Field(ge=0, le=150)] | None = None
    gender: str | None = None


class UserDto(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
