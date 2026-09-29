from .gemini_client import generate_text
from .config import FAST_MODEL


def generate_nutrition_tip_with_flash(goal):

    fallback_tips = {

        "muscle gain":
            "Include a protein-rich food in each meal, stay hydrated, and support training with adequate sleep and balanced carbohydrates.",

        "weight loss":
            "Prioritize vegetables, protein, whole foods, and water. Use sustainable portions rather than extreme restriction.",

        "general wellness":
            "Build meals around vegetables or fruit, a protein source, whole grains or other high-fiber foods, and adequate water.",

        "flexibility":
            "Stay hydrated and include a variety of whole foods while supporting recovery with adequate sleep.",

        "strength":
            "Include protein-rich foods, fiber-rich carbohydrates, vegetables, and enough water to support consistent training and recovery."
    }

    fallback = fallback_tips.get(
        goal.lower(),
        "Choose balanced meals, stay hydrated, include protein and fiber, and prioritize consistent recovery."
    )

    prompt = f"""
Give one concise, practical nutrition or recovery tip
for a person whose fitness goal is:

{goal}

Keep it under 80 words.

Avoid:
- Medical claims
- Extreme dieting
- Supplements as necessities
"""

    return generate_text(
        prompt,
        FAST_MODEL,
        fallback
    )