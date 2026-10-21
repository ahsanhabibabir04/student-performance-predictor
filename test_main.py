
import unittest
from pathlib import Path

import joblib
import pandas as pd

from main import FEATURES, TARGET, DATA_PATH

MODEL_PATH = Path("models/student_performance_model.joblib")


class TestStudentPerformancePredictor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        saved = joblib.load(MODEL_PATH)
        cls.model = saved["model"]

    def test_dataset_exists(self):
        self.assertTrue(DATA_PATH.exists())

    def test_dataset_has_target(self):
        df = pd.read_csv(DATA_PATH, sep=";")
        self.assertIn(TARGET, df.columns)
        self.assertEqual(df[TARGET].min(), 0)
        self.assertEqual(df[TARGET].max(), 20)

    def test_feature_selection(self):
        self.assertEqual(len(FEATURES), 12)
        self.assertNotIn(TARGET, FEATURES)

    def test_prediction_is_valid(self):
        student = pd.DataFrame([{
            "school": "GP",
            "sex": "F",
            "age": 17,
            "studytime": 2,
            "failures": 0,
            "absences": 2,
            "internet": "yes",
            "higher": "yes",
            "goout": 3,
            "health": 3,
            "G1": 10,
            "G2": 11,
        }])

        prediction = self.model.predict(student)

        self.assertEqual(len(prediction), 1)
        self.assertTrue(pd.notna(prediction[0]))
        self.assertGreaterEqual(prediction[0], 0)
        self.assertLessEqual(prediction[0], 20)

    def test_unseen_category(self):
        student = pd.DataFrame([{
            "school": "UNKNOWN",
            "sex": "F",
            "age": 17,
            "studytime": 2,
            "failures": 0,
            "absences": 0,
            "internet": "yes",
            "higher": "yes",
            "goout": 3,
            "health": 3,
            "G1": 10,
            "G2": 10,
        }])

        prediction = self.model.predict(student)
        self.assertEqual(len(prediction), 1)
        self.assertTrue(pd.notna(prediction[0]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
