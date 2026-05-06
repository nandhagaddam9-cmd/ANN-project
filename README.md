# Supercapacitor AI Predictor

An AI-powered web application that predicts the electrochemical performance of supercapacitor materials using Machine Learning.

## Features

- Predicts supercapacitor performance metrics
- Interactive and modern dashboard UI
- Real-time prediction updates
- Responsive design
- Dynamic charts and analytics
- Flask backend integration
- Machine Learning model support

---

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### Machine Learning
- Scikit-learn
- NumPy
- Pandas
- Joblib

---

## Project Structure

```plaintext
ANN project/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── app.py
│   ├── train.py
│   └── model.pkl
│
├── .gitignore
└── README.md
```

---

## Input Parameters

The model accepts:

- Material Type
- Capacitance (F/g)
- Voltage Window (V)
- Current Density (A/g)
- Surface Area (m²/g)
- Electrolyte Type

---

## Output Predictions

The system predicts:

- Predicted Efficiency
- Energy Density
- Power Density
- Cycle Stability

---

## How To Run The Project

### 1. Clone Repository

```bash
git clone <your-repo-link>
```

### 2. Open Project Folder

```bash
cd "ANN project"
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Environment

#### Windows PowerShell

```bash
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install flask flask-cors numpy pandas scikit-learn joblib
```

### 6. Run Backend

```bash
python backend/app.py
```

### 7. Open Frontend

Open:

```plaintext
frontend/index.html
```

with Live Server.

---

## Future Improvements

- Deep Learning model integration
- Real scientific dataset support
- Deployment on cloud platforms
- Advanced visualization dashboards
- User authentication system

---

## Author

Nandakrishnan

Machine Learning & Full Stack Development Enthusiast
