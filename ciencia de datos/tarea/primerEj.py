#imports 
import numpy as np
#functions



#main program


data = np.array([120000,125000, 150000,160000, 200000, 230000, 320000, 540000,  280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

sd = np.std(data)
casas = data[data > sd]
print(casas)

div= len(casas) / len(data)
des = div*100
print(des)
