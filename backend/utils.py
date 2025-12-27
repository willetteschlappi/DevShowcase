














import re
from fastapi import HTTPException


def generate_slug(title: str) -> str:
    """
    Генерирует читаемый slug из названия проекта.
    Пример: "AI Image Synthesizer" -> "ai-image-synthesizer"
    """
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return slug.strip("-")


def tags_to_list(tags: str | None) -> list[str]:
    """
    Преобразует строку тегов в список.
    Пример: "python,fastapi,ai" -> ["python", "fastapi", "ai"]
    """
    if not tags:
        return []
    return [t.strip().lower() for t in tags.split(",") if t.strip()]


def list_to_tags(tags_list: list[str] | None) -> str:
    """
    Преобразует список тегов в строку.
    Пример: ["python", "fastapi"] -> "python,fastapi"
    """
    if not tags_list:
        return ""
    return ",".join(sorted(set(tags_list)))


def raise_not_found(entity: str, entity_id: int):
    """
    Универсальный обработчик 404 ошибок.
    """
    raise HTTPException(status_code=404, detail=f"{entity.capitalize()} with ID {entity_id} not found.")
