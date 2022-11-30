import numpy as np
import pandas as pd
from sklearn import linear_model as xd
from sklearn.preprocessing import StandardScaler

#le asignamos a scale el methodo del modullo sklearn
scale = StandardScaler()


#obterncionn de datos de una tabla csv 
tabla = pd.read_csv("ciencia de datos\machine learning\cars2.csv")

X = tabla[['Weight', 'Volume']] #variable independiente
y = tabla ['CO2']

scaleX = scale.fit_transform(X)
print(scaleX)

regr = xd.LinearRegression()
regr.fit(scaleX,y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)