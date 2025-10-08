from sqlalchemy import Column, Integer, String, Text
from backend.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)
    image_url = Column(String(255))
    github_url = Column(String(255))
    demo_url = Column(String(255))
    tags = Column(String(255))
