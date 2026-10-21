from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

DATA_PATH = Path("data/student-mat.csv")
MODEL_PATH = Path("models/student_performance_model.joblib")

FEATURES = [
    "school", "sex", "age", "studytime", "failures", "absences",
    "internet", "higher", "goout", "health", "G1", "G2",
]
TARGET = "G3"

def train_model():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH, sep=";")
    X = df[FEATURES]
    y = df[TARGET]

    categorical_features = ["school", "sex", "internet", "higher"]
    numerical_features = [
        feature for feature in FEATURES
        if feature not in categorical_features
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features,
            ),
            ("numerical", "passthrough", numerical_features),
        ]
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "regressor",
                RandomForestRegressor(
                    n_estimators=300,
                    random_state=42,
                    min_samples_leaf=2,
                ),
            ),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        {"model": pipeline, "features": FEATURES, "target": TARGET},
        MODEL_PATH,
    )

    print("=" * 45)
    print("STUDENT PERFORMANCE PREDICTOR")
    print("=" * 45)
    print(f"Dataset rows: {len(df)}")
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    print(f"Features used: {len(FEATURES)}")
    print(f"MAE: {mae:.2f} grade points")
    print(f"RMSE: {rmse:.2f} grade points")
    print(f"R² score: {r2:.3f}")
    print(f"Model saved to: {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
