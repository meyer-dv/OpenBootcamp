""""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.
"""

import tkinter as tk


def main():
    elements = {
        "1. Primer opción": "1",
        "2. Segunda opción": "2",
        "3. Tercer opción": "3",
        "4. Cuarta opción": "4",
    }

    window = tk.Tk()
    window.title("OpenBootcamp")
    window.columnconfigure(0, minsize=200)

    # Radio buttons
    selected = tk.StringVar()
    counter = 0
    for (i, j) in elements.items():

        radioButton = tk.Radiobutton(
            window, text=i, value=j, variable=selected, font=("Times New Roman", 12)
        )

        radioButton.grid(row=counter, columnspan=2, sticky="ew", padx=5)

        counter += 1

    # Button
    def reset(event):
        print("Reset")
        selected.set("")

    button = tk.Button(window, text="Reset")
    button.bind("<Button-1>", reset)
    button.grid(row=4)

    window.columnconfigure(0, weight=1)
    window.mainloop()


if __name__ == "__main__":
    main()
