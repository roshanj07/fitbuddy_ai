from .gemini_client import generate_text
from .config import WORKOUT_MODEL


def fallback_workout(
    name,
    goal,
    intensity
):

    return f"""
FITBUDDY 7-DAY WORKOUT PLAN

Name: {name}
Goal: {goal}
Intensity: {intensity}

DAY 1 - FULL BODY

Warm-up:
5-10 minutes of easy walking and mobility.

Workout:
- Squats: 3 x 10
- Push-ups: 3 x 8-12
- Rows: 3 x 10
- Glute bridges: 3 x 12

Cooldown:
5 minutes of easy walking and stretching.


DAY 2 - CARDIO + CORE

Warm-up:
5 minutes.

Workout:
- Moderate cardio: 25 minutes
- Plank: 3 x 30 seconds
- Dead bug: 3 x 10 each side

Cooldown:
5-10 minutes stretching.


DAY 3 - LOWER BODY

Warm-up:
5-10 minutes.

Workout:
- Lunges: 3 x 10 each side
- Hip hinge: 3 x 10
- Calf raises: 3 x 15

Cooldown:
Gentle lower-body stretching.


DAY 4 - RECOVERY

- Easy walking: 20-30 minutes
- Mobility work
- Gentle stretching

Keep effort light.


DAY 5 - UPPER BODY

Warm-up:
5-10 minutes.

Workout:
- Push-ups: 3 x 8-12
- Rows: 3 x 10
- Shoulder press: 3 x 10
- Curls: 2 x 12

Cooldown:
Upper-body stretching.


DAY 6 - CARDIO + FULL BODY

Warm-up:
5 minutes.

Workout:
20-30 minutes cardio.

Then 2 rounds:
- Bodyweight squats
- Incline push-ups
- Rows

Cooldown:
5-10 minutes.


DAY 7 - REST / ACTIVE RECOVERY

- Easy walk
- Breathing exercises
- Gentle stretching


SAFETY

This is general wellness guidance.
Adjust difficulty to your experience.
Stop if you feel pain or feel unwell.
Seek professional guidance when appropriate.
"""


def generate_workout_gemini(
    name,
    age,
    weight,
    goal,
    intensity
):

    prompt = f"""
You are FitBuddy, a careful AI fitness-planning assistant.

Create a safe and practical personalized
7-day workout plan.

User information:

Name: {name}
Age: {age}
Weight: {weight} kg
Fitness Goal: {goal}
Workout Intensity: {intensity}

Requirements:

1. Return exactly 7 days.
2. Every day must have a clear focus.
3. Include warm-up.
4. Include the main workout.
5. Include exercises with sets/reps or duration.
6. Include rest intervals where appropriate.
7. Include cooldown or recovery.
8. Include at least one recovery/rest day.
9. Do not prescribe medication.
10. Do not recommend extreme dieting.
11. Avoid unsafe practices.
12. Mention that this is general wellness guidance.
13. Tell the user to adjust the plan for pain,
    injury or medical limitations.

Make the response easy to read.
"""

    fallback = fallback_workout(
        name,
        goal,
        intensity
    )

    return generate_text(
        prompt,
        WORKOUT_MODEL,
        fallback
    )