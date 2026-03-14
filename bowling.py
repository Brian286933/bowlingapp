from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

rounds_scores = []

def calculate_result(first_throw, second_throw):
    if first_throw == 10:
        return "Strike"
    elif first_throw + second_throw == 10:
        return "Spare"
    else:
        return "Normal"

def get_explanation():

    game_summary = "Bowling game summary:\n"

    for r in rounds_scores:
        round_num, first, second, result = r
        game_summary += f"Round {round_num}: {result} ({first},{second})\n"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"system","content":"Explain bowling results."},
            {"role":"user","content":game_summary}
        ],
        max_tokens=200
    )

    return response.choices[0].message.content

@app.route("/", methods=["GET","POST"])
def index():

    explanation = None
    result = None
    round_number = len(rounds_scores) + 1

    if request.method == "POST":

        first = int(request.form["first"])
        second = int(request.form["second"])

        result = calculate_result(first, second)

        rounds_scores.append((round_number, first, second, result))

        if round_number == 10:
            explanation = get_explanation()

    return render_template(
        "index.html",
        round=round_number,
        result=result,
        explanation=explanation,
        scores=rounds_scores
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)