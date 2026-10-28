import streamlit as st
import plotly.express as px
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# LOGIN PROTECTION
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.switch_page("app.py")

# LOGOUT BUTTON
col1, col2 = st.columns([6,1])

with col2:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.switch_page("app.py")

# ---------------- HERO SECTION ----------------

st.image(PROJECT_ROOT / "images" / "mental_health.jpg", use_container_width=True)

st.markdown("""
<div class="header-style">
🧠 MindScope Mental Health Dashboard
</div>
""", unsafe_allow_html=True)

st.markdown("""
Welcome to **MindScope**, a platform designed to monitor student mental wellbeing.

This system analyzes student mental health factors and helps identify stress levels.
""")

st.divider()

# ---------------- METRICS SECTION ----------------

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>Students Analysed</h3>
    <h2>120</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>Model Accuracy</h3>
    <h2>95%</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>Stress Monitoring</h3>
    <h2>Active</h2>
    </div>
    """, unsafe_allow_html=True)

st.success("Welcome to MindScope — A system for monitoring student mental wellbeing.")

st.divider()

# ---------------- FEATURES SECTION ----------------

st.subheader("🚀 Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(PROJECT_ROOT / "images" / "brain_ai.jpg", use_container_width=True)
    st.markdown("### Stress Prediction")
    st.write("Predict stress levels based on student behavioral data.")

with col2:
    st.image(PROJECT_ROOT / "images" / "students.jpg", use_container_width=True)
    st.markdown("### Student Mental Analysis")
    st.write("Analyze academic, social, and psychological factors affecting student mental health.")

with col3:
    st.image(PROJECT_ROOT / "images" / "wellness.jpg", use_container_width=True)
    st.markdown("### Smart Recommendations")
    st.write("Get suggestions to improve mental wellbeing.")

st.divider()

# ---------------- DASHBOARD VISUAL ----------------

st.subheader("📊 Mental Health Insights")

col1, col2 = st.columns([2,1])

with col1:
    st.info("Explore the charts below to see student stress levels and wellbeing insights.")

with col2:
    st.markdown("""
### Why MindScope?

✔ Early stress detection  
✔ Student wellness improvement  
✔ Academic performance monitoring  
✔ Better understanding of student wellbeing  

MindScope helps educators and students identify stress risks early and improve wellbeing.
""")


st.divider()
st.subheader("📊 Student Stress Distribution")

# Sample data (you can replace later with dataset analysis)
data = {
    "Stress Level": ["Low", "Medium", "High"],
    "Students": [45, 55, 20]
}

df = pd.DataFrame(data)

fig = px.pie(
    df,
    names="Stress Level",
    values="Students",
    color="Stress Level",
    color_discrete_map={
        "Low": "green",
        "Medium": "orange",
        "High": "red"
    },
)

st.plotly_chart(fig, use_container_width=True)


st.divider()

# ---------------- TIPS SECTION ----------------

st.subheader("💡 Mental Health Tips")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("Maintain Regular Sleep")
    st.write("Adequate sleep improves focus and reduces stress.")

with col2:
    st.info("Practice Mindfulness")
    st.write("Meditation and breathing exercises help manage anxiety.")

with col3:
    st.warning("Balance Study & Leisure")
    st.write("Healthy study-life balance prevents burnout.")

st.divider()

st.caption("MindScope Mental Health System")