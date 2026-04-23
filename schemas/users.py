from pydantic import EmailStr, BaseModel


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    email: EmailStr

    class Config:
        from_attributes = True