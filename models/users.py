from database import Base
from sqlalchemy import Column, text, Integer, String, TIMESTAMP


class User(Base):
    __tablename__ = "users"

    id= Column(String, primary_key=True)
    email= Column(String, unique=True, nullable=False)
    password= Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
