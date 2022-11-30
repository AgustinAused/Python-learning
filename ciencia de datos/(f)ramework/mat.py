#imports
import matplotlib.pyplot as plt
import numpy as np

#main program 


xpoints = [1, 6] #crea una matriz unidimencional
ypoints =[3, 10] #crea una matriz unidimencional


x = [1,3,6,8]
y =[4,2,8,1]
#mathplot lineal (con lineas)
plt.plot(xpoints, ypoints)
plt.show()

plt.plot(xpoints, ypoints,'o')
plt.show()



plt.plot(x, y, ls = ":")# lineStyle = ":" or "--"
plt.show()

plt.plot(x, y , marker = 'o', ms = 6, mfc = 'r',mec = 'b') #MarkerSize // MarkerFaceColor // MarkerEdgeColor
plt.show()

plt.plot(y, 'o:r')#fmt('marker|line|color')
plt.show()
x1 = [0, 1, 2, 3]
y1 = [3, 8, 1, 10]
x2 = [0, 1, 2, 3]
y2 = [6, 2, 7, 11]


plt.subplot(1, 2, 1)
plt.plot(y1)
plt.plot(y2)



plt.title("first graph") #titulo del grafico
plt.xlabel("Average Pulse") #titulo del la de x
plt.ylabel("Calorie Burnage") #titulo del la de Y
plt.grid() #cuaudricula en el grafico axis= 'y' or 'x' muestra la lsineas de ese eje


plt.subplot(1, 2, 2)#dos graficos en la misma figura 
plt.title("second graphic") #titulo del grafico
plt.xlabel("Average Pulse") #titulo del la de x
plt.ylabel("Calorie Burnage") #titulo del la de Y
plt.plot(x1, y1, x2, y2)

plt.suptitle("Sports Watch Data")
plt.show()

#mathplot con puntos 
#day one, the agge and speed of 13 cars
xS = [5,7,8,7,2,17,2,9,4,11,12,9,6]
yS = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(xS, yS) #lo grafica con puntos 
#day two, the age and speed of 15 cars:
x = [2,2,8,1,15,8,12,9,7,3,11,4,7,14,12]
y = [100,105,84,105,90,99,90,95,94,100,79,112,91,80,85]
plt.scatter(x, y ,c= 'pink')
plt.show()

#barras 
y = [54,30,53,62]
xa = ['jose', 'arnaldo', 'coca', 'tu mujer']
plt.bar(xa,y )
plt.show()

#hist
x = np.random.normal(170 , 10, 250)
plt.hist(x)
plt.show()

#circlu graphic 
plt.pie(y, labels= xa, startangle = 180, shadow = True)
plt.legend(title = "nombres")
plt.show()