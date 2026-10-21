\# Student Performance Predictor



A machine learning project that predicts a student's final Mathematics grade using student information, study habits, absences, and previous grades.



\## Project Overview



This project uses the UCI Student Performance dataset and a Random Forest Regression model to estimate the final grade (`G3`) on a scale of 0–20.



\## Model Performance



Evaluated on a held-out test set:



| Metric | Result |

|---|---:|

| Mean Absolute Error (MAE) | 1.07 |

| Root Mean Squared Error (RMSE) | 1.76 |

| R² Score | 0.849 |

| Training samples | 316 |

| Testing samples | 79 |



These results describe one train/test split and do not guarantee the same performance on other data.



\## Features



The model uses 12 features, including:



\- Student age and school

\- Study time and previous class failures

\- Absences and selected student information

\- First-period grade (`G1`)

\- Second-period grade (`G2`)



The target is the final Mathematics grade (`G3`).



\## Tech Stack



\- Python

\- Pandas

\- Scikit-learn

\- Joblib

\- Streamlit

\- Unittest



\## Project Structure



```text

Student-Performance-Predictor/

├── app.py

├── main.py

├── test\_main.py

├── requirements.txt

├── README.md

├── .gitignore

├── data/

│   └── student-mat.csv

└── models/

&#x20;   └── student\_performance\_model.joblib

```



\## Setup and Usage



\### 1. Clone the repository



```bash

git clone https://github.com/YOUR\_USERNAME/student-performance-predictor.git

cd student-performance-predictor

```



Replace `YOUR\_USERNAME` with your GitHub username.



\### 2. Create and activate a virtual environment



Windows PowerShell:



```powershell

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

```



\### 3. Install dependencies



```powershell

python -m pip install -r requirements.txt

```



\### 4. Train the model



```powershell

python main.py

```



\### 5. Run automated tests



```powershell

python -m unittest -v test\_main.py

```



\### 6. Launch the web app



```powershell

python -m streamlit run app.py

```



\## Dataset



The project uses the UCI Student Performance dataset, specifically the Mathematics dataset (`student-mat.csv`).



Source: https://archive.ics.uci.edu/dataset/320/student+performance



Review the dataset documentation and applicable usage terms before redistribution.



\## Limitations



\- The dataset contains 395 Mathematics student records.

\- The evaluation uses a single 80/20 train/test split.

\- Predictions are estimates, not guaranteed academic outcomes.

\- The model uses previous grades (`G1` and `G2`), so it is intended for prediction after those grades are available.

\- Results may not generalize to other schools or student populations.



\## Author



\*\*M.A. Ahsan Habib Abir\*\*



Machine Learning | Python | Artificial Intelligence



\---



This project was developed for educational and portfolio purposes.



