from fastapi import FastAPI
from routers import users

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": 200, "message": "Server running well"}

app.include_router(users.router)