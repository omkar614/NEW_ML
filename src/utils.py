import os
import sys

import pandas as pd
import numpy  as np
from sklearn.model_selection import GridSearchCV

from src.exception import CustomeException
import dill
from sklearn.metrics  import r2_score
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomeException(e,sys)
    
    
from sklearn.metrics import r2_score

def evaluate_models(X_train, y_train, X_test, y_test, models):
    """
    Trains and evaluates multiple models using R² score on test data.
    
    Parameters:
    - X_train, y_train: Training features and target
    - X_test, y_test: Testing features and target
    - models: Dictionary of model name → model instance
    
    Returns:
    - report: Dictionary of model name → test R² score
    """
    try:
        report = {}

        for model_name, model in models.items():
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score
            # Optional: print individual scores
            # print(f"{model_name}: Train R2={train_model_score:.3f}, Test R2={test_model_score:.3f}")

        return report

    except Exception as e:
        raise CustomeException(e, sys)