import os
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------
# Load API Key
# -----------------------------

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------
# Calculate bowling result
# -----------------------------

def calculate_result(first_throw, second_throw):

    if first_throw == 10:
        return "Strike"

    elif first_throw + second_throw == 10:
        return "Spare"

    else:
        return "Normal"


# -----------------------------
# Validate input
# -----------------------------

def validate_throws(first_throw, second_throw):

    if first_throw < 0 or second_throw < 0:
        return False, "Pins cannot be negative."

    if first_throw > 10 or second_throw > 10:
        return False, "Pins must be between 0 and 10."

    if first_throw != 10 and first_throw + second_throw > 10:
        return False, "Total pins in a round cannot exceed 10."

    return True, ""


# -----------------------------
# Generate AI explanation
# -----------------------------

def get_explanation(rounds_scores):

    game_summary = (
        "In a bowling game there are 10 rounds. "
        "Each round has two chances to knock down 10 pins.\n\n"
    )

    detailed_rounds = "Round details:\n"

    for round_num, first_throw, second_throw, result in rounds_scores:

        detailed_rounds += f"Round {round_num}: {result}. "

        if result == "Strike":
            detailed_rounds += "All 10 pins were knocked down in the first throw.\n"

        elif result == "Spare":
            detailed_rounds += f"{first_throw} pins in first throw and {second_throw} pins in second throw.\n"

        else:
            detailed_rounds += f"{first_throw} pins then {second_throw} pins.\n"

    prompt = (
        game_summary
        + detailed_rounds
        + "\nExplain the player's bowling performance in a clear, friendly, and engaging way."
    )

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful bowling coach."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Error generating explanation: {str(e)}"