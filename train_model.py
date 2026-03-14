import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# load dataset
data = pd.read_csv("backend/dataset.csv")

data.fillna("", inplace=True)

# collect all symptoms
symptom_columns = data.columns[1:]

all_symptoms = set()

for col in symptom_columns:
    for symptom in data[col]:
        if symptom != "":
            all_symptoms.add(symptom)

all_symptoms = sorted(list(all_symptoms))

# convert dataset into binary symptom matrix
rows = []

for _, row in data.iterrows():

    symptom_vector = dict.fromkeys(all_symptoms, 0)

    for col in symptom_columns:
        symptom = row[col]

        if symptom != "":
            symptom_vector[symptom] = 1

    symptom_vector["disease"] = row["Disease"]

    rows.append(symptom_vector)

df = pd.DataFrame(rows)

X = df.drop("disease", axis=1)
y = df["disease"]

# train model
model = DecisionTreeClassifier()

model.fit(X, y)

# save model + feature list
joblib.dump(model, "backend/disease_model.pkl")
joblib.dump(X.columns.tolist(), "backend/symptom_columns.pkl")

print("Model trained successfully!")