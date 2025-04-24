import streamlit as st
import time
import google.generativeai as genai
import matplotlib.pyplot as plt
import plotly.express as px  # Added for interactive animations
import plotly.graph_objects as go
import numpy as np
from PIL import Image  # For loading Mitosis images

# ✅ Configure Gemini API (Secure way)
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]  # Add this to secrets.toml
except:
    GEMINI_API_KEY = "AIzaSyCOkV5zuR7KY4kPwGhtCl2hWXuP1C2vegk"  # Fallback for testing

genai.configure(api_key=GEMINI_API_KEY)

# ✅ Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# ✅ Set page config
st.set_page_config(page_title="AI Lab Simulator", layout="wide", initial_sidebar_state="expanded")

# Theme toggle
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)

# Apply custom theme (Cleaner CSS)
if dark_mode:
    st.markdown("""
        <style>
            .stApp { background-color: #121212; color: #e0e0e0; }
            h1, h2, h3, h4, h5, h6 { color: #e0e0e0; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            .stApp { background-color: #ffffff; color: #000000; }
        </style>
    """, unsafe_allow_html=True)

# Dummy rule-based tutor
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

# AI Feedback
@st.cache_data(show_spinner=False)
def get_ai_feedback(simulation_data):
    prompt = f"Give detailed educational feedback on this simulation data: {simulation_data}"
    response = model.generate_content(prompt)
    return response.text.strip()

# Simulations
st.title("🔬 AI Lab Simulator: Physics & Biology")
st.subheader("Run simulations, ask your tutor, get AI feedback, and visualize your data!")

subject = st.selectbox("Choose a subject:", ["Physics", "Biology"])
simulation_result = ""

# Physics Simulation
if subject == "Physics":
    st.markdown("### ⚙ Physics Simulation: Kinetic Energy")

    mass = st.slider("Mass (kg)", 1, 10, 5)
    velocity = st.slider("Velocity (m/s)", 0, 20, 10)
    kinetic_energy = 0.5 * mass * velocity ** 2

    simulation_result = f"Mass={mass} kg, Velocity={velocity} m/s, Kinetic Energy={kinetic_energy:.2f} J"
    st.success(f"✅ Kinetic Energy: {kinetic_energy:.2f} Joules")

    # Physics Visualization (Interactive Plotly Animation)
    st.markdown("#### 📊 Energy Visualization (Interactive)")
    velocities = np.arange(0, 21, 1)  # Velocity from 0 to 20
    kinetic_energies = 0.5 * mass * velocities ** 2

    fig = px.line(x=velocities, y=kinetic_energies, labels={'x': 'Velocity (m/s)', 'y': 'Kinetic Energy (J)'},
                  title="Kinetic Energy vs Velocity")
    fig.update_traces(mode='lines+markers', hovertemplate='Velocity: %{x} m/s<br>Kinetic Energy: %{y:.2f} J')
    fig.add_scatter(x=[velocity], y=[kinetic_energy], mode='markers', marker=dict(size=15, color='red'),
                    name=f'Current Point (v={velocity}, KE={kinetic_energy:.2f})')
    st.plotly_chart(fig)

    # Animated Bar Chart (using Plotly for interactivity)
    st.markdown("#### 📈 Animated Bar Chart")
    bar_fig = go.Figure(
        data=[
            go.Bar(x=["Kinetic Energy"], y=[kinetic_energy], marker_color='skyblue')
        ],
        layout=go.Layout(
            yaxis=dict(title="Energy (Joules)"),
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(label="Play",
                              method="animate",
                              args=[None, {"frame": {"duration": 500, "redraw": True},
                                           "fromcurrent": True, "mode": "immediate"}])]
            )]
        ),
        frames=[
            go.Frame(data=[go.Bar(x=["Kinetic Energy"], y=[k])])
            for k in np.linspace(0, kinetic_energy, 20)
        ]
    )
    st.plotly_chart(bar_fig)

    st.markdown("""
        *Physics Insight:*  
        Kinetic energy increases *quadratically* with velocity. Doubling the velocity *quadruples* the kinetic energy.
    """)

