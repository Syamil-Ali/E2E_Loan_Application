import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split



def cleaning_train_pipeline(df):

    try:

        # 1. drop id column
        df.drop(columns = 'Loan_ID', inplace= True)


        # 2. drop duplicate
        df.drop_duplicates(inplace=True)

        # Handling Missing Value Part
        # 3. drop missing val
        df.dropna(inplace=True)


        # 3. classify num and cat columns
        cat_columns = [column for column in df.columns if df[column].dtype == 'object']
        num_columns = [column for column in df.columns if df[column].dtype != 'object']

        cat_columns.remove('Loan_Status')

        # 4. split to training and testing set

        X = df.drop(columns = 'Loan_Status').copy()
        y = df['Loan_Status'].copy()
                
        X_train, X_test, y_train, y_test = train_test_split(X,y, 
                                            random_state=42,  
                                            test_size=0.1,
                                            shuffle=True)


        # Encoding and Scaling Part
        # 5. encoder

        encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
        encoder.fit(X_train[cat_columns])

        X_train[cat_columns] = encoder.transform(X_train[cat_columns])    
        X_test[cat_columns] = encoder.transform(X_test[cat_columns])


        # 6. scale

        scaler = StandardScaler()
        scaler.fit(X_train)

        X_train= scaler.transform(X_train)
        X_test= scaler.transform(X_test)

        
        return X_train, y_train, X_test, y_test


    except:
        return 'Error'

