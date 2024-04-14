import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from utils.logger import logging
from mlflow.models import infer_signature
import optuna
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


# define evaluation metrics
def evaluation_metrics(y_test, y_pred):

    report = classification_report(y_test, y_pred, output_dict=True)
    sample_classification = pd.DataFrame(report).transpose()

    return sample_classification



# model training
def train_model(model_ex, X_train, y_train, X_test, y_test, params:dict):

    # run logistic regression model
    model = model_ex.set_params(**params)
    model.fit(X_train, y_train)

    score_train = model.score(X_train, y_train)
    score_valid = model.score(X_test, y_test)


    # trying to get the signature 
    # -> (responsible to save the schema of model input and output)
    predictions = model.predict(X_test)
    signature = infer_signature(X_test, predictions)
    
    
    return model, score_train, score_valid, signature

