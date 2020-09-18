import pandas as pd
import glob, os
import json

def get_json_atributes(json):

    track = json['track']
    
    type_ = json['type']
    
    legacyId = json['legacyId']
    
    duration = (pd.to_datetime(json['endDate']) - pd.to_datetime(json['startDate'])).dt.days.abs()
    
    day_of_year = pd.to_datetime(json['created']).dt.dayofyear
    
    autor = json['createdBy']
    
    update = json['updatedBy']
    
    prize_obj = json['prizeSets']
    
    name = json['name']
    
    #challenge_price
    
    all_prizes=[]
    
    for value in prize_obj:
        
        list_prizes=[]
        
        list_prizes.append(value[0]['prizes'])
        
        all_prizes.append(list_prizes)
        
    challenge_prize=[]
    
    for prizes in all_prizes:
        
        suma = 0
        
        for p in prizes[0]:
            
            suma += p["value"] 
            
        challenge_prize.append(suma)
        
    challenge_prize = pd.DataFrame(challenge_prize, columns=['challenge_prize'])
    
    # target = json["numOfSubmissions"].apply(lambda x: 1 if x > 0 else x)
    
    target = json["numOfSubmissions"]
    
    new_data = pd.concat([name, type_,legacyId, track, duration, autor, update, day_of_year, challenge_prize, target], axis=1)
    
    new_data.columns = ['name', 'type', 'legacyId', 'track', 'challenge_duration', 'createdBy',
       'updatedBy', 'day_of_year', 'challenge_prize', 'numOfSubmissions']
    
    return new_data


def create_dataset(path):    

    dataset= pd.DataFrame()
    
    for file in glob.glob( path + "/" + "*.json"):
        
        json = pd.read_json(str(file))
        
        json = get_json_atributes(json)
        
        dataset = pd.concat([dataset,json],axis=0)
        
    return dataset


def prepare_dataset(raw_dataset):
    
    raw_dataset['type'] = raw_dataset['type'].apply(lambda x: 0 if x == 'First2Finish' else 1 )

    d1 = create_cluster_dictionary(raw_dataset, "createdBy")

    d2 = create_cluster_dictionary(raw_dataset, "updatedBy")

    raw_dataset["createdBy"] = raw_dataset["createdBy"].apply(lambda x: d1[x])

    raw_dataset["updatedBy"] = raw_dataset["updatedBy"].apply(lambda x: d2[x])
    
    with open('../data/aux_data/dic_createdBy.json', 'w') as fp:
        json.dump(d1, fp)
        
    with open('../data/aux_data/dic_updatedBy.json', 'w') as fp:
        json.dump(d2, fp)
        
    raw_dataset.drop(['name','day_of_year', 'legacyId', 'updatedBy' ], axis=1)
    
    return raw_dataset


    
def create_cluster_dictionary(dataset, variable):
    
    freq_created = dataset[variable].value_counts()
    
    d = {}
    
    for counter, value in enumerate(freq_created):
        
        if(value<freq_created.median()):
            
            d[freq_created.index[counter]] = "low_freq_" + variable
            
        elif(value>=freq_created.median() and value<100):
            
            d[freq_created.index[counter]] = "medium_freq_" + variable
        
        elif(value>=100):
            
            d[freq_created.index[counter]] = "high_freq_" + variable
            
        else:
            print(value)
    
    return d

        
os.chdir(".")

#Regression

raw_dataset = create_dataset("../data/train/json")

clean_dataset = prepare_dataset(raw_dataset)

clean_dataset = clean_dataset.drop(['name'], axis=1)

clean_dataset.to_csv("../data/train/csv/training_regression.csv", index=False)

clean_dataset['numOfSubmissions'] = clean_dataset['numOfSubmissions'].apply(lambda x: 0 if x == 0  else 1 )

clean_dataset.to_csv("../data/train/csv/training_classification.csv", index=False)





