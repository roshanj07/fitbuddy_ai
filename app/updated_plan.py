from .gemini_client import generate_text
from .config import WORKOUT_MODEL


def update_workout_plan(
    original_plan,
    feedback,
    name,
    goal,
    intensity
):

    fallback = (
        original_plan
        + "\n\nUPDATED BY USER FEEDBACK:\n"
        + feedback
    )

    prompt = f"""
You are FitBuddy.

Revise the existing 7-day workout plan using
the user's feedback.

User:

Name: {name}
Goal: {goal}
Intensity: {intensity}

ORIGINAL PLAN:

{original_plan}


USER FEEDBACK:

{feedback}


Instructions:

1. Return the complete revised 7-day plan.
2. Do not return only the changes.
3. Preserve the 7-day structure.
4. Directly address the feedback.
5. Include warm-up.
6. Include main workout.
7. Include rest/recovery.
8. Include cooldown where appropriate.
9. Avoid unsafe practices.
10. Do not prescribe medication.
11. Do not recommend extreme dieting.
"""

    return generate_text(
        prompt,
        WORKOUT_MODEL,
        fallback
    )