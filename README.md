# 💧 Water Potability Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether water is potable (safe for drinking) using Machine Learning. It includes data preprocessing, exploratory data analysis, model training, and a Flask web application for prediction.

---

## 📂 Project Structure

```
Water-Potability-Prediction/
│
├── notebooks/
│   ├── MLactivity01.ipynb
│   └── MLactivity2.ipynb
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── water.csv
├── cleaned_water_data.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- Jupyter Notebook

---

## 📊 Project Workflow

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Selection
- Model Training
- Water Potability Prediction
- Flask Web Application

---

## 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/Hardika75/Water-Potability-Prediction.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train the model

```bash
python train_model.py
```

### Run the Flask application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📷 Visualizations

The project includes:

- Heatmap
- Pair Plot
- Histogram
- Box Plot
- Bar Chart

---

## 🎯 Future Improvements

- Deploy using Render or Railway
- Hyperparameter tuning
- Try additional ML algorithms
- Improve UI

---

## 📝 Note

The trained model file (`model.pkl`) is not included in this repository because it exceeded GitHub's file size limit. To generate the model locally, run:

```bash
python train_model.py
```

This will create the `model.pkl` file required by the Flask application.

## 👩‍💻 Author

**Hardhika V Shetty**
