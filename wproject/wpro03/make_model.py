import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression,Ridge,Lasso,LogisticRegression 
from sklearn.model_selection import GridSearchCV


df = pd.read_csv('data/wine.csv')
data = df[df.columns[:-1]].values
label = df['Species'].values

train_data,test_data,train_label,test_label = \
train_test_split(data,label,random_state=42)

model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

params = {'C' : [0.001,0.01,0.1,1,10,100,1000]}

gs = GridSearchCV(model,params,cv=5, return_train_score=True,n_jobs=-1)

model.fit(train_data,train_label)
best_model = gs.best_estimator_
print('가장 좋은 추정치:', best_model)

joblib.dump(model,'model.joblib')