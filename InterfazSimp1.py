from tabnanny import check
from tkinter import*

ventana = Tk()
ventana.title("Vuelos")


foto = PhotoImage(file="AvionAnimado.png")
Label(ventana, image = foto).pack()


# METODOS
Checkbutton(ventana, text="Playa").pack()
Checkbutton(ventana, text="Montaña").pack()
Checkbutton(ventana, text="Turismo").pack()
chek =Checkbutton(ventana, text="otros")
chek.pack()





ventana.mainloop()