# Biology Simulation
elif subject == "Biology":
    st.markdown("### 🧬 Biology Simulation: Mitosis Stages")

    cell_type = st.selectbox("Choose Cell Type:", ["Animal Cell", "Plant Cell"])
    stages = ["Prophase", "Metaphase", "Anaphase", "Telophase"]
    stage = st.selectbox("Choose Mitosis Stage:", stages)

    simulation_result = f"Cell Type={cell_type}, Stage={stage}"
    st.success(f"✅ You selected the *{stage}* stage of mitosis in a *{cell_type.lower()}*.")

    # Mitosis Diagrams (Static Images)
    st.markdown("#### 🖼 Mitosis Stage Diagram")
    mitosis_images = {
        "Prophase": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Prophase_%282%29.svg/800px-Prophase_%282%29.svg.png",
        "Metaphase": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Metaphase.svg/800px-Metaphase.svg.png",
        "Anaphase": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Anaphase.svg/800px-Anaphase.svg.png",
        "Telophase": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Telophase.svg/800px-Telophase.svg.png"
    }
    st.image(mitosis_images[stage], caption=f"{stage} Stage in {cell_type}", use_column_width=True)

    # Animated Mitosis Process (GIF Suggestion)
    st.markdown("#### 🎬 Mitosis Animation")
    st.markdown("""
        Since Streamlit can't directly render animations, you can use a GIF or video for the Mitosis process. Here's a placeholder:
    """)
    st.markdown("[Watch Mitosis Animation](https://upload.wikimedia.org/wikipedia/commons/4/4a/Mitosis_animation.gif)")
    # Note: Replace the above link with a hosted GIF or use a local file with st.image("mitosis_animation.gif")

    st.markdown(f"""
        *Biology Insight:*  
        During *{stage}*, the cell undergoes specific changes vital for division.  
        - Prophase: Chromosomes condense, spindle forms  
        - Metaphase: Chromosomes align in center  
        - Anaphase: Sister chromatids pull apart  
        - Telophase: Nuclear membranes reform  
    """)

# Get AI feedback
if st.button("🔍 Get AI Feedback"):
    with st.spinner("Generating feedback..."):
        feedback = get_ai_feedback(simulation_result)
        st.info(feedback)

# Chat with tutor
st.markdown("---")
st.markdown("### 🤖 Ask Your Tutor")
user_query = st.text_input("Ask a question (e.g., What is velocity?)")
if user_query:
    response = rule_based_tutor(user_query)
    st.write(f"Tutor: {response}")

# Quiz & Report
st.markdown("---")
st.markdown("### 📋 Post-Simulation Quiz & Report")

# Define quizzes for Physics and Biology
physics_quiz = [
    {
        "question": "What is the unit of kinetic energy?",
        "options": ["kg", "m/s", "Joules", "Watts"],
        "correct_answer": "Joules"
    },
    {
        "question": "What does velocity measure?",
        "options": ["Rate of change of position", "Rate of change of acceleration", "Mass per unit volume", "Energy per unit time"],
        "correct_answer": "Rate of change of position"
    },
    {
        "question": "How does kinetic energy change if velocity doubles?",
        "options": ["Doubles", "Triples", "Quadruples", "Remains the same"],
        "correct_answer": "Quadruples"
    }
]

biology_quiz = [
    {
        "question": "What is the main purpose of mitosis?",
        "options": ["Produce gametes", "Cell growth and repair", "Reduce chromosome number", "Exchange genetic material"],
        "correct_answer": "Cell growth and repair"
    },
    {
        "question": "During which mitosis stage do chromosomes align at the center?",
        "options": ["Prophase", "Metaphase", "Anaphase", "Telophase"],
        "correct_answer": "Metaphase"
    },
    {
        "question": "What structure pulls chromosomes apart in Anaphase?",
        "options": ["Nucleus", "Spindle fibers", "Cell membrane", "Centrioles"],
        "correct_answer": "Spindle fibers"
    }
]

# Select quiz based on subject
quiz = physics_quiz if subject == "Physics" else biology_quiz

# Show quiz questions one by one
st.markdown(f"#### 🧠 {subject} Quiz")
score = 0
total_questions = len(quiz)

for i, q in enumerate(quiz):
    st.markdown(f"*Question {i+1}/{total_questions}: {q['question']}*")
    selected_answer = st.radio(f"Select an answer for question {i+1}:", q["options"], index=None, key=f"q{i}")
    
    if selected_answer:
        if selected_answer == q["correct_answer"]:
            st.success(f"✅ Correct! {q['correct_answer']} is the right answer.")
            score += 1
        else:
            st.error(f"❌ Incorrect. The correct answer is {q['correct_answer']}.")

# Show final score
if st.button("📊 Show Quiz Results"):
    st.markdown(f"### 🎉 Quiz Results")
    st.write(f"You scored *{score}/{total_questions}* in the {subject} quiz!")
    if score == total_questions:
        st.balloons()
        st.write("Perfect score! You're a pro! 🚀")
    elif score >= total_questions // 2:
        st.write("Good job! Keep practicing! 💪")
    else:
        st.write("Nice try! Let's learn more and try again! 📚")

# Report generation
if st.button("📝 Generate Report"):
    with st.spinner("Preparing report..."):
        time.sleep(2)
        st.markdown(f"Report: Your simulation included the following parameters:\n\n{simulation_result}.\n\nYou completed an interactive session in *{subject}* and scored *{score}/{total_questions}* in the quiz. You also received both rule-based and AI-generated feedback.")