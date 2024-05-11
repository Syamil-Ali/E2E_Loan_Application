import os
import datetime
import shutil

def preprocessing_handle(path):

    # default_counter
    default_counter = 1

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

    return "Updated"





