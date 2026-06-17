 TruthLens AI

 AI-Powered Fake News Detection Platform

TruthLens AI is a Machine Learning and Natural Language Processing (NLP) based web application that analyzes news articles and predicts whether they are **REAL** or **FAKE**. The system uses TF-IDF vectorization and a Random Forest Classifier to evaluate textual content and provide credibility insights.

 Project Overview

The rapid spread of misinformation on digital platforms has created a growing need for automated fact-checking systems. TruthLens AI addresses this challenge by providing an intelligent news analysis platform that classifies articles and generates confidence-based predictions.

The application combines Machine Learning, Flask, SQLite, and an interactive web interface to deliver real-time fake news detection.


# Key Features

# Machine Learning

a. Fake News Detection
b. Real News Detection
c. TF-IDF Text Vectorization
d. Random Forest Classification
e. Confidence Score Generation

# AI Analysis

a. Credibility Score
b. Risk Level Assessment
c. News Category Detection
d. AI-Based Explanation System

# User Features

a. Modern Responsive Interface
b. Dark Mode Support
c. Copy Result Functionality
d. Share Result Functionality
e. Searchable Analysis History

# Analytics Dashboard

a. Total News Analyses
b. Real News Statistics
c. Fake News Statistics
d. Interactive Pie Chart Visualization
e. Historical Analysis Tracking



# Technology Stack

# Frontend

a. HTML5
b. CSS3
c. JavaScript

# Backend

a. Python
b. Flask

# Machine Learning

a. Scikit-Learn
b. TF-IDF Vectorizer
c. Random Forest Classifier

# Database

a. SQLite

# Data Processing

a. Pandas
b. NumPy



## System Workflow

User Input
↓
Text Preprocessing
↓
TF-IDF Vectorization
↓
Random Forest Model
↓
Prediction Engine
↓
Confidence & Credibility Analysis
↓
Dashboard & History Storage


# Project Structure

TruthLens-AI/

├── app.py
├── create_db.py
├── train_model.py
├── requirements.txt
├── README.md

├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js

├── templates/
│   ├── index.html
│   └── dashboard.html

├── screenshots/

└── .gitignore


# Installation

# Clone Repository

bash
git clone https://github.com/kripapatwari8-creator/TruthLens-AI.git


bash
cd TruthLens-AI


# Create Virtual Environment

bash
python -m venv venv


# Activate Virtual Environment

bash
venv\Scripts\activate

# Install Dependencies

bash
pip install -r requirements.txt


# Create Database

bash
python create_db.py


# Train Model
bash
python train_model.py


# Run Application

bash
python app.py


Open:

text
http://127.0.0.1:5000

# Screenshots

# Home Page
<img width="959" height="473" alt="Screenshot 2026-06-17 045258" src="https://github.com/user-attachments/assets/c3d68f30-5046-45f3-8fb1-a44514c9a396" />

# Credibility Analysis

<img width="950" height="500" alt="Screenshot 2026-06-17 045412" src="https://github.com/user-attachments/assets/19d1be32-f1bc-4ea4-93e7-6899afcb76a5" />

# Analytics Dashboard
<img width="959" height="502" alt="Screenshot 2026-06-17 045427" src="https://github.com/user-attachments/assets/b76eeb7b-14d4-489b-9d97-f1c95a3fadef" />

## Learning Outcomes

This project demonstrates practical implementation of:

a. Machine Learning
b. Natural Language Processing
c. Text Classification
d. Full-Stack Development
e. Database Management
f. Model Deployment



This project was developed for educational and internship purposes.
