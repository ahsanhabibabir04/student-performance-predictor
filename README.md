# Student Performance Predictor

A machine learning project that predicts a student's final Mathematics grade using student information, study habits, absences, and previous academic performance.

## Live Demo

**Try the application:** [Student Performance Predictor](https://student-performance-predictor-byabir.streamlit.app/)

**GitHub Repository:** [student-performance-predictor](https://github.com/ahsanhabibabir04/student-performance-predictor)

## Project Overview

The Student Performance Predictor is a machine learning application built with Python and Streamlit. It uses a Random Forest Regression model to estimate a student's final Mathematics grade (`G3`) on a scale of 0 to 20.

The project uses the UCI Student Performance dataset and demonstrates a complete machine learning workflow, including data processing, feature selection, model training, evaluation, automated testing, and web application deployment.

## Model Performance

The model was evaluated using a held-out test set containing 79 student records.

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 1.07 |
| Root Mean Squared Error (RMSE) | 1.76 |
| R² Score | 0.849 |
| Training Samples | 316 |
| Testing Samples | 79 |
| Total Dataset Records | 395 |

### What Do These Metrics Mean?

- **MAE — 1.07:** The model's predictions differ from the actual grades by approximately 1.07 grade points on average.
- **RMSE — 1.76:** This metric gives greater weight to larger prediction errors.
- **R² Score — 0.849:** The model explains approximately 84.9% of the variation in the target grades on this particular test set.

These results come from one train/test split and do not guarantee the same performance on new data.

## Features

The model uses 12 input features:

- School
- Student sex
- Student age
- Study time
- Number of previous class failures
- Number of absences
- Internet access
- Intention to pursue higher education
- Going-out frequency
- Health status
- First-period grade (`G1`)
- Second-period grade (`G2`)

**Target variable:** Final Mathematics grade (`G3`), ranging from 0 to 20.

The application uses the trained model to generate a predicted final grade based on the submitted student information.

## Technology Stack

- **Python** — Core programming language
- **Pandas** — Data loading and processing
- **Scikit-learn** — Machine learning pipeline and Random Forest Regression
- **Joblib** — Saving and loading the trained model
- **Streamlit** — Interactive web application
- **Unittest** — Automated testing
- **Git and GitHub** — Version control and source code hosting
- **Streamlit Community Cloud** — Application deployment

## Project Structure

```text
Student-Performance-Predictor/
├── app.py
├── main.py
├── test_main.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── student-mat.csv
│   └── student.txt
└── models/
    └── student_performance_model.joblib
```

## Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

- Python 3.11 or a compatible Python version
- Git
- Internet connection for installing dependencies

### 1. Clone the Repository

```bash
git clone https://github.com/ahsanhabibabir04/student-performance-predictor.git
cd student-performance-predictor
```

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv .venv
```

### 3. Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can run the Python commands using the virtual environment's Python executable directly.

### 4. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Train the Model

```powershell
python main.py
```

This runs the training and evaluation workflow and saves the trained model in the `models/` directory.

### 6. Run Automated Tests

```powershell
python -m unittest -v test_main.py
```

The tests cover dataset availability, target validity, feature selection, prediction behavior, and handling of unseen categorical values.

### 7. Launch the Web Application

```powershell
python -m streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## Dataset

This project uses the **UCI Student Performance dataset**, specifically the Mathematics dataset (`student-mat.csv`).

**Dataset source:** [UCI Machine Learning Repository — Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance)

The Mathematics dataset contains 395 student records and includes demographic, social, school-related, and academic information.

Please review the dataset documentation and applicable usage terms before redistributing the data.

## Machine Learning Workflow

1. Load the student dataset.
2. Select the input features and final-grade target.
3. Split the data into training and testing sets using an 80/20 split.
4. Preprocess categorical features using a scikit-learn pipeline.
5. Train a Random Forest Regressor.
6. Evaluate predictions using MAE, RMSE, and R².
7. Save the trained model with Joblib.
8. Load the model into a Streamlit application.
9. Accept student information and display the predicted final grade.
10. Run automated tests to validate important model behaviors.

## Limitations

- The dataset contains only 395 Mathematics student records.
- Evaluation is based on a single 80/20 train/test split.
- The model uses previous grades (`G1` and `G2`), so it is intended for use when those grades are available.
- The model was developed using a specific dataset and may not generalize to other schools, countries, or student populations.
- Predictions are estimates, not guaranteed academic outcomes.
- The model should not be used as the sole basis for academic decisions about students.

## Future Improvements

Potential improvements include:

- Evaluate performance using cross-validation.
- Compare Random Forest with other regression algorithms.
- Add visualizations for model evaluation and feature importance.
- Test generalization on additional student datasets.
- Improve input validation and application usability.
- Add model monitoring and more comprehensive automated tests.

## Author

**M.A. Ahsan Habib Abir**

Machine Learning | Python | Artificial Intelligence

- **GitHub:** [@ahsanhabibabir04](https://github.com/ahsanhabibabir04)
- **LinkedIn:** [M.A. Ahsan Habib Abir](https://www.linkedin.com/in/m-a-ahsan-habib-abir/)

## Disclaimer

This project was developed for educational and portfolio purposes. Its predictions are experimental estimates and should not be interpreted as guaranteed academic results.

---

If you find this project useful, feel free to explore the repository and try the live application.