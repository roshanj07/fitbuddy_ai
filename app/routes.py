from pathlib import Path
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from .schemas import UserInput
from .database import save_user, save_plan, get_all_users, get_user_with_plan, update_plan, delete_user
from .gemini_generator import generate_workout_gemini
from .gemini_flash_generator import generate_nutrition_tip_with_flash
from .updated_plan import update_workout_plan

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).resolve().parent.parent / "templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request})

@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout(request: Request, user_id: str = Form(...), name: str = Form(...), age: int = Form(...), weight: float = Form(...), goal: str = Form(...), intensity: str = Form(...)):
    try:
        user = UserInput(user_id=user_id, name=name, age=age, weight=weight, goal=goal, intensity=intensity)
    except Exception as exc:
        return templates.TemplateResponse(request, "index.html", {"request": request, "error": str(exc)})
    workout_plan = generate_workout_gemini(user.name, user.age, user.weight, user.goal, user.intensity)
    nutrition_tip = generate_nutrition_tip_with_flash(user.goal)
    save_user(user.model_dump())
    save_plan(user.user_id, workout_plan, nutrition_tip)
    return templates.TemplateResponse(request, "result.html", {"request": request, "user": user, "workout_plan": workout_plan, "nutrition_tip": nutrition_tip, "message": None, "error": None})

@router.post("/submit-feedback", response_class=HTMLResponse)
def submit_feedback(request: Request, user_id: str = Form(...), feedback: str = Form(...)):
    user, stored_plan = get_user_with_plan(user_id)
    if not user or not stored_plan:
        return templates.TemplateResponse(request, "result.html", {"request": request, "error": "User ID not found.", "user": None})
    if not feedback.strip():
        return templates.TemplateResponse(request, "result.html", {"request": request, "error": "Please enter feedback.", "user": user})
    revised_plan = update_workout_plan(stored_plan.original_plan, feedback.strip(), user.name, user.goal, user.intensity)
    nutrition_tip = generate_nutrition_tip_with_flash(user.goal)
    update_plan(user_id, revised_plan, feedback.strip(), nutrition_tip)
    return templates.TemplateResponse(request, "result.html", {"request": request, "user": user, "workout_plan": revised_plan, "nutrition_tip": nutrition_tip, "message": "Your plan has been updated successfully.", "error": None})

@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request):
    users = get_all_users()
    rows = []
    for user in users:
        _, plan = get_user_with_plan(user.user_id)
        rows.append((user, plan))
    return templates.TemplateResponse(request, "all_users.html", {"request": request, "rows": rows})

@router.post("/delete-user/{user_id}")
def remove_user(user_id: str):
    delete_user(user_id)
    return RedirectResponse("/view-all-users", status_code=303)

@router.get("/api/users")
def api_users():
    rows = []
    for user in get_all_users():
        _, plan = get_user_with_plan(user.user_id)
        rows.append({"user_id": user.user_id, "name": user.name, "age": user.age, "weight": user.weight, "goal": user.goal, "intensity": user.intensity, "original_plan": plan.original_plan if plan else None, "updated_plan": plan.updated_plan if plan else None, "feedback": plan.feedback if plan else None})
    return rows