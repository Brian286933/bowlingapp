from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.bowling import calculate_result, get_explanation, validate_throws

app = FastAPI(title="AI Bowling Coach")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

rounds_scores = []


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    explanation = None
    if len(rounds_scores) == 10:
        explanation = get_explanation(rounds_scores)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "rounds_scores": rounds_scores,
            "current_round": min(len(rounds_scores) + 1, 10),
            "message": "",
            "message_type": "",
            "explanation": explanation,
        },
    )


@app.post("/submit", response_class=HTMLResponse)
async def submit_round(
    request: Request,
    first_throw: int = Form(...),
    second_throw: int = Form(...),
):
    current_round = len(rounds_scores) + 1

    if len(rounds_scores) >= 10:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "rounds_scores": rounds_scores,
                "current_round": 10,
                "message": "Game already completed. Please restart to begin a new game.",
                "message_type": "error",
                "explanation": get_explanation(rounds_scores),
            },
        )

    is_valid, error_message = validate_throws(first_throw, second_throw)
    if not is_valid:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "rounds_scores": rounds_scores,
                "current_round": current_round,
                "message": error_message,
                "message_type": "error",
                "explanation": None,
            },
        )

    result = calculate_result(first_throw, second_throw)
    rounds_scores.append((current_round, first_throw, second_throw, result))

    explanation = None
    if len(rounds_scores) == 10:
        explanation = get_explanation(rounds_scores)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "rounds_scores": rounds_scores,
            "current_round": min(len(rounds_scores) + 1, 10),
            "message": f"Round {current_round}: {result}",
            "message_type": "success",
            "explanation": explanation,
        },
    )


@app.post("/restart")
async def restart_game():
    rounds_scores.clear()
    return RedirectResponse(url="/", status_code=303)