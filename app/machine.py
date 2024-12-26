from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from pandas import DataFrame
import joblib
from datetime import datetime


class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"

        if df.empty:
            raise ValueError("The Dataframe is empty")

        # Split into Feature and Target

        if 'Rarity' not in df.columns:
            raise ValueError("The Column Rarity does not exists")

        X = df.drop(columns=['Rarity'])
        y = df['Rarity']

        self.timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')


        # Instantiate and fit the model
        self.model = RandomForestClassifier(random_state=42, n_jobs=-1, n_estimators=100, max_depth=10)
        self.model.fit(X, y)

    def __call__(self, feature_basis: DataFrame):
        """Calling the Predictive Model to predict our features"""
        # if feature_basis.empty:
        #     raise ValueError('The dataframe is empty')

        prediction, *_ = self.model.predict(feature_basis)
        confidence, *_ = self.model.predict_proba(feature_basis)

        return prediction, max(confidence)


    def save(self, filepath: str):
        """Save The Machine Learning Model"""

        joblib.dump(self.model, filepath)


    @staticmethod
    def open(filepath: str):
        """Load the Machine Learning Model"""

        return joblib.load(filepath)



    def info(self) -> str:
        """Print information about the Machine Learning Model"""

        return f'model_type: {self.name} timestamp: {self.timestamp}'
