
x=int(input('digite un numero: '))

#faghfasgfoiavgbf
try:
    print(x) #error
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else:
    print("nothing went wrong")
finally:
    print("The 'try except' is finished. go!!")

#hasiofghai[osbfg[aoi]]
if x < 0:
    raise Exception("Sorry, no numbers below zero")


#hasoiudhaoisgdpiuagfpiua


x = 12.00
print(type(x))
if not type(x) is int:
    raise TypeError("Only integers are allowed. the number is {}".format(x))

  