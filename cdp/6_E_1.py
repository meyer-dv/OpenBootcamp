"""
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
- Color
- Ruedas
- Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
- Velocidad
- Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
"""

class Vehiculo:
    color = 'rojo'
    ruedas = 4
    puertas = 2

    def __str__(self):
        return f'Este objeto es un {self.__class__} de color {self.color}, con {self.ruedas} ruedas y {self.puertas} puertas.\n'

class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 2

    def __str__(self) -> str:
        return super().__str__() + f'Adicionalmente tiene una velocidad máxima de {self.velocidad} km/h y su cilindrada es de {self.cilindrada} litros.'

miCarro = Coche()

print(miCarro)
