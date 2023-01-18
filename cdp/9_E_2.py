"""
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""
from functools import reduce

def main():
    lista = [i for i in range(15)]

    lista = list(filter(lambda x: x % 2 != 0, lista))

    print(reduce(lambda x, y: x + y, lista))
    
if __name__ == "__main__":
    main()
