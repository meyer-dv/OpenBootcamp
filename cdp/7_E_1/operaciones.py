"""
En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
"""

def sumar(x: float, y: float) -> float:
    return round(x + y, 2)

def restar(x: float, y: float) -> float:
    return round(x - y, 2)

def multiplicar(x: float, y: float) -> float:
    return round(x * y, 2)

def dividir(x: float, y: float) -> float:
    return round(x / y, 2)