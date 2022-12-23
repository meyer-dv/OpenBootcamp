peso = float(input("Igresa tu peso en Kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))
indiceMasaCorporal = round(peso * estatura ** 2, 2)

print("Tu índice de masa corporal es", indiceMasaCorporal)
