from typing import Annotated

from fastapi import APIRouter, Form, Request
from jinja2_fragments.fastapi import Jinja2Blocks

from app.config import Settings

# from pydantic import NonNegativeFloat

settings = Settings()
templates = Jinja2Blocks(directory=settings.TEMPLATE_DIR)

router = APIRouter()


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@router.get("/about")
def about(request: Request):
    """About page - some background information about this app."""

    return templates.TemplateResponse("about.html", {"request": request})
