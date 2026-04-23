from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.users import User
from schemas.users import UserResponse, UserCreate
from core.auth_helpers import verify_password

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=UserResponse)
def login(data:UserCreate, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User with this email does not exist"
        )
    
    if not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect password"
        )
    return user


