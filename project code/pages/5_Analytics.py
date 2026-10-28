import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- LOGIN PROTECTION ----------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.switch_page("app.py")

st.set_page_config(layout="wide")

st.title("📊 Student Stress Analytics")

st.progress(1.0)
st.markdown("### Analytics Dashboard")

# ---------- LOAD DATASET ----------
@st.cache_data
def load_data():
    return pd.read_csv("StressLevelDataset.csv")

try:
    df = load_data()
except:
    st.error("Dataset not found. Please check the file path.")
    st.stop()

# ---------- CONVERT STRESS LABELS ----------
stress_map = {0: "Low", 1: "Medium", 2: "High"}
df["stress_label"] = df["stress_level"].map(stress_map)

st.divider()

# ---------- SUMMARY METRICS ----------
st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", len(df))

with col2:
    st.metric("Average Stress Level", round(df["stress_level"].mean(), 2))

with col3:
    st.metric("Average Study Load", round(df["study_load"].mean(), 2))

st.divider()

# ---------- DATA PREVIEW ----------
st.subheader("Dataset Preview")
st.dataframe(df.head())

st.divider()

# ---------- STRESS DISTRIBUTION ----------
st.subheader("Stress Level Distribution")

fig1 = px.histogram(
    df,
    x="stress_label",
    color="stress_label",
    color_discrete_map={
        "Low": "green",
        "Medium": "orange",
        "High": "red"
    },
    labels={"stress_label": "Stress Level"},
    title="Distribution of Stress Levels"
)

st.plotly_chart(fig1, use_container_width=True)

st.divider()

# ---------- ANALYTICS CHARTS ----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Study Load vs Stress")

    fig2 = px.box(
        df,
        x="stress_label",
        y="study_load",
        color="stress_label",
        labels={
            "stress_label": "Stress Level",
            "study_load": "Study Load"
        }
    )

    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.subheader("Sleep Quality vs Stress")

    fig3 = px.scatter(
        df,
        x="sleep_quality",
        y="stress_label",
        color="stress_label",
        labels={
            "sleep_quality": "Sleep Quality",
            "stress_label": "Stress Level"
        }
    )

    st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ---------- PEER PRESSURE ----------
st.subheader("Peer Pressure Impact")

fig4 = px.scatter(
    df,
    x="peer_pressure",
    y="stress_label",
    color="stress_label",
    labels={
        "peer_pressure": "Peer Pressure",
        "stress_label": "Stress Level"
    }
)

st.plotly_chart(fig4, use_container_width=True)

st.divider()

# ---------- CORRELATION HEATMAP ----------
st.subheader("🔍 Feature Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")

corr = numeric_df.corr()

fig5 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    title="Correlation Between Mental Health Factors"
)

st.plotly_chart(fig5, use_container_width=True)

st.divider()

# ---------- FEATURE IMPORTANCE ----------
st.divider()

st.subheader("📊 Top Factors Affecting Student Stress")

try:

    rf_model = model.named_steps["rft"]

    feature_names = [
        "anxiety_level",
        "self_esteem",
        "mental_health_history",
        "depression",
        "headache",
        "blood_pressure",
        "sleep_quality",
        "breathing_problem",
        "noise_level",
        "living_conditions",
        "safety",
        "basic_needs",
        "academic_performance",
        "study_load",
        "teacher_student_relationship",
        "future_career_concerns",
        "social_support",
        "peer_pressure",
        "extracurricular_activities",
        "bullying"
    ]

    importances = rf_model.feature_importances_

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    })

    importance_df = importance_df.sort_values(by="Importance", ascending=False)

    fig6 = px.bar(
        importance_df.head(10),
        x="Importance",
        y="Feature",
        orientation="h",
        title="Top Factors Influencing Stress Prediction"
    )

    st.plotly_chart(fig6, use_container_width=True)

except:
    st.warning("Feature importance could not be calculated.")

st.divider()

st.caption("MindScope Mental Health Dashboard | Analytics Module")