from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import requests

app = FastAPI()

# allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load datasets
dataset = pd.read_csv("backend/dataset.csv")
dataset.fillna("", inplace=True)

description_df = pd.read_csv("backend/symptom_Description.csv")
precaution_df = pd.read_csv("backend/symptom_precaution.csv")

OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"


@app.get("/")
def home():
    return {"message": "AI Medical Symptom Checker API running"}


# description
def get_disease_description(disease):

    for _, row in description_df.iterrows():

        if row["Disease"].lower() == disease.lower():

            return row["Description"]

    return "No description available."


# precautions
def get_precautions(disease):

    for _, row in precaution_df.iterrows():

        if row["Disease"].lower() == disease.lower():

            return list(row[1:].dropna().values)

    return []


# optional LLM explanation
def get_llama_explanation(disease):

    prompt = f"""
Explain the disease {disease} simply for a patient.
Include symptoms and precautions.
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]


# build disease -> symptom map once
disease_symptom_map = {}

for i in range(len(dataset)):

    disease = dataset.iloc[i, 0]

    symptoms = [str(s).strip().lower() for s in dataset.iloc[i, 1:].values if s != ""]

    if disease not in disease_symptom_map:
        disease_symptom_map[disease] = set()

    disease_symptom_map[disease].update(symptoms)


@app.post("/predict")
def predict(data: dict):

    # frontend sends symptoms as keys
    user_symptoms = [s.strip().lower().replace(" ", "_") for s in data.keys()]

    disease_scores = {}

    for disease, symptoms in disease_symptom_map.items():

        score = 0

        for us in user_symptoms:

            if us in symptoms:
                score += 1

        disease_scores[disease] = score

    # sort diseases by score
    sorted_diseases = sorted(disease_scores.items(), key=lambda x: x[1], reverse=True)

    top3 = [d[0] for d in sorted_diseases[:3]]

    results = []

    for disease in top3:

        description = get_disease_description(disease)

        precautions = get_precautions(disease)

        if description != "No description available.":
            explanation = description
        else:
            explanation = get_llama_explanation(disease)

        results.append({
            "disease": disease,
            "description": description,
            "precautions": precautions,
            "llm_explanation": explanation
        })

    return {"predictions": results}