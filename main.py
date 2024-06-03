import streamlit as st
import joblib
#import mlflow
#import os
import pickle
import pandas as pd


# ------------------ MODEL CACHING

@st.cache_resource
def get_ml_models():

    filename = 'production/PModel/loan_application_model.sav'

    loaded_model = pickle.load(open(filename, 'rb'))
    

    return loaded_model


@st.cache_resource
def get_preprocessing(file_name):
    path = 'production/PPreprocessing/Deployed/'
    preprocessing_file = joblib.load(path + file_name)

    return preprocessing_file




# ------------------ MODEL LOAD

# import preprocessing model and trained model
ml_model = get_ml_models()


# #utils.save_object('artifacts',encoder)
encoder = get_preprocessing('encoder.pkl')
scaler = get_preprocessing('scaler.pkl')




# ------------- cleanup function
# trying to predict
def cleanup(df):

    cat_columns = [column for column in df.columns if df[column].dtype == 'object']
    df[cat_columns] = encoder.transform(df[cat_columns])
    df = scaler.transform(df)

    return df



# ------------------ UI
# 

with st.form("my_form"):

    st.markdown("**Personal Info**")

    # Gender
    gender = st.radio('Gender', 
                        ['Male', 'Female'],
                        horizontal = True)


    # Married
    married = st.radio('Married', 
                        ['Yes', 'No'],
                        horizontal = True)

    # Total Dependents	
    dependents = st.radio('Total Dependents',
                            ['0', '1', '2', '3+'], horizontal=True)



    # Education
    education = st.radio('Graduate?',
                            ['Yes', 'No'], horizontal=True)


    # Self Employed
    self_employed = st.radio('Self Employed?',
                            ['Yes', 'No'], horizontal=True)


    # application income
    income = st.number_input('Monthly Income ($)', min_value=0)


    # co-application income
    coincome = st.number_input('Co Applicant Monthly Income ($)', min_value=0)

    # Loan Amount (1000)
    loan_amount = st.number_input('Loan Amount in thousand ($)', min_value=0)

    # Loan Amount term
    loan_amount_term = st.number_input('Loan Amount Term in month', min_value=0)

    # Credit History
    credit_history = st.radio('Do you have create any loan before?',
                            ['Yes', 'No'], horizontal=True)
    
    
    # Property Area
    property_area = st.radio('Property Area',
                            ['Urban', 'Rural', 'Semiurban'], horizontal=True)


    st.write('---')
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")


if submitted:

    # combine all the result
    user_input = {
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'education': 'Graduate' if education == 'Yes' else 'Not Graduate',
        'Self_Employed': self_employed,
        'ApplicantIncome' : income,
        'CoapplicantIncome': coincome,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_amount_term,
        'Credit_History': 1 if credit_history == 'Yes' else 0,	
        'Property_Area': property_area
    }

    # update to 
    
    user_input_df = pd.DataFrame(user_input, index=[0])

    model_input = cleanup(user_input_df)


    # prediction
    result = ml_model.predict(model_input)

    # update the db
    user_input['Loan_Application_Pred'] = int(result[0])


    #upload_firebase(db, collection_name, user_input)
    #doc_ref.set(user_input)
    
    print(user_input)


    #st.dataframe(user_input_df)
    prediction_convert = ":green[Approved]" if result[0] == 1 else ":red[Not Approved]"
    st.write('')
    st.write('')

    st.markdown(f"Loan Prediction: **{prediction_convert}**")
    #st.write(result[0])




















