"""
En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
"""
from os.path import exists
from pickle import dump, load


class Vehiculo:
    def __init__(self, color: str, placa: str):
        self.color = color
        self.placa = placa

    def encender(self):
        print("Vehículo encendido")

    def apagar(self):
        print("Vehículo apagado")

    def getColor(self):
        return self.color

    def __str__(self):
        return f"Este vehículo es de color {self.getColor()} y tiene la placa con el serial '{self.placa}'."


if not exists("carro.bin"):

    carro = Vehiculo("Rojo", "210-SFA")

    f = open("carro.bin", "wb")
    dump(carro, f)
    f.close()

f = open("carro.bin", "rb")
carro = load(f)
f.close()

carro.encender()
print(carro)
carro.apagar()
