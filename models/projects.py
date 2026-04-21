from database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, text

class Project(Base):
    __tablename__ = "projects"
    
    id= Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
    description= Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))