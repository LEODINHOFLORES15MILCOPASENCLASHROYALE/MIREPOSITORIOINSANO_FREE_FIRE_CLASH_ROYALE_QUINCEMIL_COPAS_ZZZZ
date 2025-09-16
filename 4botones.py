from tkinter import*
from tkinter.ttk import*

def circular():
    ventana_2=Tk()
    ventana_2.title("Circulo")
    ventana_2.geometry("400x450")
    etiqueta=Label(ventana_2, text="Ingresa el area")
    etiqueta.pack(pady=5)
    radio=Entry(ventana_2)
    radio.pack(pady=5)
    ventana_2.mainloop()

def cuadrado():
    ventana_2=Tk()
    ventana_2.title("cuadrado")
    ventana_2.geometry("400x450")
    etiqueta=Label(ventana_2, text="Ingresa el area")
    etiqueta.pack(pady=5)
    radio=Entry(ventana_2)
    radio.pack(pady=5)
    ventana_2.mainloop()

def triangulo():
    ventana_2=Tk()
    ventana_2.title("triangulo")
    ventana_2.geometry("400x450")
    etiqueta=Label(ventana_2, text="Ingresa el area")
    etiqueta.pack(pady=5)
    radio=Entry(ventana_2)
    radio.pack(pady=5)
    ventana_2.mainloop()

def rectangulo():
    ventana_2=Tk()
    ventana_2.title("rectangulo")
    ventana_2.geometry("400x450")
    etiqueta=Label(ventana_2, text="Ingresa el area")
    etiqueta.pack(pady=5)
    radio=Entry(ventana_2)
    radio.pack(pady=5)
    ventana_2.mainloop()

def freefire():
    ventana_2=Tk()
    ventana_2.title("DIAMANTES GRATIS")
    ventana_2.geometry("400x450")
    etiqueta=Label(ventana_2, text="Ingresa cantidad de diamantes en tu cuenta")
    etiqueta.pack(pady=5)
    diamantes=Entry(ventana_2)
    diamantes.pack(pady=5)
    etiqueta2=Label(ventana_2, text="Ingresa cantidad de diamantes que quieres tener en tu cuenta")
    etiqueta2.pack(pady=5)
    diamantesquieres=Entry(ventana_2)
    diamantesquieres.pack(pady=5)
    etiqueta3=Label(ventana_2, text="Ingrese gmail, vinculado a su cuenta de free fire")
    etiqueta3.pack(pady=5)
    gmail=Entry(ventana_2)
    gmail.pack(pady=5)
    etiqueta4=Label(ventana_2, text="Ingrese contraseña")
    etiqueta4.pack(pady=5)
    contra=Entry(ventana_2)
    contra.pack(pady=5)
    etiqueta5=Label(ventana_2, text="Ingrese numero de tarjeta")
    etiqueta5.pack(pady=5)
    tarjeta=Entry(ventana_2)
    tarjeta.pack(pady=5)
    etiqueta6=Label(ventana_2, text="Ingrese datos del titular")
    etiqueta6.pack(pady=5)
    datos=Entry(ventana_2)
    datos.pack(pady=5)
    etiqueta7=Label(ventana_2, text="Ingrese fecha de vencimiento")
    etiqueta7.pack(pady=5)
    vencimiento=Entry(ventana_2)
    vencimiento.pack(pady=5)
    etiqueta8=Label(ventana_2, text="Ingrese numero de seguridad, los 3 digitos")
    etiqueta8.pack(pady=5)
    codigo=Entry(ventana_2)
    codigo.pack(pady=5)
    etiqueta9=Label(ventana_2, text="Ingrese numero de DNI")
    etiqueta9.pack(pady=5)
    dni=Entry(ventana_2)
    dni.pack(pady=5)
    boton_1=Button(ventana_2,text="enviar")
    boton_1.pack(pady=5)

    ventana_2.mainloop()    


ventana=Tk()
ventana.title("Figuras geometricas")
ventana.geometry("400x450")

boton_1=Button(ventana,text="Circulo",command=circular)
boton_1.pack(pady=5)

boton_2=Button(ventana,text="Cuadrad", command=cuadrado)
boton_2.pack(pady=5)

boton_3=Button(ventana,text="Triangulo",command=triangulo)
boton_3.pack(pady=5)

boton_4=Button(ventana,text="Rectangulo",command=rectangulo)
boton_4.pack(pady=5)

boton_5=Button(ventana,text="Salir y jugar free fire",command=freefire)
boton_5.pack(pady=5)

ventana.mainloop()