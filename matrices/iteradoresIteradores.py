
tupla = (1,4,2,3,5,6,2,68)
conjunto = {"hola", 4,True,"roto", 2,5,1}

myit = iter(tupla) # convierte el objeto en iterrable 
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

palabra = "hola mundo"
miIt=iter(palabra)
print(next(miIt))
print(next(miIt))
print(next(miIt))
print(next(miIt))
print(next(miIt))
print(next(miIt))
print(next(miIt))
print(next(miIt))
print(next(miIt))
print(next(miIt)) 

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


