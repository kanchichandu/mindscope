import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# ---------- LOGIN PROTECTION ----------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.switch_page("app.py")

st.title("💡 Mental Health Recommendations")

# ---------- STEP TRACKER ----------
st.progress(1.0)
st.markdown("### Step 3️⃣ : Mental Health Recommendations")

st.image(PROJECT_ROOT / "images" / "wellness_recommendation.jpg", use_container_width=True)

st.divider()

# ---------- CHECK PREDICTION ----------
if "prediction" not in st.session_state:

    st.warning("⚠ Please complete the prediction step first.")

else:

    level = st.session_state.prediction

    col1, col2, col3 = st.columns(3)

    # ---------- LOW STRESS ----------
    if level == 0:

        st.success("Low Stress Level")

        with col1:
            st.info("🧘 Maintain Healthy Lifestyle")
            st.write("""
- Continue regular exercise  
- Maintain a balanced diet  
- Practice relaxation techniques
""")

        with col2:
            st.info("👥 Stay Socially Connected")
            st.write("""
- Spend time with friends and family  
- Participate in social activities  
- Maintain positive relationships
""")

        with col3:
            st.info("📚 Balanced Study Routine")
            st.write("""
- Maintain effective study habits  
- Take regular study breaks  
- Balance study and leisure time
""")

    # ---------- MEDIUM STRESS ----------
    elif level == 1:

        st.warning("Moderate Stress Level")

        with col1:
            st.info("😴 Improve Sleep Quality")
            st.write("""
- Aim for 7–8 hours of sleep  
- Avoid late-night screen time  
- Maintain a regular sleep schedule
""")

        with col2:
            st.info("🧠 Manage Stress")
            st.write("""
- Practice deep breathing  
- Try meditation or mindfulness  
- Plan daily activities effectively
""")

        with col3:
            st.info("📖 Reduce Academic Pressure")
            st.write("""
- Break large tasks into smaller goals  
- Ask for help when needed  
- Maintain healthy study habits
""")

    # ---------- HIGH STRESS ----------
    else:

        st.error("High Stress Level")

        with col1:
            st.info("👨‍⚕ Seek Professional Support")
            st.write("""
- Speak with a counselor  
- Consult mental health professionals  
- Seek guidance from trusted mentors
""")

        with col2:
            st.info("🧘 Practice Relaxation")
            st.write("""
- Engage in yoga or meditation  
- Spend time outdoors  
- Practice calming breathing exercises
""")

        with col3:
            st.info("❤️ Emotional Support")
            st.write("""
- Talk openly with family or friends  
- Build a strong support network  
- Avoid isolation during stressful times
""")

    st.divider()

    # ---------- NAVIGATION ----------
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏠 Back to Home"):
            st.switch_page("pages/1_Home.py")

    with col2:
        if st.button("🔄 Start New Prediction"):

            if "input_data" in st.session_state:
                del st.session_state["input_data"]

            if "prediction" in st.session_state:
                del st.session_state["prediction"]

            st.switch_page("pages/2_Input_Data.py")

st.divider()

# ---------- FINAL MESSAGE ----------
st.markdown("""
### 🌿 Wellbeing Reminder

Maintaining mental wellbeing is important for overall health.  
Developing positive habits, seeking support when needed, and maintaining balance in daily life can help reduce stress.
""")

st.caption("MindScope Mental Health Dashboard | Student Wellness System")