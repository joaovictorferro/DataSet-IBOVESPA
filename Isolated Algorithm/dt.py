# -*- coding: utf-8 -*-
"""DT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    XXXX

# Imports
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import r2_score
import time

from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("XXXX")

"""# Division Train and Test"""

X = df.drop(['Close'],axis=1)
Y = df['Close']

# division Train and Test
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

"""# Model Decision Tree (CART)"""

time_init = time.time()

model = DecisionTreeRegressor(criterion= 'friedman_mse', max_depth = 4)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse_score = mean_squared_error(y_test , y_pred)

evs_score = explained_variance_score(y_test, y_pred)

mae_score = mean_absolute_error(y_test, y_pred)

msle_score = mean_squared_log_error(y_test, y_pred)

r2_s = r2_score(y_test, y_pred)

time_final = time.time()

print("MSE:", mse_score)
print("EVS:", evs_score)
print("MAE:", mae_score)
print("MSLE:", msle_score)
print("r2:", r2_s)
print("Time:", time_final - time_init)
