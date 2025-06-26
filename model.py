import joblib
import pandas as pd
import numpy as np
from pathlib import Path

class TitanicModel:
    def __init__(self, model_path: str):
        self.model = None
        self.model_path = Path(model_path)
        self.load_model()

    def load_model(self) -> None:
        if not self.model_path.exists():
            raise FileNotFoundError(f"El modelo no se encontró en {self.model_path}")
        
        self.model = joblib.load(self.model_path)
        print(f"Modelo cargado desde {self.model_path}")

    def predict(self, data: dict) -> dict:
        df = pd.DataFrame([data])

        df['sex'] = df['sex'].map({'male': 1, 'female': 0})
        df['embarked'] = df['embarked'].map({'S': 2, 'C': 0, 'Q': 1})
        df['alone'] = df['alone'].astype(int)  # Convertir booleano a 0/1

        if 'age' in df and np.isnan(df['age'].values[0]):
            df['age'] = df['age'].fillna(29.699)  # Media de edad del dataset original

        required_columns = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'alone']
        df = df[required_columns]

        prediction = self.model.predict(df)[0]
        
        return {
            'prediction': int(prediction),
            'survived': 'Sí' if prediction == 1 else 'No'
        }