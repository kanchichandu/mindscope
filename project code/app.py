import streamlit as st

st.set_page_config(page_title="MindScope Login", layout="centered")

# ---------- SESSION ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------- IF ALREADY LOGGED IN ----------
if st.session_state.logged_in:
    st.success("Already logged in ✅")
    if st.button("Go to Home"):
        st.switch_page("pages/1_Home.py")
    st.stop()

# ---------- LOGIN UI ----------
st.title("🧠 MindScope")
st.subheader("Register")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", 1, 100)

if st.button("register"):
    if name:
        st.session_state.logged_in = True
        st.session_state.user_name = name

        st.success(f"Welcome {name} 👋")

        st.switch_page("pages/1_Home.py")
    else:
        st.warning("Please enter your name")