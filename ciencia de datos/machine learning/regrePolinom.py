
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
#caso 1
#horas
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
#velocidades
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]


myModel = np.poly1d(np.polyfit(x,y,3))

myLine = np.linspace(1,22,150)


speed = myModel(15)
print(speed)
print(r2_score(y, myModel(x)))
plt.scatter(x, y) #grafico de puntos de dispercion 
plt.plot(myLine,myModel(myLine)) #grafica la linea de gregresion polinomial 

plt.show() #muestra el grafico 

# caso 2
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = np.poly1d(np.polyfit(x, y, 3))

myline = np.linspace(2, 95, 100)

print(r2_score(y, mymodel(x)))
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()