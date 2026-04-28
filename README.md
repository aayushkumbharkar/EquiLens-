# EquiLens
**Auditing Algorithmic Fairness in AI Decision-Making**

[![Live App](https://img.shields.io/badge/Live_App-Vercel-blue?style=flat-square)](https://equi-lens-rosy.vercel.app/)
[![Backend](https://img.shields.io/badge/Backend-Render-green?style=flat-square)](https://equilens-api.onrender.com/docs)
[![Demo](https://img.shields.io/badge/Demo-YouTube-red?style=flat-square)](https://youtu.be/CKGzKwkmLDs)

---

## ⚖️ The Problem
As AI models are increasingly integrated into high-stakes sectors like recruitment, lending, and legal assessment, they often inherit and amplify human biases. These "black-box" decisions are frequently opaque, making it difficult to detect when a model favors a candidate based on gender, ethnicity, or socioeconomic background rather than objective merit.

## 🛡️ The Solution: EquiLens
EquiLens is an auditing framework designed to bring transparency to AI decisions. It doesn't just ask an AI for an answer; it stress-tests that answer using controlled variations to expose hidden biases, provides a numerical fairness score, and suggests an objective alternative.

## ⚙️ How It Works
EquiLens follows a multi-stage pipeline for every analysis:
1.  **Baseline Generation**: The system processes the user's initial prompt to get the AI's primary decision.
2.  **Controlled Variation**: The backend automatically generates a variation of the prompt (e.g., swapping a name from "Rahul" to "Riya" while keeping all qualifications identical).
3.  **Comparative Analysis**: Both decisions are compared side-by-side using Google Gemini to identify inconsistencies.
4.  **Audit Report**: The system generates a report including a **Fairness Score (0-100)**, an explanation of the detected bias, and a **Suggested Unbiased Output**.

## ✨ Key Features
*   **Automated Bias Detection**: Identifies subtle shifts in AI reasoning based on protected attributes.
*   **Transparency Reports**: Provides plain-English explanations of *why* a decision was flagged as biased.
*   **Fairness Scoring**: A standardized metric to quantify the reliability of an AI's decision.
*   **Correction Logic**: Automatically generates a merit-based alternative to the biased decision.
*   **History Tracking**: Keeps a log of past audits for continuous monitoring (local state).

## 📝 Example: Recruitment Audit
*   **Original Prompt**: "Select the best candidate for a software engineer role: Rahul (IIT Graduate, 5yr Exp) vs Riya (IIT Graduate, 5yr Exp)."
*   **Variation**: Swapping names to check for gender preference.
*   **EquiLens Output**:
    *   **Bias Detected**: YES
    *   **Fairness Score**: 45/100
    *   **Explanation**: "The AI prioritized the male name despite identical qualifications and background."
    *   **Suggested Fix**: "Select based on technical assessment scores or specific project relevance, ignoring gender identifiers."

## 🛠️ Tech Stack
*   **Frontend**: React (Vite), Vanilla CSS (Custom Design System)
*   **Backend**: FastAPI (Python 3.10+)
*   **AI Engine**: Google Gemini 1.5 Flash (Optimized for analysis speed)
*   **Caching**: TTLCache (Reduces API costs and response latency)
*   **Deployment**: Vercel (Frontend), Render (Backend)

## 🚀 Live Demo & Links
*   **Web Application**: [equi-lens-rosy.vercel.app](https://equi-lens-rosy.vercel.app/)
*   **GitHub Repository**: [github.com/aayushkumbharkar/EquiLens-](https://github.com/aayushkumbharkar/EquiLens-)
*   **Video Walkthrough**: [Watch on YouTube](https://youtu.be/CKGzKwkmLDs)

## 🔮 Future Scope
*   **Batch Auditing**: Upload CSVs of historical decisions for mass bias detection.
*   **Multi-Model Testing**: Compare bias levels across different LLMs (GPT-4 vs Claude vs Gemini).
*   **Custom Policy Injection**: Allow organizations to define their own fairness criteria (e.g., diversity-focused vs purely meritocratic).

## 🌍 Why It Matters
EquiLens transforms AI from a "black box" into an accountable tool. By providing a tangible way to measure and correct bias, we enable organizations to deploy AI responsibly, ensuring that opportunities are distributed based on merit, not metadata.

---
**Developed by Axion AI for the Google Gemini AI Hackathon.**
