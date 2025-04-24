import streamlit as st
import time
import google.generativeai as genai
from google.generativeai import GenerativeModel

# ✅ Configure Gemini API
GEMINI_API_KEY = "AIzaSyApJiiwcVKFxVsZ09H4jiJmlvsRxNj0kiE"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# ✅ Set page config
st.set_page_config(page_title="AI Lab Simulator", layout="wide", initial_sidebar_state="expanded")

# Dark mode toggle
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)  # Set default to False (white background)

# Apply styles based on theme
if dark_mode:
    st.markdown("""
        <style>
            body, .stApp {
                background-color: #121212;
                color: #e0e0e0;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body, .stApp {
                background-color: #ffffff;
                color: #000000;
            }
        </style>
    """, unsafe_allow_html=True)

# Dummy rule-based tutor chatbot
def rule_based_tutor(user_input):
    rules = {
        "velocity": "Velocity is the rate of change of position with respect to time.",
        "acceleration": "Acceleration is the rate of change of velocity.",
        "cell": "A cell is the basic structural and functional unit of life.",
        "mitosis": "Mitosis is a type of cell division that results in two daughter cells."
    }
    for keyword in rules:
        if keyword in user_input.lower():
            return rules[keyword]
    return "I didn't understand that. Can you ask something else about Physics or Biology?"

# AI feedback using Gemini
@st.cache_data(show_spinner=False)
def get_ai_feedback(simulation_data):
    prompt = f"Give feedback for this simulation data: {simulation_data}"
    response = model.generate_content(prompt)
    return response.text.strip()

# Simulations
st.title("🔬 AI Lab Simulator: Physics & Biology")
st.subheader("Run simulations, ask your tutor, and learn interactively!")

subject = st.selectbox("Choose a subject:", ["Physics", "Biology"])

simulation_result = ""

if subject == "Physics":
    st.markdown("### ⚙ Physics Simulation")
    mass = st.slider("Mass (kg)", 1, 10, 5)
    velocity = st.slider("Velocity (m/s)", 0, 20, 10)
    kinetic_energy = 0.5 * mass * velocity ** 2
    simulation_result = f"Mass={mass}, Velocity={velocity}, Kinetic Energy={kinetic_energy:.2f} J"
    st.success(f"Kinetic Energy: {kinetic_energy:.2f} J")

elif subject == "Biology":
    st.markdown("### 🧬 Biology Simulation")
    cell_type = st.selectbox("Choose Cell Type:", ["Animal Cell", "Plant Cell"])
    stages = ["Prophase", "Metaphase", "Anaphase", "Telophase"]
    stage = st.selectbox("Choose Mitosis Stage:", stages)
    simulation_result = f"Cell Type={cell_type}, Stage={stage}"
    st.success(f"You selected the {stage} stage of mitosis in a {cell_type.lower()}.")

# Get AI feedback
if st.button("🔍 Get AI Feedback"):
    with st.spinner("Generating feedback..."):
        feedback = get_ai_feedback(simulation_result)
        st.info(feedback)

# Chat with tutor
st.markdown("---")
st.markdown("### 🤖 Ask Your Tutor")
user_query = st.text_input("Type your question (e.g., What is velocity?)")
if user_query:
    tutor_response = rule_based_tutor(user_query)
    st.write(f"*Tutor:* {tutor_response}")

# Quiz and Report Generation
st.markdown("---")
st.markdown("### 📋 Post-Simulation Quiz & Report")
if st.button("📝 Generate Quiz & Report"):
    with st.spinner("Preparing your quiz and report..."):
        time.sleep(2)
        st.markdown("*Quiz:* What is the unit of kinetic energy?\n\nA. kg\n\nB. m/s\n\nC. Joules\n\nD. Watts")
        st.markdown("*Answer: C. Joules*")

        st.markdown(f"*Report:* Based on your simulation, the values were: {simulation_result}. You successfully completed a simulation in {subject} and received feedback from the AI tutor.")

# Footer
st.markdown("""<style>.reportview-container .main footer {visibility: hidden;}</style>""", unsafe_allow_html=True)
import streamlit as st
import time
import google.generativeai as genai
from google.generativeai import GenerativeModel

