"""
En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
"""

from tkinter import Tk, StringVar, Radiobutton, Label, mainloop

window = Tk()
window.resizable(width=True, height=False)
window.columnconfigure(0, weight=1)

label = Label(window, text="¿Cuál es tu color favorito?")
label.grid(row=0)

colors = {
    "#fff000",
    "#000fff",
    "#f00000",
    "#008000",
    "#ffffff",
    "#000000",
}

v = StringVar(window)

counter = 1
for i in colors:
    element = Radiobutton(
        window,
        text=f"{i}",
        variable=v,
        value=f"{i}",
        indicatoron=False,
        background="light blue",
        disabledforeground="black",
        activebackground=f"{i}",
        activeforeground=f"{i}",
        width=20,
    )
    element.grid(row=counter)
    counter += 1


mainloop()
