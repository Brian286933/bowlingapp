# 🎳 AI Bowling Coach

AI Bowling Coach is a FastAPI web application that simulates a 10-round bowling game and generates an AI-powered explanation of the player’s performance.

After the game is completed, the system analyzes the rounds and produces a friendly explanation like a bowling coach using the OpenAI API.

---

# 🚀 Features

- 🎳 Play a **10-round bowling game**
- ✅ Validates bowling rules
- 🧠 AI explanation of your performance
- ⚡ Built with **FastAPI**
- 🎨 HTML interface with **Jinja2**
- 🐳 Docker + Docker Compose support
- 🔐 Environment variable configuration

---

# 📁 Project Structure

```
bowling/
│
├── app/
│   ├── bowling.py        # Bowling logic + AI explanation
│   ├── main.py           # FastAPI application
│   ├── static/           # CSS and images
│   └── templates/        # HTML templates
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .env.example
└── README.md
```

---

# 🧠 How the AI Works

After the player completes **10 rounds**, the system generates a summary of the game and sends it to OpenAI to generate a friendly explanation of the performance.

Example output:

> "You started strong with a strike in round 1. Your mid-game consistency showed solid control, and the spare in round 7 demonstrated good recovery."

---

# ⚙️ Requirements

- Python 3.11+
- Docker
- Docker Compose
- OpenAI API Key

Python dependencies:

```
fastapi
uvicorn[standard]
jinja2
python-multipart
python-dotenv
openai
```

---

# 🔑 Environment Setup

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key
```

This key is used to generate the AI explanation.

---

# 🐳 Run With Docker (Recommended)

Build and start the project:

```
docker compose up --build
```

The app will start at:

```
http://localhost:8000
```

---

# 💻 Run Locally (Without Docker)

### Install dependencies

```
pip install -r requirements.txt
```

### Start the FastAPI server

```
uvicorn app.main:app --reload
```

### Open in browser

```
http://localhost:8000
```

---

# 🎮 How to Play

1. Enter the **first throw** and **second throw** pins.
2. Submit the round.
3. Continue until **10 rounds are completed**.
4. The AI coach will generate a performance explanation.

---

# 🧾 Bowling Rules Implemented

- Strike → 10 pins in the first throw
- Spare → Total pins = 10 in two throws
- Normal → Less than 10 pins

Validation rules:

- Pins must be between **0 and 10**
- Total pins in a round cannot exceed **10**
- Negative values are not allowed

---

# 🔒 Environment Files

`.env` contains secrets and is ignored by git.

`.env.example` provides a template for developers.

---

# 🧪 Possible Improvements

- Bowling score calculation system
- Player statistics dashboard
- AI performance tips
- Game history storage
- Mobile responsive UI

---

# 👨‍💻 Author

AI Bowling Coach was built as a demonstration project combining:

- FastAPI backend
- OpenAI integration
- Docker containerization
- Web UI with Jinja2