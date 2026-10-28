import streamlit as st
import joblib
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time
from pathlib import Path

st.set_page_config(layout="wide")

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# ---------- LOGIN PROTECTION ----------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.switch_page("app.py")

st.title("🤖 Stress Prediction Result")

# ---------- LOAD MODEL ----------
model = joblib.load(PROJECT_ROOT / "model" / "mental_health_model.pkl")

# ---------- CHECK INPUT ----------
if "input_data" not in st.session_state:

    st.warning("⚠ Please enter student data first in the Input Page.")

else:

    data = np.array([st.session_state.input_data])

    # ---------- LOADING SPINNER ----------
    with st.spinner("Analyzing student stress level..."):
        time.sleep(2)
        prediction = model.predict(data)[0]

    # ---------- PROBABILITY ----------
    probabilities = model.predict_proba(data)[0]

    low_prob = round(probabilities[0] * 100)
    medium_prob = round(probabilities[1] * 100)
    high_prob = round(probabilities[2] * 100)

    st.session_state.prediction = prediction

    # ---------- PROGRESS BAR ----------
    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    stress_labels = {
        0: "Low Stress",
        1: "Medium Stress",
        2: "High Stress"
    }

    st.divider()

    # ---------- RESULT DISPLAY ----------
    col1, col2 = st.columns([1,2])

    with col1:

        st.subheader("Prediction Result")

        if prediction == 0:
            st.success("Low Stress Level Detected")

        elif prediction == 1:
            st.warning("Moderate Stress Level Detected")

        else:
            st.error("High Stress Level Detected")

        st.metric("Predicted Level", stress_labels[prediction])

    # ---------- STRESS METER ----------
    with col2:

        if prediction == 0:
            meter_value = 20
        elif prediction == 1:
            meter_value = 60
        else:
            meter_value = 90

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=meter_value,
            title={'text': "Stress Meter"},
            number={'suffix': "%"},
            gauge={
                'axis': {'range': [0,100]},
                'bar': {'color': "black"},
                'steps': [
                    {'range': [0,33], 'color': "#2ecc71"},
                    {'range': [33,66], 'color': "#f1c40f"},
                    {'range': [66,100], 'color': "#e74c3c"}
                ],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': meter_value
                }
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ---------- STRESS PROBABILITY ----------
    st.subheader("Stress Prediction Probability")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Low Stress", f"{low_prob}%")

    with col2:
        st.metric("Medium Stress", f"{medium_prob}%")

    with col3:
        st.metric("High Stress", f"{high_prob}%")

    # ---------- PROBABILITY CHART ----------
    prob_data = {
        "Stress Level": ["Low", "Medium", "High"],
        "Probability": [low_prob, medium_prob, high_prob]
    }

    fig2 = px.bar(
        prob_data,
        x="Stress Level",
        y="Probability",
        color="Stress Level",
        title="Stress Prediction Probability"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # ---------- STRESS ANALYSIS ----------
    st.subheader("Stress Analysis")

    if prediction == 0:

        st.info("""
The student currently shows **low stress indicators**.

Mental health condition appears stable.  
Continue maintaining a balanced lifestyle and healthy study habits.
""")

    elif prediction == 1:

        st.warning("""
The student shows **moderate stress indicators**.

Academic workload and lifestyle factors may be contributing.  
Early stress management techniques are recommended.
""")

    else:

        st.error("""
The student shows **high stress indicators**.

Immediate attention is recommended including counseling
and lifestyle adjustments.
""")

    st.divider()

    # ---------- NAVIGATION ----------
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 Start New Prediction"):
            del st.session_state["input_data"]
            st.switch_page("pages/2_Input_Data.py")

    with col2:
        if st.button("💡 View Recommendations"):
            st.switch_page("pages/4_Recommendations.py")

st.markdown("---")
st.caption("MindScope Mental Health Dashboard | Student Wellness System")