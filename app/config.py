import os
from dotenv import load_dotenv


load_dotenv()


APP_NAME = os.getenv(
    "APP_NAME",
    "FitBuddy"
)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./fitbuddy.db"
)

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    ""
)

WORKOUT_MODEL = os.getenv(
    "GEMINI_WORKOUT_MODEL",
    "gemini-3.1-pro-preview"
)

FAST_MODEL = os.getenv(
    "GEMINI_FAST_MODEL",
    "gemini-3.8-flash"
)

AI_REQUIRED = os.getenv(
    "AI_REQUIRED",
    "false"
).lower() == "true"