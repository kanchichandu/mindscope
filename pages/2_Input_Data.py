import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# ---------- LOGIN PROTECTION ----------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.switch_page("app.py")

st.title("📊 Student Mental Health Input")

st.markdown("Provide the following information to analyze stress levels.")

st.image(PROJECT_ROOT / "images" / "student_input.png", use_container_width=True)

st.divider()

# ---------- HEALTH FACTORS ----------
st.subheader("🧠 Health Factors")

col1, col2 = st.columns(2)

with col1:
    anxiety = st.slider("Anxiety Level",0,10,5)
    depression = st.slider("Depression Level",0,10,5)
    headache = st.slider("Headache Frequency",0,10,5)
    sleep_quality = st.slider("Sleep Quality",0,10,5)

with col2:
    self_esteem = st.slider("Self Esteem",0,10,5)
    breathing_problem = st.slider("Breathing Problems",0,10,5)
    blood_pressure = st.slider("Blood Pressure Level",0,10,5)
    mental_health_history = st.selectbox("Mental Health History",[0,1])

st.divider()

# ---------- ENVIRONMENT FACTORS ----------
st.subheader("🏠 Environment Factors")

col1, col2 = st.columns(2)

with col1:
    noise_level = st.slider("Noise Level",0,10,5)
    living_conditions = st.slider("Living Conditions",0,10,5)
    safety = st.slider("Safety Level",0,10,5)

with col2:
    basic_needs = st.slider("Basic Needs Availability",0,10,5)

st.divider()

# ---------- ACADEMIC FACTORS ----------
st.subheader("📚 Academic Factors")

col1, col2 = st.columns(2)

with col1:
    academic_performance = st.slider("Academic Performance",0,10,5)
    study_load = st.slider("Study Load",0,10,5)

with col2:
    teacher_student_relationship = st.slider("Teacher Student Relationship",0,10,5)
    future_career_concerns = st.slider("Future Career Concerns",0,10,5)

st.divider()

# ---------- SOCIAL FACTORS ----------
st.subheader("👥 Social Factors")

col1, col2 = st.columns(2)

with col1:
    social_support = st.slider("Social Support",0,10,5)
    peer_pressure = st.slider("Peer Pressure",0,10,5)

with col2:
    extracurricular_activities = st.slider("Extracurricular Activities",0,10,5)
    bullying = st.slider("Bullying Experience",0,10,5)

st.divider()

# ---------- PREDICT BUTTON ----------
if st.button("🚀 Predict Stress Level"):

    # Check if user changed any values
    if (
        anxiety == 5 and depression == 5 and study_load == 5 and peer_pressure == 5
        and sleep_quality == 5 and social_support == 5
    ):
        st.warning("⚠ Please adjust the inputs before prediction.")
        st.stop()

    st.session_state.input_data = [
        anxiety,
        self_esteem,
        mental_health_history,
        depression,
        headache,
        blood_pressure,
        sleep_quality,
        breathing_problem,
        noise_level,
        living_conditions,
        safety,
        basic_needs,
        academic_performance,
        study_load,
        teacher_student_relationship,
        future_career_concerns,
        social_support,
        peer_pressure,
        extracurricular_activities,
        bullying
    ]

    st.success("Student data saved successfully!")

    st.switch_page("pages/3_Prediction.py")

st.markdown("---")
st.caption("MindScope Mental Health Dashboard | Student Wellness System")