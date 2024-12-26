# from sklearn.ensemble import RandomForestClassifier
# import pandas as pd
# from pandas import DataFrame
# import joblib
# from datetime import datetime
# from sklearn.model_selection import train_test_split


# class Machine:

#     def __init__(self, df: DataFrame):
#         self.name = "Random Forest Classifier"

#         if df.empty:
#             raise ValueError("The Dataframe is empty")

#         # Split into Feature and Target

#         if 'Rarity' not in df.columns:
#             raise ValueError("The Column Rarity does not exists")

#         X = df.drop(columns=['Rarity'])
#         y = df['Rarity']

#         # Train test split
#         self._train, self.y_train, self.X_test, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#         # Instantiate and fit the model
#         self.model = RandomForestClassifier(random_state=42, n_estimators=100, max_depth=10)
#         self.model.fit(self.X_train, self.y_train)
#         self.accuracy = self.model.score(self.X_test, self.y_test)

#     def predict(self, feature_basis: DataFrame):
#         """Calling the Predictive Model to predict our features"""
#         if feature_basis.empty:
#             raise ValueError('The dataframe is empty')

#         prediction = self.model.predict(feature_basis)
#         confidence = self.model.predict_proba(feature_basis)

#         return prediction, confidence


#     def save(self, filepath: str):
#         """Save The Machine Learning Model"""

#         joblib.dump(self, filepath)


    @staticmethod
    def open(filepath: str):
        """Load the Machine Learning Model"""

        return joblib.load(filepath)



    def info(self) -> dict:
        """Print information about the Machine Learning Model"""

        return {
            "model_type": type(self.model).__name__,
            "Features": self.model.feature_names_in_.tolist(),
        }