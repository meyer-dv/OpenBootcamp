"""
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
"""


f = open("archivo.txt", "w")
f.write("Archivo creado\n")
f.close()

f = open("archivo.txt", "a")
f.write("Contenido del archivo")
f.close()

f = open("archivo.txt", "r")
print(f.read())
f.close()
