from pydantic import BaseModel

from schemas.users import UserResponse

class LoginResponse(UserResponse):
    access_token: str
    token_type: str = "Bearer"

    class Config:
        from_attributes = True