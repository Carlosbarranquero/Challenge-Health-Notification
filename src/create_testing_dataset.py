import pandas as pd
import os
import json
import numpy as np

from create_training_dataset import create_dataset


os.chdir(".")

def transform_track_category_to_binary(raw_dataset_testing):

    track_dict = {"Development" : 0,
                  "Data Science" : 1,
                  "Quality Assurance" : 2,
                  "Design" : 3}
    
    trac_one_hot = np.zeros((raw_dataset_testing.shape[0], 4))
            
    track_binary = pd.DataFrame(trac_one_hot, columns=["Development" ,"Data Science" ,"Quality Assurance","Design" ])
    
    for i in range(raw_dataset_testing.shape[0]):
                   
        track_binary.iloc[i, track_dict[raw_dataset_testing['track'][i]]] = 1
        
    return track_binary
     

def transform_createdBy_category_to_binary(raw_dataset_testing):
     
    track_dict = {"high_freq_createdBy" : 0,
                  "low_freq_createdBy" : 1,
                  "medium_freq_createdBy" : 2}
    
    trac_one_hot = np.zeros((raw_dataset_testing.shape[0], 3))
            
    createdBy_binary = pd.DataFrame(trac_one_hot, columns=["high_freq_createdBy" ,"low_freq_createdBy Science" ,"medium_freq_createdBy"])
    
    for i in range(raw_dataset_testing.shape[0]):
                   
        createdBy_binary.iloc[i, track_dict[raw_dataset_testing['createdBy'][i]]] = 1
        
    return createdBy_binary
     
     
# main

raw_dataset_testing = create_dataset("../data/test/json")

with open('../data/aux_data/dic_createdBy.json', 'r') as f:
    
     createdBy_dic = json.load(f)

name = raw_dataset_testing["name"]

raw_dataset_testing["createdBy"] = raw_dataset_testing["createdBy"].apply(lambda x: createdBy_dic[x])

raw_dataset_testing['type'] = raw_dataset_testing['type'].apply(lambda x: 0 if x == 'First2Finish' else 1 )

legal_id = raw_dataset_testing["legacyId"]
day_of_year = raw_dataset_testing["day_of_year"]

raw_dataset_testing = raw_dataset_testing.drop(['day_of_year', 'legacyId', 'updatedBy' ], axis = 1)

track_one_hot_encoding = transform_track_category_to_binary(raw_dataset_testing)

createdBy_one_hot_encoding = transform_createdBy_category_to_binary(raw_dataset_testing)
    

testing_dataset = pd.concat([raw_dataset_testing["name"],
                             raw_dataset_testing["type"], 
                             track_one_hot_encoding,
                             raw_dataset_testing["challenge_duration"],
                             createdBy_one_hot_encoding,
                             raw_dataset_testing["challenge_prize"]],axis=1)

testing_dataset.to_csv("../data/test/csv/test_dataset.csv", index=False)


testing_dataset_classification = pd.concat([raw_dataset_testing["name"],
                                   raw_dataset_testing["type"],
                                   legal_id, 
                                   track_one_hot_encoding,
                                   raw_dataset_testing["challenge_duration"],
                                   createdBy_one_hot_encoding,
                                   day_of_year,                                  
                                   raw_dataset_testing["challenge_prize"]],axis=1)

    
testing_dataset_classification.to_csv("../data/test/csv/test_dataset_classification.csv", index=False)



    













    
        

























