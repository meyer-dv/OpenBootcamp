"""
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""

from sqlite3 import connect


def main():

    conn = connect("/home/meyer/Code/learning/OpenBootcamp/OpenBootcamp/cdp/database.db")
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO Alumnos VALUES
            (1, "Juan", "de Dios"),
            (2, "Mateo", "Luna"),
            (3, "Marcos", "de Jesús"),
            (4, "Pedro", "Pascacio"),
            (5, "Santiago", "de la Cruz"),
            (6, "Jesús", "de Arimatea"),
            (7, "Morgan", "de las Casas"),
            (8, "Mike", "Castañeda"),
            (9, "Artemis", "del Olimpo");

    """
    )

    alumno = cur.execute("SELECT * FROM Alumnos WHERE nombre='Mike'")
    id, nombre, apellido = alumno.fetchone()

    print(f"ID: {id}\nNombre: {nombre}\nApellido: {apellido}")

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
