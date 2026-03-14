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



## Installation

### 1. Clone the repository
git clone https://github.com/yourusername/ai-medical-symptom-checker.git
cd ai-medical-symptom-checker
### 2. Install dependencies
pip install -r requirements.txt
### 3. Set OpenRouter API Key
setx OPENROUTER_API_KEY "your_api_key_here"
### 4. Run the backend
uvicorn backend.main:app --reload
### 5. Open the frontend
Open `frontend/index.html` in your browser.

---
## Future Improvements

- Improve disease prediction accuracy
- Add more symptoms and diseases
- Use ML models for better predictions
- Add user-friendly UI improvements
- Deploy as a full web application

---
## Project Overview

The AI Medical Symptom Checker is a web-based application that predicts possible diseases based on symptoms entered by the user. The system analyzes the input symptoms, compares them with a medical symptom dataset, and identifies the most likely diseases.

The application returns the top possible diseases, along with their descriptions and recommended precautions to help users understand the condition better. Additionally, the system integrates a Large Language Model (Llama 3 via OpenRouter) to generate simple explanations of the predicted diseases for easier understanding.

The project uses a FastAPI backend to process symptom inputs and perform disease prediction, while a simple HTML/CSS/JavaScript frontend provides an interactive interface for users to enter symptoms and view results.

Overall, the system demonstrates how machine learning datasets and AI models can be combined with web technologies to build an intelligent health assistance tool.






## Disclaimer

This application is intended for **educational and demonstration purposes only**.  
It should not be used for real medical diagnosis.





























































<img width="318" height="901" alt="Image" src="https://github.com/user-attachments/assets/a5af1611-ef23-479f-a7e1-0da5c3d35f24" />

<img width="331" height="872" alt="Image" src="https://github.com/user-attachments/assets/47fe337d-b41d-4579-87ec-f575cc137b97" />
