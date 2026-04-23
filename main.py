from fastapi import FastAPI
from routers import users, projects, tasks_router
from database import create_db

app = FastAPI()

# Create all database tables at startup
@app.on_event("startup")
def startup_event():
    create_db()

@app.get("/")
def health_check():
    return {"status": 200, "message": "Server running well"}

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks_router.router)