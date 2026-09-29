# FitBuddy - AI Fitness Plan Generator

FitBuddy is an AI-powered fitness planning web application.

The application allows a user to:

- Enter personal fitness information
- Select a fitness goal
- Select workout intensity
- Generate a personalized 7-day workout plan
- Generate a nutrition/recovery tip
- Submit feedback
- Generate an updated workout plan
- Store the original and updated plans
- View users from an admin dashboard

---

# Technology Stack

Frontend:

- HTML
- CSS
- Jinja2

Backend:

- Python
- FastAPI

Database:

- SQLite
- SQLAlchemy

AI:

- Google Gemini API

Testing:

- Pytest

---

# Project Structure

FitBuddy/

    app/

        __init__.py
        main.py
        config.py
        database.py
        schemas.py
        routes.py
        gemini_client.py
        gemini_generator.py
        gemini_flash_generator.py
        updated_plan.py

    templates/

        index.html
        result.html
        all_users.html

    static/

        css/
            style.css

    tests/

        test_app.py

    requirements.txt
    .env.example
    .gitignore
    README.md

---

# Step 1 - Install Python

Install Python 3.11 or newer.

Check:

python --version

---

# Step 2 - Open the Project

Open the FitBuddy folder in VS Code.

---

# Step 3 - Create Virtual Environment

Open VS Code Terminal.

Run:

python -m venv venv

---

# Step 4 - Activate Virtual Environment

Windows PowerShell:

venv\Scripts\Activate.ps1

If PowerShell does not allow it, use Command Prompt:

venv\Scripts\activate

---

# Step 5 - Install Dependencies

Run:

python -m pip install --upgrade pip

Then:

pip install -r requirements.txt

---

# Step 6 - Create .env

Copy:

.env.example

and rename the copy to:

.env

Your folder should contain:

.env

Open .env.

Add your Gemini API key:

GEMINI_API_KEY=your_actual_api_key

---

# Step 7 - Start the Application

Run:

uvicorn app.main:app --reload

You should see something similar to:

Uvicorn running on http://127.0.0.1:8000

---

# Step 8 - Open FitBuddy

Open your browser:

http://127.0.0.1:8000

---

# Step 9 - Test the Application

Example input:

User ID:

FB001

Name:

Roshan

Age:

22

Weight:

65

Goal:

Muscle Gain

Intensity:

Medium

Click:

Generate My Plan

FitBuddy will:

1. Save the user
2. Generate a workout plan
3. Generate a nutrition/recovery tip
4. Store the plan
5. Display the result

---

# Step 10 - Test AI Feedback

After the plan is generated, use:

Add more cardio on Day 2 and make Day 4 a full rest day.

Click:

Update Plan with AI

The application will generate a revised 7-day plan.

---

# Admin Dashboard

Open:

http://127.0.0.1:8000/view-all-users

The dashboard shows:

- User information
- Original workout plan
- Updated workout plan
- Latest feedback
- Delete button

---

# API Documentation

FastAPI automatically provides Swagger UI.

Open:

http://127.0.0.1:8000/docs

---

# Health Check

Open:

http://127.0.0.1:8000/health

Expected result:

{
    "status": "ok",
    "service": "FitBuddy"
}

---

# Users API

Open:

http://127.0.0.1:8000/api/users

This returns stored users and their plans.

---

# Run Tests

Open a terminal with the virtual environment activated.

Run:

pytest

---

# Database

SQLite is automatically created when the application starts.

The file will be:

fitbuddy.db

You do not need to manually create it.

---

# Gemini

Gemini is used for:

1. Workout plan generation
2. Nutrition/recovery tip generation
3. Workout plan revision based on feedback

The Gemini API key is read from:

.env

The models can be changed from:

GEMINI_WORKOUT_MODEL

GEMINI_FAST_MODEL

---

# AI Fallback

If:

GEMINI_API_KEY

is empty and:

AI_REQUIRED=false

the application uses a local fallback workout plan instead of crashing.

If you want Gemini to be mandatory, set:

AI_REQUIRED=true

---

# Important

FitBuddy is a general fitness-planning application.

AI-generated plans should not be treated as medical advice.

Users with injuries, medical conditions, or other health limitations should consult an appropriately qualified professional.