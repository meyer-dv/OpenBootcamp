"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
"""

import time

def main():
    
    if time.localtime().tm_hour > 19:
        print("Es hora de ir a casa")
    else:
        print(f"Te quedan {19 - time.localtime().tm_hour} horas de trabajo")

if __name__ == '__main__':
    main()