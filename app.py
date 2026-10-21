from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

MODEL_PATH = Path("models/student_performance_model.joblib")

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered",
)

st.title("🎓 Student Performance Predictor")
st.write(
    "Predict a student's final Mathematics grade (G3) "
    "using previous grades and selected student information."
)

if not MODEL_PATH.exists():
    st.error("Trained model not found. Run: python main.py")
    st.stop()

saved = joblib.load(MODEL_PATH)
model = saved["model"]

st.info(
    "This educational demo uses the UCI Student Performance dataset. "
    "Predictions are estimates, not guaranteed grades."
)

with st.form("prediction_form"):
    st.subheader("Student Information")

    col1, col2 = st.columns(2)

    with col1:
        school = st.selectbox("School", ["GP", "MS"])
        sex = st.selectbox("Sex", ["F", "M"])
        age = st.slider("Age", 15, 22, 17)
        studytime = st.selectbox(
            "Weekly study time",
            options=[1, 2, 3, 4],
            format_func=lambda x: {
                1: "Less than 2 hours",
                2: "2–5 hours",
                3: "5–10 hours",
                4: "More than 10 hours",
            }[x],
        )
        failures = st.selectbox("Past class failures", [0, 1, 2, 3])
        absences = st.number_input(
            "School absences", min_value=0, max_value=100, value=0
        )

    with col2:
        internet = st.selectbox("Internet access at home", ["yes", "no"])
        higher = st.selectbox(
            "Wants higher education", ["yes", "no"]
        )
        goout = st.slider(
            "Going out with friends (1–5)", 1, 5, 3
        )
        health = st.slider("Current health (1–5)", 1, 5, 3)
        g1 = st.slider("First period grade (G1)", 0, 20, 10)
        g2 = st.slider("Second period grade (G2)", 0, 20, 10)

    submitted = st.form_submit_button(
        "Predict Final Grade", type="primary", use_container_width=True
    )

if submitted:
    student = pd.DataFrame(
        [{
            "school": school,
            "sex": sex,
            "age": age,
            "studytime": studytime,
            "failures": failures,
            "absences": absences,
            "internet": internet,
            "higher": higher,
            "goout": goout,
            "health": health,
            "G1": g1,
            "G2": g2,
        }]
    )

    prediction = float(model.predict(student)[0])
    prediction = max(0.0, min(20.0, prediction))

    st.subheader("Predicted Final Grade")
    st.metric("Estimated G3 score", f"{prediction:.1f} / 20")
    st.progress(prediction / 20)

    if prediction >= 15:
        st.success("The model predicts a high final grade.")
    elif prediction >= 10:
        st.info("The model predicts a moderate final grade.")
    else:
        st.warning(
            "The model predicts a lower final grade. "
            "This is an estimate, not a judgment of the student."
        )

    st.caption(
        "Model predictions may be inaccurate, especially for students "
        "whose characteristics differ from the training dataset."
    )
