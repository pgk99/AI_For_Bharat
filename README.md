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
