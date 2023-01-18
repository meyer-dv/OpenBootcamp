"""
Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
"""


def main():
    listaPaises = input("Ingresa una lista de países separados por coma: ").split(",")
    listaPaises = set(listaPaises)
    listaPaises = list(listaPaises)
    listaPaises.sort(reverse=True)

    lista = list()

    for i in listaPaises:
        lista.append(i)

    print(", ".join(lista))


if __name__ == "__main__":
    main()
