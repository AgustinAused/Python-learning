


myset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset = set(("apple", "banana", "cherry")) 
print(thisset)
print(type(myset))  #typo de dato

#acceder 
for x in thisset:
  print(x)

print("banana" in thisset)

#agregar a un set
thisset.add("orange")

# agregar un set 
thisset.update(tropical)  #podes agregar cualquier iterable 
print(thisset)
#eliminar un elemento genera un error si no existe
thisset.remove("banana")
print(thisset)
#eliminar un elemento. no genera un error si no existe
thisset.discard("agua")
#limpiar el set
thisset.clear()
#elimina el set por completo 
del thisset
#unir set 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #unis ambos en un nuevo set 
print(set3)
set1.update(set2) #actualizas el set para unir 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) #
x.intersection_update(y) #conserva los duplicados 
print(x)
print(z)


#Conservar todo, pero NO los duplicados
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
x.symmetric_difference_update(y)
print(z)
print(x)