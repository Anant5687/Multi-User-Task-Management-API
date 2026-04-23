from database import Base
from sqlalchemy import Column, String


class Priority:
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"


class Status:
    TODO = "todo"
    COMPLETED = "completed"
    INPROGRESS = "in-progress"
    REJECTED = "rejected"


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    priority = Column(String)
    project_id = Column(String)