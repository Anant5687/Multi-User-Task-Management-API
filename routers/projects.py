from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models.projects import Project
from schemas.projects import ProjectCreate, ProjectResponse

router = APIRouter(prefix='/projects', tags=["PROJECTS"])

@router.get('/', response_model=list[ProjectResponse])
def get_all_projects(db:Session=Depends(get_db)):
    return db.query(Project).all()

@router.post("/create", response_model=ProjectResponse)
def create_project(data: ProjectCreate, db:Session=Depends(get_db)):
    all_projects = db.query(Project).all()
    new_project = Project(**data.dict())

    new_project.id = f"PRJ-{len(all_projects) + 1}"
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


@router.delete("/delete/{project_id}")
def delete_project(project_id:str, db:Session=Depends(get_db)):
    all_projects = db.query(Project).all()

    for project in all_projects:
        
        if project.id == project_id:
            db.delete(project)
            db.commit()
            return {"status": 200, "message": "Project deleted successfully", "project": project}
        
    raise HTTPException(status_code=404, detail=f"No project found with {project_id}")

@router.put("/project/{project_id}")
def update_project(data: ProjectCreate, project_id: str, db:Session=Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail=f"Project not found with {project_id}")

    for key, value in data.dict().items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)

    return {"status": 200, "data":project}
