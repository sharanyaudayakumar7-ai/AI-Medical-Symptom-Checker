# AI-Medical-Symptom-Checker
AI Medical Symptom Checker

An AI-powered web application that predicts possible diseases based on user symptoms and provides explanations and precautions.
The system uses a symptom dataset to identify the most likely diseases and integrates an LLM (Llama 3 via OpenRouter) to generate easy-to-understand medical explanations.

⚠️ This project is not a substitute for professional medical advice.

---

## Features

- Symptom-based disease prediction
- Top 3 possible diseases with descriptions
- AI-generated medical explanations
- Precaution recommendations
- Simple and interactive web interface
- FastAPI backend API
- LLM integration using OpenRouter (Llama 3)

---

## Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Python
- FastAPI

**AI / ML**
- Symptom dataset from Kaggle
- Llama 3 (via OpenRouter API)

---


---

## How It Works

1. The user enters symptoms separated by commas.
2. The backend compares the symptoms with a medical dataset.
3. The system calculates a match score for each disease.
4. The top 3 most relevant diseases are returned.
5. The system displays:
   - disease description
   - precautions
   - optional AI explanation.

---

## Example Input































































<img width="318" height="901" alt="Image" src="https://github.com/user-attachments/assets/a5af1611-ef23-479f-a7e1-0da5c3d35f24" />

<img width="331" height="872" alt="Image" src="https://github.com/user-attachments/assets/47fe337d-b41d-4579-87ec-f575cc137b97" />
