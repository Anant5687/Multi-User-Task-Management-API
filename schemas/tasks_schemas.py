from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    status: str
    priority: str
    project_id: str


class TaskResponse(BaseModel):
    id: str
    title: str
    description: str
    status: str
    priority: str
    project_id: str

    class Config:
        from_attributes = True