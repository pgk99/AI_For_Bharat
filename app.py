import streamlit as st
from openai import OpenAI
import os
import pandas as pd
import plotly.graph_objects as go


# Page Config
st.set_page_config(
    layout="wide",
    page_title="Power Anomaly Detection",
    page_icon="⚡"
)

# OpenAI API Key
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

#Load the dataset
@st.cache_data
def load_data(uploaded_file):
    power = pd.read_csv(uploaded_file)

    # Combine Date + Time → datetime
    power['datetime'] = pd.to_datetime(power['Date'] + ' ' + power['Time'])
    power.set_index('datetime', inplace=True)

    # Drop original columns
    power.drop(['Date', 'Time'], axis=1, inplace=True)

    return power


# Title
st.title("⚡ Power Anomaly Detection Dashboard")
st.markdown("**AI-Powered Analysis of Household Electricity Anomalies**")


# Sidebar Upload
st.sidebar.header("📁 Data Upload")
uploaded_file = st.sidebar.file_uploader("Upload Power CSV", type=['csv'])


# Main App Logic
if uploaded_file is not None:

    power = load_data(uploaded_file)

    st.success(f"✅ Loaded {len(power):,} rows")

    # Check anomaly column
    if 'anamoly' not in power.columns:
        st.error("❌ No 'anamoly' column found. Please run Isolation Forest first.")
    else:
        # 📊 Metrics (Full Dataset)
        col1, col2 = st.columns(2)

        total_anomalies = (power['anamoly'] == -1).sum()
        anomaly_rate = (power['anamoly'] == -1).mean() * 100

        with col1:
            st.metric("Total Anomalies", f"{total_anomalies:,}")
            st.metric("Anomaly Rate", f"{anomaly_rate:.2f}%")

        with col2:
            st.metric("Total Records", f"{len(power):,}")

        # 📉 Downsample for Plotting
        plot_data = power.iloc[::50]   # keep every 50th row (~40k rows)

        anomalies_plot = plot_data[plot_data['anamoly'] == -1]

        st.subheader("📈 Active Power Trend with Anomalies")

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=plot_data.index,
            y=plot_data['Global_active_power'],
            mode='lines',
            name='Active Power',
            opacity=0.6
        ))

        fig.add_trace(go.Scatter(
            x=anomalies_plot.index,
            y=anomalies_plot['Global_active_power'],
            mode='markers',
            marker=dict(color='red', size=6),
            name='Anomalies'
        ))

        st.plotly_chart(fig, use_container_width=True)

        # =============================
        # 🤖 AI Diagnosis Section
        # =============================
        st.header("🤖 AI Anomaly Diagnosis")

        anomaly_periods = power[power['anamoly'] == -1].index[:5].tolist()

        if len(anomaly_periods) > 0:

            selected_period = st.selectbox(
                "Select anomaly to analyze:",
                anomaly_periods
            )

            if st.button("🔍 Analyze This Anomaly"):

                with st.spinner("AI analyzing..."):

                    row = power.loc[selected_period]

                    prompt = f"""
                    An anomaly occurred at {selected_period}.

                    Active Power: {row['Global_active_power']} kW
                    Voltage: {row['Voltage']} V
                    Current: {row['Global_intensity']} A

                    Explain:
                    1. Severity (Low/Medium/High)
                    2. Top 3 possible causes
                    3. Recommended action items
                    """
                    client = OpenAI()

                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=400,
                        temperature=0.3
                    )

                    st.success("✅ AI Diagnosis")
                    st.markdown(response.choices[0].message.content)

        else:
            st.info("No anomalies detected in dataset.")