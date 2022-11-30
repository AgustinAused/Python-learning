

from math import cos
import scipy.optimize as spo
import scipy as sp



#encontrar la raiz de una ecuacion
def eqn(x):
  return x + cos(x)

myroot = spo.root(eqn, 0)

print(myroot.x)

# encontrar el minimo 
def eqn(x):
  return x**2 + x + 2

mymin = spo.minimize(eqn, 0, method='BFGS')

print(mymin)