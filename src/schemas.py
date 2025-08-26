from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int | None = None


class UserDto(UserBase):
    id: int

    class Config:
        from_attributes = True
