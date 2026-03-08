 # ⚡ AI-Powered Power Anomaly Detection System

An intelligent cloud-native solution for detecting anomalies in household electricity consumption using Machine Learning and Generative AI. The system identifies unusual power usage patterns and provides AI-driven root cause diagnostics through an interactive dashboard.

📌 Project Overview

Energy consumption data often contains hidden anomalies that may indicate:

Faulty appliances

Power surges or voltage fluctuations

Wiring issues

Electricity theft

Unexpected energy usage

This project leverages Isolation Forest anomaly detection along with Generative AI diagnostics to identify and explain abnormal power patterns.

The solution is deployed using AWS cloud services for scalability and reliability.

🚀 Key Features
⚡ Intelligent Anomaly Detection

Detects abnormal power consumption patterns using Isolation Forest

Unsupervised ML model suitable for large datasets

📊 Interactive Visualization Dashboard

Built with Streamlit

Displays time-series electricity consumption trends

Highlights anomalies in real time

🧠 AI-Powered Root Cause Analysis

Uses Amazon Bedrock (LLM) to analyze detected anomalies

Provides:

Severity classification

Probable causes

Recommended actions

☁ Cloud-Native Architecture

Amazon EC2 – hosts the Streamlit application

Amazon S3 – stores power consumption datasets

Amazon SageMaker – hosts ML inference endpoint

Amazon Bedrock – provides generative AI explanations

🔎 Scalable System Design

Decoupled storage and compute

ML inference handled via API endpoint

Easily extensible for smart grid monitoring

🏗 System Architecture
User
 ↓
Streamlit Dashboard (EC2)
 ↓
Amazon S3 (Dataset Storage)
 ↓
Amazon SageMaker (ML Inference Endpoint)
 ↓
Anomaly Results
 ↓
Amazon Bedrock (AI Diagnosis)
 ↓
Interactive Dashboard Visualization
🧰 Technologies Used
Layer	Technology
Cloud Platform	AWS
Compute	Amazon EC2
Storage	Amazon S3
Machine Learning	Amazon SageMaker
Generative AI	Amazon Bedrock
Programming Language	Python
Data Processing	Pandas, NumPy
ML Algorithm	Isolation Forest
Visualization	Plotly
Dashboard Framework	Streamlit
📂 Project Structure
power-anomaly-detection/
│
├── data/
│   └── household_power_consumption.csv
│
├── models/
│   └── isolation_forest_model.pkl
│
├── notebooks/
│   └── anomaly_detection_training.ipynb
│
├── app/
│   └── app.py
│
├── screenshots/
│   └── dashboard.png
│
├── requirements.txt
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/power-anomaly-detection.git
cd power-anomaly-detection

Create virtual environment:

python -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
▶️ Running the Application

Start the Streamlit dashboard:

streamlit run app.py

Then open in browser:

http://localhost:8501
📊 Dataset

The project uses the Household Power Consumption Dataset, containing measurements such as:

Global Active Power

Voltage

Global Intensity

Sub-metering values

Dataset contains ~2 million records of electricity usage data.

📈 Model Details

Algorithm Used: Isolation Forest

Why Isolation Forest?

Efficient for large datasets

Works well for unsupervised anomaly detection

Detects rare patterns without labeled data

📊 Prototype Performance
Metric	Result
Dataset Size	~2 Million Records
Model Type	Isolation Forest
Dashboard Load Time	~3 seconds
ML Inference Time	~1 second
AI Diagnosis Response	~2–4 seconds
💰 Estimated Deployment Cost (AWS)
Service	Estimated Monthly Cost
EC2 (t3.medium)	~$30
Amazon S3	~$2
SageMaker Endpoint	~$40
Amazon Bedrock	~$10

Total Estimated Cost: ~$80/month

📸 Prototype Snapshot

(Add your dashboard screenshot here)

Example:

screenshots/dashboard.png
🔮 Future Improvements

Real-time smart meter data integration

Automated anomaly alert system

Mobile dashboard for energy monitoring

Predictive energy consumption forecasting

Integration with IoT energy sensors

👨‍💻 Author : Pranav Kavishwar (GitHub ID : pgk99)

Developed as part of AI for Bharat Hackathon
