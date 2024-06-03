import os
import datetime
import shutil
import mlflow
import pickle
import joblib


# ------------ PRODUCTION PURPOSE ------------

def model_update(client):

    for model in client.search_registered_models():
        if 'champion' in model.aliases.keys():
            # get model name and version
            model_name = model.name
            version = model.aliases['champion']
            deployment_model = mlflow.pyfunc.load_model(f"models:/{model_name}@champion")
            
            
    # save model to production model
    filename = '../production/PModel/loan_application_model.sav'
    pickle.dump(deployment_model, open(filename, 'wb'))


    return 'Updated'


def load_champion_model(client):

    for model in client.search_registered_models():
        if 'champion' in model.aliases.keys():
            # get model name and version
            model_name = model.name
            version = model.aliases['champion']
            deployment_model = mlflow.pyfunc.load_model(f"models:/{model_name}@champion")
            
    
    return deployment_model, {'Model Name': model_name, 'Version': version}



def load_latest_model(client, model_name, latest_model = True, version = 1):

    if latest_model:

        # get latest_model
        model_metadata = client.get_latest_versions(model_name)
        model_version = model_metadata[0].version

    else:
        model_version = version
        

    
    # load  model
    deployment_model = mlflow.pyfunc.load_model(f"models:/{model_name}/{model_version}")

    return deployment_model, {'Model Name': model_name, 'Version': model_version}

    # things needed: if need latest model, custom model, model name (if it is logistic regression, )




def preprocessing_update(encoder, scaler):


    path = '../production/PPreprocessing/'

    # default_counter
    default_counter = 1


    try:

        # check list of file
        list_version = os.listdir(path + 'Archieved/')

        # date created
        date = datetime.datetime.now().date()



        if len(list_version) == 0:
            # make a new dir
            #os.makedirs(path + f'{default_counter}. {date}', exist_ok=True)
            shutil.move(path + 'Deployed', path + f'Archieved/{default_counter}. {date}')
            
        else:
            counter_version = [int(file.strip('.')[0]) for file in list_version] # get the latest version number
            new_counter = max(counter_version) + 1
            #os.makedirs(path + f'{new_counter}. {date}', exist_ok=True)
            
            
            shutil.move(path + 'Deployed', path + f'Archieved/{new_counter}. {date}')

    except:
        print('moving encoder and scaler got problem')
        pass

    os.makedirs(path + 'Deployed', exist_ok=True)
    joblib.dump(encoder, path+'Deployed/encoder.pkl')
    joblib.dump(scaler, path+'Deployed/scaler.pkl')


    return "Updated"



# do load preprocessing model from archived



