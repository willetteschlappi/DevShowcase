from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import projects
from backend.database import init_db

app = FastAPI(title="DevShowcase API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])

@app.get("/")
async def root():
    return {"message": "Welcome to DevShowcase API"}
