# ✈️ AeroFare: 

## Table of Contents
* [Demo](#demo)
* [Overview](#overview)
* [Motivation](#motivation)
* [Features](#features)
* [Installation](#installation)
* [Tech Stack](#tech-stack)
* [Deployment on Streamlit](#deployment-on-streamlit)
* [Project Structure](#project-structure)
* [Bug / Feature Request](#bug--feature-request)
* [Future Scope](#future-scope)
* [Author](#author)



## Demo
Link: [https://aerofare-sdnre5xmvhrukj4nm7yftm.streamlit.app/](https://aerofare-sdnre5xmvhrukj4nm7yftm.streamlit.app/)

[![](https://github.com/Shrimanthv/AeroFare/blob/main/Screenshot%202025-05-25%20112049.png?raw=true)]
[![](https://github.com/Shrimanthv/AeroFare/blob/main/Screenshot%202025-05-25%20112118.png?raw=true)](
## Overview
AeroFare is an AI-driven web app that predicts flight fares based on user inputs such as airline, route, stops, and travel time.
It leverages machine learning models trained on historical flight data to generate accurate fare estimates.
The app offers a simple and interactive Streamlit interface to help users plan and budget their travel more effectively.


## Motivation
Airfare prices are highly dynamic and often unpredictable, making it challenging for travelers to book flights at the right time.
AeroFare was created to solve this problem by using machine learning to forecast flight fares based on real-world data.
The goal is to empower users with actionable insights, helping them make informed, cost-effective travel decisions with confidence.

## Features

- 🔍 **Predict flight fares** based on user input (airline, source, destination, stops, departure/arrival time, etc.)
- 📊 **Machine learning powered** with models like Random Forest Regressor
- 🖥️ **Streamlit-based web interface** for real-time predictions
- 📁 Clean code structure and easy-to-deploy application

---


---

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/flight-fare-prediction.git
cd flight-fare-prediction

Create a Virtual Environment

```bash
conda create -n flywise-env python=3.10
conda activate flywise-env
Install Dependencies

```bash
pip install -r requirements.txt
Run the App

```bash
streamlit run app.py

```


## Tech Stack

| Layer          | Tools Used                              |
|----------------|------------------------------------------|
| Frontend       | Streamlit                               |
| Backend        | Python, Scikit-learn, Pandas, NumPy     |
| Model Training | RandomForestRegressor, DecisionTreeRegressor |
| Deployment     | Local (can be extended to Streamlit Cloud, AWS, etc.) |

## Deployment on Streamlit
To deploy this project on Streamlit Cloud, follow these steps:

Sign up or log in to Streamlit.

Connect your GitHub account to Streamlit.

Create a new app by selecting the repository containing your project.

Choose the appropriate Python file (e.g., app.py) as the entry point.

Ensure your repository includes a requirements.txt file with all necessary dependencies.

## Project Structure 
```
AeroFare/
│
├── app.py                  # Main Streamlit application
├── model.pkl               # Trained machine learning model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── utils/                  # Preprocessing functions and helpers
│   └── data_cleaning.py
├── data/                   # Raw and cleaned datasets (CSV)
└── notebooks/              # Jupyter notebooks for EDA and training


```
## Bug / Feature Request
If you encounter any bugs or have suggestions for new features, please feel free to open an issue on the GitHub repository.

To report a bug:
Provide a clear description of the problem, steps to reproduce it, and any relevant screenshots or error messages.

To request a feature:
Describe the new functionality you'd like to see and explain how it would improve the project.

Your feedback helps improve AeroFare — thank you for contributing!

## Technologies Used


<img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" width="180" alt="Streamlit Logo" />
<img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width="200" alt="Scikit-learn Logo" />
<img src="https://pandas.pydata.org/static/img/pandas_mark.svg" width="150" alt="Pandas Logo" />
<img src="https://numpy.org/images/logo.svg" width="150" alt="NumPy Logo" />
🔮 Future Use and Enhancements
Expand Model Accuracy: Incorporate additional data sources like seasonal trends, holidays, and competitor pricing to improve prediction precision.

Real-time Price Tracking: Integrate APIs to fetch live flight prices and offer dynamic alerts for fare drops.

Multi-modal Travel: Extend the system to predict fares for other transport modes such as trains and buses.

Mobile App Development: Build a user-friendly mobile app to increase accessibility and user engagement.

Personalized Recommendations: Use user behavior and preferences to tailor travel suggestions and optimal booking times.

## Author
Shrimanth V
Email: shrimanthv99@gmail.com
Feel free to reach out for any questions or collaboration!