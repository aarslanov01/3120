# Import required modules
import pandas as pd
import numpy as np
from statsmodels.formula.api import logit

# task 1
car_insurance = pd.read_csv('car_insurance.csv')

car_insurance['credit_score'].fillna(car_insurance['credit_score'].mean(),inplace = True)
car_insurance['annual_mileage'].fillna(car_insurance['annual_mileage'].mean(),inplace = True)

models = []

car_insurance.head()
features = car_insurance.drop(columns = ['id','outcome']).columns
features

for col in features:
    model = logit(f'outcome ~ {col}', data=car_insurance).fit()
    models.append(model)
    
accuracies = []

for feature in range(0,len(models)):
    conf_matrix = models[feature].pred_table()
    tn = conf_matrix[0,0]
    tp = conf_matrix[0,0]
    fp = conf_matrix[1,0]
    fn = conf_matrix[0,1]
    acc = (tn + tp) / (tn+tp+fn+fp)
    accuracies.append(acc)
    
best_feature = features[accuracies.index(max(accuracies))]
best_feature_df = pd.DataFrame({'best_feature': best_feature,
                               'best_accuracy': max(accuracies)},
                              index=[0])
best_feature_df
