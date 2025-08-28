from enum import Enum
from typing import Annotated
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class UserBase(BaseModel):
    first_name: Annotated[str, Field(min_length=1, max_length=255)]
    last_name: Annotated[str, Field(min_length=1, max_length=255)]
    email: EmailStr
    age: Annotated[int, Field(ge=0, le=150)] | None = None
    gender: Gender | None = None


class UserDto(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class AddressBase(BaseModel):
    street: Annotated[str, Field(min_length=1, max_length=255)]
    city: Annotated[str, Field(min_length=1, max_length=100)]
    postal_code: Annotated[str, Field(min_length=1, max_length=20)]
    country: Annotated[str, Field(min_length=1, max_length=100)]
    user_id: int


class AddressDto(AddressBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
