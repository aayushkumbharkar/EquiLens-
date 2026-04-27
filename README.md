# EquiLens

EquiLens is an AI Bias Detection platform. It allows users to test the fairness of AI-generated decisions by automatically swapping sensitive attributes (like names or genders) in prompts and analyzing if the AI changes its decision.

## Features

- **Automated Bias Testing**: Submits a prompt, generates a controlled variation, and compares the AI's decisions.
- **Fairness Scoring**: Calculates a percentage-based fairness score.
- **Explainability**: Explains why a prompt was flagged as biased and provides an unbiased alternative.
- **History Tracking**: Persists all historical analysis runs in a database.
- **Clean Architecture**: Backend is built using Uncle Bob's Clean Architecture for high modularity.

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy (SQLite/PostgreSQL), Google Gemini API, CacheTools
- **Frontend**: React (Vite), Axios, Modular CSS
- **Architecture**: Clean Architecture (Domain, Use Cases, Infrastructure)

---

## Local Setup

### 1. Backend

Navigate to the backend directory:
```bash
cd backend
```

Create a virtual environment and install dependencies:
```bash
python -m venv venv
# Windows
.\venv\Scripts\Activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Set up your environment variables:
Copy `.env.example` to `.env` and add your **Gemini API Key**.
```bash
cp .env.example .env
```

Run the FastAPI server:
```bash
uvicorn app.main:app --reload
```
The backend will start at `http://localhost:8000`.

### 2. Frontend

Navigate to the frontend directory:
```bash
cd frontend
```

Install Node dependencies:
```bash
npm install
```

Run the Vite development server:
```bash
npm run dev
```
The frontend will start at `http://localhost:5173`.

---

## Deployment Guide

### Backend (Render)
1. Push the repository to GitHub.
2. Create a new Web Service on [Render](https://render.com/).
3. Connect your GitHub repo.
4. Set the Root Directory to `backend`.
5. Set Build Command: `pip install -r requirements.txt`
6. Set Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
7. Add Environment Variables:
   - `GEMINI_API_KEY`: Your Gemini Key
   - `PYTHON_VERSION`: `3.10.0` (or higher)

### Frontend (Vercel)
1. Go to [Vercel](https://vercel.com/) and import the GitHub repo.
2. Set the Framework Preset to `Vite`.
3. Set the Root Directory to `frontend`.
4. Add Environment Variable:
   - `VITE_API_URL`: The URL of your deployed Render backend (e.g., `https://your-backend.onrender.com/api/v1`)
5. Click Deploy!
