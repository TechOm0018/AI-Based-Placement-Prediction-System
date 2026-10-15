# 🎓 Placify AI — AI-Based Placement Prediction System

An end-to-end Machine Learning web platform designed to analyze student academic performance, technical projects, internships, certifications, and aptitude scores to predict campus placement readiness and provide actionable, personalized recommendations.

[![GitHub Repo](https://img.shields.io/badge/GitHub-TechOm0018-blue?logo=github)](https://github.com/TechOm0018/AI-Based-Placement-Prediction-System)
[![Live Demo](https://img.shields.io/badge/Website-Live%20on%20GitHub%20Pages-success?style=flat&logo=githubpages)](https://techom0018.github.io/AI-Based-Placement-Prediction-System/)
[![React](https://img.shields.io/badge/Frontend-React%20%2B%20Vite-61DAFB?logo=react)](https://react.dev/)
[![Flask](https://img.shields.io/badge/Backend-Python%20Flask-000000?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?logo=scikit-learn)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> 🚀 **Live Website**: [https://techom0018.github.io/AI-Based-Placement-Prediction-System/](https://techom0018.github.io/AI-Based-Placement-Prediction-System/)

---

## 🌟 Key Features

- **🎯 Real-Time Placement Probability**: Instant prediction with confidence score and risk categorization (*High Chance*, *Medium Chance*, *Low Chance*).
- **🧠 Interpretable AI / Explainability**: Highlights the top factors (e.g., Internships, Projects, CGPA) driving the prediction.
- **💡 Actionable Guidance**: Generates personalized recommendations based on student weak spots (aptitude practice, mock interviews, certifications).
- **📊 Institutional Analytics Dashboard**: Visualizes cohort readiness metrics, skill distributions, and progress trends using interactive charts.
- **📱 Responsive UI**: Modern, glassmorphism-inspired dark interface built with React, Vite, Lucide Icons, and Recharts.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React 19, Vite, Lucide React, Recharts, React Router DOM, CSS Variables |
| **Backend** | Python 3, Flask, Flask-CORS, Gunicorn |
| **Machine Learning** | Scikit-learn (Logistic Regression, StandardScaler), Pandas, NumPy, Joblib |
| **Deployment Ready** | Vercel / Netlify (Frontend) + Render / Railway (Backend) |

---

## 📂 Project Structure

```
AI-Placement-Prediction-System/
├── backend/
│   ├── app.py                 # Flask REST API with /predict endpoint
│   ├── placement_data.csv     # Training dataset
│   ├── placement_model.pkl    # Pre-trained ML model
│   ├── scaler.pkl             # Feature scaler
│   ├── requirements.txt       # Python dependencies (Flask, scikit-learn, etc.)
│   └── train_model.py         # Model training script
├── frontend/
│   ├── public/                # Static assets
│   ├── src/
│   │   ├── components/        # UI components
│   │   ├── main.jsx           # React app, router & pages
│   │   └── styles.css         # Modern design system styles
│   ├── index.html             # HTML entry point
│   ├── package.json           # Frontend dependencies & scripts
│   └── vite.config.js         # Vite configuration
├── previews/
│   └── preview.html           # Standalone visual preview
├── RUN_INSTRUCTIONS.txt       # Local quick-start guide
└── README.md                  # Project documentation
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- **Python 3.9+**
- **Node.js 18+** & npm

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
# Windows:
python -m venv venv
venv\Scripts\activate
# macOS/Linux:
# python3 -m venv venv
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Re-train the model
python train_model.py

# Start Flask server
python app.py
```
Backend runs at `http://127.0.0.1:5000`.

### 3. Frontend Setup

```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```
Open `http://localhost:5173` in your browser.

---

## 🌐 Deploying Live (Step-by-Step)

### Option A: Deploy Frontend to Vercel
1. Go to [Vercel](https://vercel.com/) and import `TechOm0018/AI-Based-Placement-Prediction-System`.
2. Set **Root Directory** to `frontend`.
3. Set **Framework Preset** to `Vite`.
4. (Optional) In Environment Variables, add:
   - `VITE_API_URL`: Your deployed backend URL (e.g. `https://your-flask-app.onrender.com`)
5. Click **Deploy**.

### Option B: Deploy Backend to Render
1. Go to [Render](https://render.com/) and create a new **Web Service**.
2. Connect your GitHub repository: `TechOm0018/AI-Based-Placement-Prediction-System`.
3. Configure the service:
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Click **Create Web Service**.
5. Once deployed, copy your Render URL and set it as `VITE_API_URL` on your Vercel frontend.

---

## 📡 API Reference

### Health Check
- **URL**: `/`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "status": "ok",
    "message": "Placify AI Placement Prediction API"
  }
  ```

### Prediction Endpoint
- **URL**: `/predict`
- **Method**: `POST`
- **Headers**: `Content-Type: application/json`
- **Payload Example**:
  ```json
  {
    "CGPA": 8.4,
    "SSC_Marks": 88,
    "HSC_Marks": 84,
    "Internships": 2,
    "Projects": 3,
    "Certifications": 4,
    "AptitudeScore": 82,
    "SoftSkillsRating": 4.2,
    "Backlogs": 0,
    "Extracurricular": "Yes",
    "PlacementTraining": "Yes"
  }
  ```
- **Response Example**:
  ```json
  {
    "prediction": "Placed",
    "probability": 87.4,
    "category": "High Chance",
    "confidence": 87.4,
    "top_factors": [
      ["Internships", 1.82],
      ["Projects", 1.45],
      ["CGPA", 1.21]
    ],
    "suggestions": [
      "Keep strengthening role-specific technical skills.",
      "Practice mock interviews and aptitude regularly."
    ]
  }
  ```

---

## 👤 Author

- **GitHub**: [@TechOm0018](https://github.com/TechOm0018)
- **Repository**: [AI-Based-Placement-Prediction-System](https://github.com/TechOm0018/AI-Based-Placement-Prediction-System)
