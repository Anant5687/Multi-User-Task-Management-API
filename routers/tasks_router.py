from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models.projects import Project
from models.tasks_model import Tasks
from schemas.tasks_schemas import TaskCreate, TaskResponse

router = APIRouter(prefix="/tasks", tags=["TASKS"])


@router.post("/create", response_model=TaskResponse)
def create_task(data: TaskCreate, db:Session=Depends(get_db)):
    new_task = Tasks(**data.dict())
    project = db.query(Project).filter(Project.id == data.project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail=f"Project not found with {new_task.project_id}")
    
    all_tasks= db.query(Tasks).all()
    id = f"TSK-{len(all_tasks) + 1}"
    new_task.id = id
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get("/", response_model=list[TaskResponse])
def get_all_tasks(db:Session=Depends(get_db)):
    return db.query(Tasks).all()

@router.get("/${task_id}", response_model=TaskResponse)
def get_task_by_id(task_id:str, db:Session=Depends(get_db)):
    task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task not found with id {task_id}")
    
    return task


@router.put("/update/${task_id}", response_model=TaskResponse)
def update_task_by_id(task_id: str,data:TaskResponse, db:Session=Depends(get_db)):
    task = db.query(Tasks).filter(Tasks.id == task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task not found with id {task_id}")
    
    for key, value in data.dict().items():
        setattr(task, key, value)
    return task



@router.delete("/${task_id}", response_model=TaskResponse)
def delete_task_by_id(task_id:str, db:Session=Depends(get_db)):
    task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task not found with id {task_id}")
    
    db.delete(task)
    db.commit()
    return task