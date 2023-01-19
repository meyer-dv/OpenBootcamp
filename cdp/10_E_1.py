""""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.
"""

from tkinter import Tk, StringVar, TOP, mainloop
from tkinter.ttk import Radiobutton, Button, Label

# Ventana
window = Tk()
window.title("MEVyer")
window.resizable(width=False, height=False)


# Tkinter string variable
# able to store any string value
v = StringVar(window)

# Diccionario con diferentes opciones
elements = {
    1: "Primer opción",
    2: "Segunda opción",
    3: "Tercer opción",
    4: "Cuarta opción",
}

# Label
def setLabel():
    label.config(text=f"-> {elements[int(v.get())]} <-")


# Radio Buttons
for (value, text) in elements.items():
    Radiobutton(window, text=text, variable=v, command=setLabel, value=value, width=15,).pack(
        side=TOP,
        padx=10,
        pady=5,
    )


# Button on click
def reset(event):
    v.set("")
    label.config(text="-> <-")


# Label
label = Label(text="-> <-")
label.pack(pady=5,)

# Button
button = Button(window, text="Reset")
button.bind("<Button-1>", reset)
button.pack(pady=5,)


mainloop()
