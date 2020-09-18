import pandas as pd
import create_testing_dataset
from approximation_model_5n import expression
from classification_model import expression_classification

#Approximation

testing_dataset = pd.read_csv("../data/test/csv/test_dataset.csv")

name = testing_dataset['name']

test_data = testing_dataset.drop(columns=['name'], axis = 1)

output=[]

for i in range(test_data.shape[0]):
    
    inputs = list(test_data.iloc[i,:])
    
    if expression(inputs) < 0:
        
        output.append(0)
    else:
        output.append(expression(inputs))
    

o = pd.DataFrame(output, columns=["output"] )
                 
result1 = pd.concat([o, name], axis=1)

result1.to_csv("../doc/results_approximation.csv",index=False)

# Classification

testing_dataset = pd.read_csv("../data/test/csv/test_dataset_classification.csv")

name = testing_dataset['name']

test_data = testing_dataset.drop(columns=['name'], axis = 1)

output=[]

for i in range(test_data.shape[0]):
    
    inputs = list(test_data.iloc[i,:])
    
    if expression_classification(inputs) < 0:
        
        output.append(0)
    else:
        output.append(expression_classification(inputs))
    


o = pd.DataFrame(output, columns=["output"] )
                 
result = pd.concat([o, name], axis=1)

result.to_csv("../doc/test_dataset_classification.csv",index=False)




