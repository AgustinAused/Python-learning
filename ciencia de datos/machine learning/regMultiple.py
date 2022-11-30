import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model as xd

#tomamos los datos de laa tabla de datos de csv
tablaDeDatos = pd.read_csv('ciencia de datos\machine learning\cars.csv')
#agarrampos las series que necesitamos para predecir
X = tablaDeDatos[['Weight', 'Volume']] #variable iindependiente
y = tablaDeDatos['CO2'] #variable dependiente 

'''utilizmaos la funcion de sklearn de methodo de regresion lineal pra crear un objeto y este tiene un un methodo llamado fit que le debemos ingrtesar la variables dependientes e independientes '''
regr = xd.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2)
peso,cm3 = regr.coef_
print(' el valor dice que si el peso aumenta en 1 kg el co2 aurmenta', peso,'y si aumenta unel volumen del motor un cm3 el co2 aumentta',cm3 )