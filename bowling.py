from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

rounds_scores = []


def calculate_result(first_throw, second_throw):

    if first_throw == 10:
        return "Strike"
    elif first_throw + second_throw == 10:
        return "Spare"
    else:
        return "Open"


def calculate_total():
    total = 0
    for r in rounds_scores:
        total += r[1] + r[2]
    return total


def get_explanation():

    game_summary = ""

    for r in rounds_scores:
        round_num, first, second, result = r
        game_summary += f"Round {round_num}: {result} ({first},{second})\n"

    prompt = f"""
You are a bowling sports commentator.

Analyze this bowling game and describe the player's performance.

{game_summary}

Respond like an exciting sports narrator.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI analysis error: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def index():

    explanation = None
    result = None

    round_number = len(rounds_scores) + 1

    if request.method == "POST":

        try:
            first = int(request.form.get("first", 0))
            second = int(request.form.get("second", 0))
        except:
            first = 0
            second = 0

        result = calculate_result(first, second)

        rounds_scores.append((round_number, first, second, result))

        if round_number == 10:
            explanation = get_explanation()

    return render_template(
        "index.html",
        round=round_number,
        result=result,
        scores=rounds_scores,
        total=calculate_total(),
        explanation=explanation
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)