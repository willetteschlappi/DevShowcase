from pydantic import BaseModel

class ProjectBase(BaseModel):
    title: str
    description: str
    image_url: str | None = None
    github_url: str | None = None
    demo_url: str | None = None
    tags: str | None = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True
