from app import templates
from fastapi import APIRouter, Request, Response, Depends
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from typing import Optional


router = APIRouter()


@router.get(path="/", summary="Home page", tags=["Pages"])
async def home(request: Request):
    return templates.TemplateResponse("pages/home.html", {"request": request})
