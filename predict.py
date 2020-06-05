import os
import pickle
from sklearn.linear_model import LinearRegression
import sklearn
import pandas as pd
with open("crop_model.pkl",'rb') as model_file:
    alg=pickle.load(model_file)
val=[[year1,year2,year3,year4]
print(alg.predict(pd.DataFrame(val)))
