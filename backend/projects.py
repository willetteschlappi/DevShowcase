from backend.utils import generate_slug, tags_to_list, raise_not_found

@router.post("/", response_model=schemas.Project)
async def create_project(project: schemas.ProjectCreate, db: AsyncSession = Depends(get_db)):
    new_project = models.Project(**project.dict())
    new_project.slug = generate_slug(project.title)
    db.add(new_project)
    await db.commit()
    await db.refresh(new_project)
    return new_project
