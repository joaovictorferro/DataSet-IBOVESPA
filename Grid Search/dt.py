# -*- coding: utf-8 -*-
"""DT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DgtKF7w64o9f-NoW_6-L8zIcLtyXvv39

# Imports
"""

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor

import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/joaovictorferro/DataSet-IBOVESPA/main/DataSet_IBOVESPA_Norma.csv")

"""# Division Train and Test"""

X = df.drop(['Close'],axis=1)
Y = df['Close']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

"""# DT"""

params = {
    'criterion': ['squared_error',  'friedman_mse', 'absolute_error', 'poisson'],
    'splitter': ['best', 'random'],
    'random_state': [42],
}

grid_search = GridSearchCV(estimator=DecisionTreeRegressor(), param_grid=params, cv=5, verbose=0)

grid_search.fit(X_train, y_train)

print("best hyperparameters:", grid.best_params_)