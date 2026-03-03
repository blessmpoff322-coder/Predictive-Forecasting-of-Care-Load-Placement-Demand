Predictive Care Load Forecasting

Repository: UAC_Forecasting_Project

Project Overview

This project implements a predictive forecasting system for daily care load using SARIMA and machine learning models (Random Forest and Gradient Boosting). The goal is to provide actionable insights for staff allocation, capacity planning, and early warning of high-demand days.

The repository includes:

Data preprocessing scripts to clean and prepare historical care load data.

Time series and machine learning models for short-term forecasting.

Evaluation metrics (MAE, RMSE, MAPE) to assess model performance.

Forecast confidence intervals and breach probability calculations.

Interactive Streamlit dashboard for visualizing forecasts and risk levels.

Saved models (saved_models.pkl) for quick deployment.

Executive summary and research paper in .docx format for stakeholders and technical documentation.

Features

SARIMA model captures trend and weekly seasonality.

Random Forest & Gradient Boosting models incorporate lag, rolling, and calendar features.

Visualization of forecasts with confidence intervals and high-risk days.

Interactive Streamlit dashboard for exploring forecasts.

CSV export of forecast data.

Ready-to-use requirements.txt for environment setup.

Installation
# Clone the repository
git clone https://github.com/<your-username>/UAC_Forecasting_Project.git

# Navigate to project folder
cd UAC_Forecasting_Project

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run streamlit_app.py
Usage

Explore the Streamlit dashboard to view forecasted care load, confidence intervals, and breach probability.

Use the date filter to focus on specific periods.

Download forecast data as CSV for further analysis.

Project Structure
UAC_Forecasting_Project/
├── app/                   # Streamlit app files
├── data/                  # Raw and processed datasets
├── models/                # Trained ML models (saved_models.pkl)
├── notebooks/             # Jupyter notebooks with EDA and modeling
├── executive_summary.docx # High-level project summary for stakeholders
├── research_paper.docx    # Detailed technical report
├── requirements.txt       # Project dependencies
└── streamlit_app.py       # Interactive dashboard
Contributors

Blessy Margreat Priscilla J 
