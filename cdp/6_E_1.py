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
    def __init__(self, color: str, ruedas: int, puertas: int) -> None:
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return f"Este objeto es un {self.__class__} de color {self.color}, con {self.ruedas} ruedas y {self.puertas} puertas.\n"


class Coche(Vehiculo):
    def __init__(
        self, color: str, ruedas: int, puertas: int, velocidad: float, cilindrada: int
    ) -> None:
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self) -> str:
        return (
            super().__str__()
            + f"Adicionalmente tiene una velocidad máxima de {self.velocidad} km/h y su cilindrada es de {self.cilindrada} litros."
        )


miCarro = Coche("Rojo", 4, 2, 100, 2)

print(miCarro)
