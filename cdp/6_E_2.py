"""
En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""


class Alumno:
    nombre = str()
    nota = float()

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def getNombre(self) -> str:
        return self.nombre

    def getNota(self) -> float:
        return self.nota

    def __str__(self):
        aprueba = "aprobó" if self.getNota() > 5 else "no aprobó"
        return (
            f"El estudiante {self.getNombre()} {aprueba} con su calificación de {self.getNota()}."
        )


juan = Alumno("Juan Diego", 6)

print(juan)
