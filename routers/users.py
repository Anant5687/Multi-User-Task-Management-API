from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.users import User
from schemas.users import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/create", response_model=UserResponse)
def create_user(data:UserCreate, db:Session=Depends(get_db)):
    existing_user = db.query(User).filter(User.email == data.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists with this email"
        )
    new_user = User(**data.dict())
    new_user.id = f"USR-{len(db.query(User).all()) + 1}"
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user