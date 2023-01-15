"""
Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
"""

def leap(year):
    if year % 4 == 0 and year % 100 != 0:
        print(year, "es un año bisiesto")
    elif year % 100 == 0 and year % 400 == 0:
         print(year, "es un año bisiesto")       
    else:
        print(year, "no es un año bisiesto")

year = int(input("Ingresa un año: "))
leap(year)
