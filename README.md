# 🎳 AI Bowling Coach

AI Bowling Coach is a **FastAPI web application** that simulates a 10-round bowling game and generates an **AI-powered explanation of the player's performance**.

After the game is completed, the application analyzes the results and produces a friendly explanation like a bowling coach using the **OpenAI API**.

This project demonstrates how to combine:

- FastAPI
- OpenAI API
- Docker containerization
- Web UI with Jinja2 templates
- Environment configuration with `.env`

---

# 🚀 Features

- 🎳 Play a **10-round bowling game**
- 🧠 AI-generated explanation of player performance
- ✅ Bowling rule validation
- ⚡ FastAPI backend
- 🎨 HTML interface using **Jinja2 templates**
- 🐳 Docker + Docker Compose deployment
- 🔐 Environment variable configuration
- 🧪 Basic unit testing for bowling logic

---

# 📷 Application Workflow

1️⃣ User enters bowling scores for each round  
2️⃣ Backend validates bowling rules  
3️⃣ Results are stored for 10 rounds  
4️⃣ Game summary is generated  
5️⃣ OpenAI produces a friendly explanation of the player's performance

---

# 📁 Project Structure

```
bowlingapp/
│
├── app/
│   ├── main.py           # FastAPI application
│   ├── bowling.py        # Bowling logic + AI explanation
│   │
│   ├── templates/        # HTML templates
│   │   └── index.html
│   │
│   └── static/           # CSS / images
│
├── test.py               # Unit tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .dockerignore
└── README.md
```

---

# 📥 Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/Brian286933/bowlingapp.git
```

Move into the project folder:

```bash
cd bowlingapp
```

---

# 🔑 Environment Setup

Create a `.env` file in the root directory.

Example:

```
OPENAI_API_KEY=your_openai_api_key
```

You can copy the template:

```bash
cp .env.example .env
```

---

# 🐳 Run With Docker (Recommended)

Build and start the application:

```bash
docker compose up --build
```

Open your browser:

```
http://localhost:8000
```

---

# 💻 Run Locally (Without Docker)

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Start FastAPI server

```bash
uvicorn app.main:app --reload
```

### 3️⃣ Open in browser

```
http://localhost:8000
```

---

# 🎮 How the Game Works

Each bowling game consists of **10 rounds**.

In each round:

- Player gets **two throws**
- Maximum pins = **10**

Possible outcomes:

| Result | Description |
|------|-------------|
| Strike | 10 pins knocked down on the first throw |
| Spare | Total pins = 10 after two throws |
| Normal | Less than 10 pins |

After **10 rounds**, the AI generates a performance explanation.

---

# 🧠 AI Explanation System

When the game finishes, the application:

1️⃣ Builds a summary of the game rounds  
2️⃣ Sends the summary to OpenAI  
3️⃣ Generates a friendly explanation  

Example output:

> "You started strong with a strike in round 1. Your mid-game consistency showed good control, and the spare in round 7 demonstrated strong recovery."

---

# 🧪 Running Tests

This project includes a simple **unit test file (`test.py`)** to verify the bowling logic.

The tests check:

- Strike detection
- Spare detection
- Normal round detection
- Input validation rules

Run the tests with:

```bash
python test.py
```

Expected output:

```
All tests passed successfully!
```

---

# ⚙️ Dependencies

Main dependencies:

```
fastapi
uvicorn[standard]
jinja2
python-multipart
python-dotenv
openai
```

Install using:

```bash
pip install -r requirements.txt
```

---

# 🐳 Docker Setup

The project includes:

- `Dockerfile`
- `docker-compose.yml`

Docker Compose starts the FastAPI server and exposes port **8000**.

Example service:

```
services:
  bowling-ai:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
```

---

# 🔒 Environment Files

`.env` contains secrets such as the OpenAI API key.

It is excluded from Git using `.gitignore`.

`.env.example` provides a template for new developers.

---

# 🧪 Possible Improvements

Future enhancements could include:

- Full bowling score calculation
- Player statistics dashboard
- Game history storage
- Authentication system
- Mobile responsive UI
- Deployment to cloud (AWS / GCP / Kubernetes)

---

# 🧑‍💻 Author

**Brian**

Project built as a demonstration of:

- FastAPI backend development
- AI integration with OpenAI
- Docker containerization
- Interactive web applications

---

# ⭐ If You Like This Project

Give it a ⭐ on GitHub!