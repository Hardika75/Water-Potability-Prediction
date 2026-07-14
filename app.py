from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Load dataset to get column order
df = pd.read_csv("cleaned_water_data.csv")
feature_columns = df.drop("Potability", axis=1).columns

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = []

        for col in feature_columns:
            val = request.form.get(col)
            if val == "" or val is None:
                val = 0
            features.append(float(val))

        final_features = np.array([features])

        prediction = model.predict(final_features)

        if prediction[0] == 1:
            result = "Safe to Drink"
        else:
            result = "Not Safe to Drink"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        print("ERROR:", e)
        return render_template('index.html', prediction_text="Error in input")

if __name__ == "__main__":
    app.run(debug=True)