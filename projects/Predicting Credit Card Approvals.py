# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV

# Load the dataset
cc_apps = pd.read_csv("cc_approvals.data", header=None) 
cc_apps.head()

'''
Task 1.
Summarize the data with describe() on cc_apps and then split the data into cc_apps_train and cc_apps_test.
'''

cc_apps.describe()

cc_apps = cc_apps.drop([11,13], axis=1)  # Features

# Split the data into training and testing sets
cc_apps_train, cc_apps_test = train_test_split(cc_apps, test_size=0.33, random_state=42)

'''
Task 2.
Impute the missing values in the dataset
'''
# Clean cc_apps_train
print(cc_apps_train.head())

# Find the columns with '?'
columns_with_question_mark_train = cc_apps_train.columns[cc_apps_train.apply(lambda col: any(col == '?'))].to_list()

# Display columns with '?'
print(columns_with_question_mark_train)

# Replace the '?' with np.Nan
cc_apps_train_nans_replaced = cc_apps_train.replace('?', np.nan)

# Clean cc_apps_test
print(cc_apps_test.head())

# Find the columns with '?'
columns_with_question_mark_test = cc_apps_test.columns[cc_apps_test.apply(lambda col: any(col == '?'))].to_list()

# Display columns with '?'
print(columns_with_question_mark_test)

# Replace the '?' with np.Nan
cc_apps_test_nans_replaced = cc_apps_test.replace('?', np.nan)

# Impute the missing values with fillna()
cc_apps_train_imputed = cc_apps_train_nans_replaced.fillna(cc_apps_train_nans_replaced.mean())
cc_apps_test_imputed = cc_apps_test_nans_replaced.fillna(cc_apps_test_nans_replaced.mean())

# Find object type
for col in cc_apps_train_imputed.columns:
    if cc_apps_train_imputed[col].dtypes == 'object':
        cc_apps_train_imputed[col] = cc_apps_train_imputed[col].fillna(cc_apps_train_imputed[col].value_counts().index[0])
        cc_apps_test_imputed[col] = cc_apps_test_imputed[col].fillna(cc_apps_test_imputed[col].value_counts().index[0])

  '''
Task 3.
Preprocess the data by encoding the categorical features
'''

cc_apps_train_cat_encoding = pd.get_dummies(cc_apps_train_imputed)
cc_apps_test_cat_encoding = pd.get_dummies(cc_apps_test_imputed)

# Assuming cc_apps_train_cat_encoding and cc_apps_test_cat_encoding are your DataFrames

# Reindex cc_apps_test_cat_encoding with columns from cc_apps_train_cat_encoding
cc_apps_test_cat_encoding = cc_apps_test_cat_encoding.reindex(columns=cc_apps_train_cat_encoding.columns, fill_value=0)

'''
Task 4.
Segregate features and labels for training and testing: X_train, y_train, X_test, and y_test. Then rescale the training and testing features contained in X_train and X_test: rescaledX_train and rescaledX_test
'''

# Assuming cc_apps_train_cat_encoding and cc_apps_test_cat_encoding are defined and contain the necessary data

X_train, y_train = (cc_apps_train_cat_encoding.iloc[:,:-1].values, cc_apps_train_cat_encoding.iloc[:,-1].values)
X_test, y_test = (cc_apps_test_cat_encoding.iloc[:,:-1].values, cc_apps_test_cat_encoding.iloc[:,-1].values)

scaler = MinMaxScaler(feature_range=(0,1))
rescaledX_train = scaler.fit_transform(X_train)
rescaledX_test = scaler.transform(X_test)

'''
Task 5.
Train a logistic regression classifier logreg on (rescaledX_train, y_train) and evaluate on (rescaledX_test, y_test).
'''

logreg = LogisticRegression()
logreg.fit(rescaledX_train,y_train)

y_pred = logreg.predict(rescaledX_test)
print(confusion_matrix(y_test, y_pred))

'''
Task 6.
Perform hyperparameter tuning with a GridSearchCV object: grid_model. Once the grid-search process in completed, extract the best model and the best performance score yielded from grid_model.
'''
tol = [0.01, 0.001, 0.0001]
max_iter = [100, 150, 200]

param_grid = {'tol':tol,'max_iter':max_iter}

grid_model = GridSearchCV(estimator=logreg, param_grid=param_grid, cv=5)

grid_model_result = grid_model.fit(rescaledX_train,y_train)

best_model = grid_model_result.best_estimator_
best_params = grid_model_result.best_params_
best_score = grid_model_result.best_score_
print('Best: %f using %s' % (best_score,best_params))
print('Accuracy of logistic regression classifier: ', best_model.score(rescaledX_test, y_test))
