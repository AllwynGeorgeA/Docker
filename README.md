# 🤖 Basic GenAI App

A simple Generative AI application built using **Streamlit, FastAPI, OpenAI, and Docker**.

The project demonstrates how a frontend communicates with a backend API, which then sends the user's prompt to an OpenAI model and returns the AI response.

## 🚀 Tech Stack

* **Streamlit** – Frontend UI
* **FastAPI** – Backend REST API
* **OpenAI API** – Generative AI
* **Docker** – Containerization
* **Docker Compose** – Run all services together
* **Nginx** – Single entry point for frontend and backend

## 📁 Project Structure

```text
basic-genai-app/
│
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── backend/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── .env
├── docker-compose.yml
├── nginx.conf
└── .gitignore
```

## 🔄 Application Flow

```text
User
  ↓
Streamlit Frontend
  ↓
Nginx
  ↓
FastAPI Backend
  ↓
OpenAI API
  ↓
AI Response
  ↓
Streamlit
```

## 🐳 Docker Architecture

```text
                 Docker Compose
                       │
             ┌─────────┴─────────┐
             │                   │
        Frontend              Backend
        Streamlit             FastAPI
          :8501                :8000
             │                   │
             └─────────┬─────────┘
                       │
                     Nginx
                       │
                       ▼
                  Single URL
                localhost:8080
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/AllwynGeorgeA/Docker.git
```

Go into the project folder:

```bash
cd Docker
```

Then go into the application folder:

```bash
cd basic-genai-app
```

### 2. Add OpenAI API Key

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

**Never commit your `.env` file or API key to GitHub.**

### 3. Build and Run

Run the complete application with one command:

```bash
docker compose up --build
```

## 🌐 Access the Application

### Streamlit Application

```text
http://localhost:8080
```

### FastAPI Swagger Documentation

```text
http://localhost:8080/api/docs
```

## 🛑 Stop the Application

```bash
docker compose down
```

## 🔄 Run in Background

```bash
docker compose up -d --build
```

## 📋 View Containers

```bash
docker compose ps
```

## 📜 View Logs

```bash
docker compose logs
```

Backend logs:

```bash
docker compose logs backend
```

Frontend logs:

```bash
docker compose logs frontend
```

## 🧠 Example Prompt

Enter a prompt such as:

```text
Explain Generative AI in simple words.
```

The application sends the request through:

```text
Streamlit
   ↓
FastAPI
   ↓
OpenAI
   ↓
FastAPI
   ↓
Streamlit
```

## 🎯 Learning Goals

This project helps understand:

* Building a basic GenAI application
* Streamlit frontend development
* FastAPI REST API development
* Connecting an application to OpenAI
* Frontend-to-backend communication
* Docker containers
* Docker Compose
* Nginx reverse proxy
* Running multiple services together

## 🔐 Security

Keep your API key in `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Make sure `.env` is included in `.gitignore`:

```text
.env
__pycache__/
*.pyc
.venv/
venv/
```

## 👨‍💻 Author

**Allwyn George**

GitHub: [AllwynGeorgeA](https://github.com/AllwynGeorgeA)