# ✅ Configure Gemini API
GEMINI_API_KEY = "AIzaSyApJiiwcVKFxVsZ09H4jiJmlvsRxNj0kiE"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# ✅ Set page config
st.set_page_config(page_title="AI Lab Simulator", layout="wide", initial_sidebar_state="expanded")

# Dark mode toggle
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)  # Set default to False (white background)

# Apply styles based on theme
if dark_mode:
    st.markdown("""
        <style>
            body, .stApp {
                background-color: #121212;
                color: #e0e0e0;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body, .stApp {
                background-color: #ffffff;
                color: #000000;
            }
        </style>
    """, unsafe_allow_html=True)

# Dummy rule-based tutor chatbot
def rule_based_tutor(user_input):
    rules = {
        "velocity": "Velocity is the rate of change of position with respect to time.",
        "acceleration": "Acceleration is the rate of change of velocity.",
        "cell": "A cell is the basic structural and functional unit of life.",
        "mitosis": "Mitosis is a type of cell division that results in two daughter cells."
    }
    for keyword in rules:
        if keyword in user_input.lower():
            return rules[keyword]
    return "I didn't understand that. Can you ask something else about Physics or Biology?"

# AI feedback using Gemini
@st.cache_data(show_spinner=False)
def get_ai_feedback(simulation_data):
    prompt = f"Give feedback for this simulation data: {simulation_data}"
    response = model.generate_content(prompt)
    return response.text.strip()

# Simulations
st.title("🔬 AI Lab Simulator: Physics & Biology")
st.subheader("Run simulations, ask your tutor, and learn interactively!")

subject = st.selectbox("Choose a subject:", ["Physics", "Biology"])

simulation_result = ""

if subject == "Physics":
    st.markdown("### ⚙ Physics Simulation")
    mass = st.slider("Mass (kg)", 1, 10, 5)
    velocity = st.slider("Velocity (m/s)", 0, 20, 10)
    kinetic_energy = 0.5 * mass * velocity ** 2
    simulation_result = f"Mass={mass}, Velocity={velocity}, Kinetic Energy={kinetic_energy:.2f} J"
    st.success(f"Kinetic Energy: {kinetic_energy:.2f} J")

elif subject == "Biology":
    st.markdown("### 🧬 Biology Simulation")
    cell_type = st.selectbox("Choose Cell Type:", ["Animal Cell", "Plant Cell"])
    stages = ["Prophase", "Metaphase", "Anaphase", "Telophase"]
    stage = st.selectbox("Choose Mitosis Stage:", stages)
    simulation_result = f"Cell Type={cell_type}, Stage={stage}"
    st.success(f"You selected the {stage} stage of mitosis in a {cell_type.lower()}.")

# Get AI feedback
if st.button("🔍 Get AI Feedback"):
    with st.spinner("Generating feedback..."):
        feedback = get_ai_feedback(simulation_result)
        st.info(feedback)

# Chat with tutor
st.markdown("---")
st.markdown("### 🤖 Ask Your Tutor")
user_query = st.text_input("Type your question (e.g., What is velocity?)")
if user_query:
    tutor_response = rule_based_tutor(user_query)
    st.write(f"*Tutor:* {tutor_response}")

# Quiz and Report Generation
st.markdown("---")
st.markdown("### 📋 Post-Simulation Quiz & Report")
if st.button("📝 Generate Quiz & Report"):
    with st.spinner("Preparing your quiz and report..."):
        time.sleep(2)
        st.markdown("*Quiz:* What is the unit of kinetic energy?\n\nA. kg\n\nB. m/s\n\nC. Joules\n\nD. Watts")
        st.markdown("*Answer: C. Joules*")

        st.markdown(f"*Report:* Based on your simulation, the values were: {simulation_result}. You successfully completed a simulation in {subject} and received feedback from the AI tutor.")

# Footer
st.markdown("""<style>.reportview-container .main footer {visibility: hidden;}</style>""", unsafe_allow_html=True)
