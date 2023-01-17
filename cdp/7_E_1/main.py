from random import randint
from operaciones import *


def main():
    x = randint(-50, 100)
    y = randint(1, 200)

    print(f"{x} + {y} = {sumar(x, y)}")
    print(f"{x} - {y} = {restar(x, y)}")
    print(f"{x} * {y} = {multiplicar(x, y)}")
    print(f"{x} / {y} = {dividir(x, y)}")


if __name__ == "__main__":
    main()
