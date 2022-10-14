# Exercise: Level 1

# Operators
# Open the python interactive shell and do the following operations. The operands are 3 and 4

import math


print(3 + 4) # addition(+)
print(3 - 4) # subtraction(-)   
print(3 * 4) # multiplication(*)
print(3 % 4) # modulus(%)
print(3 / 4) # division(/)
print(3 ** 4) # exponential(**)
print(3 // 4)  # floor division operator(//)

# Strings
# Write strings on the python interactive shell. The strings are the following

myname = 'Christian'
print(myname)
mylname = 'Chacón'
print(mylname)
mycountry = 'Venezuela'
print(mycountry)
mysentence = 'I am enjoying 30 days of Python'
print(mysentence)

# Datatypes
# Check the data types of the following data

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Christian'))
print(type('Chacón'))
print(type('Venezuela'))

# Exercise 3
# Write an example for different Python data types

myBoolean = True
print(type(myBoolean))
myList =(['Christian', 'Chacón', 'Venezuela'])
print(type(myList))
mytuple = ("Manzanas","Peras","naranjas")
print(type(mytuple))
mySet = {"Manzanas","Peras","naranjas"}
print(type(mySet))
myDict = {"Nombre": "Christian", "Apellido": "Chacón", "País": "Venezuela"}
print(type(myDict))

# Calculando Distancia Euclidiana

x = ((2 - 3) ** 2)
y = ((10 - 8) ** 2)
xy = x + y
dE = math.sqrt(xy)
print(dE)