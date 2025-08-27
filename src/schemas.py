from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=255)
    last_name: str = Field(min_length=1, max_length=255)
    email: EmailStr
    age: int | None = Field(default=None, ge=0, le=150)


class UserDto(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
