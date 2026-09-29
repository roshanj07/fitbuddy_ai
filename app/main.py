from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import router

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="FitBuddy AI")

# Un structure ku etha maadiri correct path
app.mount("/static", StaticFiles(directory=BASE_DIR / "app" / "static"), name="static")

app.include_router(router)
