from pydantic import BaseModel, EmailStr, validator, constr
from typing import Optional


class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: EmailStr
    hashed_password: str
    role: str


class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=8)
    password2: str

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError("passwords don't match")
        return v
