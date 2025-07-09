import streamlit as st
from login import login_section

# --- Page Setup ---
st.set_page_config(page_title="HR Dashboard", layout="wide")

# --- Dark Mode Toggle with unique key ---
dark_mode = st.sidebar.toggle("🌙 Dark Mode", key="dark_mode_main")
if dark_mode:
    st.markdown("""
    <style>
    body { background: #121212 !important; color: #ffffff !important; }
    .block-container { background-color: #1e1e1e !important; }
    </style>
    """, unsafe_allow_html=True)

# --- Enhanced UI Styling ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    transition: all 0.3s ease-in-out;
}
body {
    background: linear-gradient(135deg, #f3f4f6, #f0fdf4);
}
.main .block-container {
    padding: 2rem;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 12px 36px rgba(0,0,0,0.12);
    animation: fadeInZoom 0.9s ease-in-out;
    border: 1px solid #e0e0e0;
}
@keyframes fadeInZoom {
    from { opacity: 0; transform: scale(0.98); }
    to { opacity: 1; transform: scale(1); }
}
button[kind="primary"] {
    background: linear-gradient(90deg, #00b894, #00cec9);
    color: white;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 3px 8px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# --- HR Login ---
st.image("logo.png", width=200)
st.title("🧠 HR Admin Panel")

if not login_section():
    st.stop()

# --- HR Dashboard ---
page = st.radio("Choose Action", [
    "🏠 Dashboard",
    "🧠 Resume Screener",
    "📁 Manage JDs",
    "📊 Screening Analytics",
    "📤 Email Candidates",
    "🔍 Search Resumes",
    "📝 Candidate Notes",
    "🚪 Logout"
])

# --- Page Logic ---
if page == "🏠 Dashboard":
    st.subheader("Welcome to the HR Dashboard")
    st.write("Choose an action from the options above.")

elif page == "🧠 Resume Screener":
    with open("screener.py", encoding="utf-8") as f:
        exec(f.read())

elif page == "📁 Manage JDs":
    st.subheader("📁 Job Description Manager (Coming Soon)")

elif page == "📊 Screening Analytics":
    st.subheader("📊 Screening Insights (Coming Soon)")

elif page == "📤 Email Candidates":
    st.subheader("📤 Email Shortlisted Candidates (Coming Soon)")

elif page == "🔍 Search Resumes":
    st.subheader("🔍 Resume Search by Skill (Coming Soon)")

elif page == "📝 Candidate Notes":
    st.subheader("📝 HR Notes & Annotations (Coming Soon)")

elif page == "🚪 Logout":
    st.session_state.authenticated = False
    st.success("✅ You have been logged out.")
    st.stop()
