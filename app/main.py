from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from app.routers import root

app = FastAPI()
app.include_router(root.router)
