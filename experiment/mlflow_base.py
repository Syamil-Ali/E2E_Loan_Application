# import basic
import pandas as pd
import numpy as np

# import mlflow
import mlflow
from mlflow import MlflowClient
# from mlflow.models import infer_signature

# # import hyper-parameter tuning tool
# import optuna

# # import compile steps
# from dsteps import data_ingestion as di
# from dsteps import data_transformation as dt
# from dsteps import model_training as mt
# import mlflow_exp as mle


# # model
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import AdaBoostClassifier

# # model validation include cross validation score
# from sklearn.model_selection import cross_val_score
# from sklearn.metrics import classification_report
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import precision_score


# os
import os
# MLFLOW_TRACKING_URI=https://dagshub.com/Syamil-Ali/E2E_Loan_Application.mlflow \
# MLFLOW_TRACKING_USERNAME=Syamil-Ali \
# MLFLOW_TRACKING_PASSWORD=2e6b27e2093c83eacbf6777913b6d087592d1710 \
# python script.py


# specify the mlflow credential
MLFLOW_TRACKING_URI='https://dagshub.com/Syamil-Ali/E2E_Loan_Application.mlflow'
MLFLOW_TRACKING_USERNAME='Syamil-Ali'
MLFLOW_TRACKING_PASSWORD='2e6b27e2093c83eacbf6777913b6d087592d1710'

# It's recommended to define this within the code, because it's project specific (but this works too)
os.environ['MLFLOW_TRACKING_URI'] = MLFLOW_TRACKING_URI

# Recommended to define as environment variables
os.environ['MLFLOW_TRACKING_USERNAME'] = MLFLOW_TRACKING_USERNAME
os.environ['MLFLOW_TRACKING_PASSWORD'] = MLFLOW_TRACKING_PASSWORD

import dagshub
# make a connection to dagshib repo

dagshub.init(repo_owner='Syamil-Ali', repo_name='E2E_Loan_Application', mlflow=True)

#import mlflow
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

#client = MlflowClient(MLFLOW_TRACKING_URI)#tracking_uri = MLFLOW_TRACKING_URI)


mlflow.start_run()
mlflow.log_metric('accuracy', 42)
mlflow.log_param('Param name', 'Value')