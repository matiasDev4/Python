from tkinter import *
#Creo la ventana de la calculadora
ventana = Tk()
ventana.title("Calculadora")#Nombre que se muestra en la ventana

#Entrada
i = 0
e_text = Entry(ventana, font = ("Calibri 20"))#Creo la entrada de texto + su tipo de fuente
e_text.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)#Asigno su tamaño en X, Y

#Funcion de los botones
def click_boton(valor):
    global i
    e_text.insert(i, valor)
    i += 1
#Funcion para borrar el texto
def borrar_texto():
    e_text.delete(0, END)
    i = 0
#Funcion de operaciones
def hacer_operacion():
    ecuacion = e_text.get()
    resultado = eval(ecuacion)
    e_text.delete(0, END)
    e_text.insert(0, resultado)
    i = 0
#Botones del 1 al 0
boton1 = Button(ventana, text = "1", width = 5, height = 2, command = lambda: click_boton(1))
boton2 = Button(ventana, text = "2", width = 5, height = 2, command = lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width = 5, height = 2, command = lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 5, height = 2, command = lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 5, height = 2, command = lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 5, height = 2, command = lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 5, height = 2, command = lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 5, height = 2, command = lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 5, height = 2, command = lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 16, height = 2, command = lambda: click_boton(0))
#Botones de operaciones
boton_Sumar = Button(ventana, text = "+", width = 5, height = 2, command = lambda: click_boton("+"))
boton_Restar = Button(ventana, text = "-", width = 5, height = 2, command = lambda: click_boton("-"))
boton_Div= Button(ventana, text = "/", width = 5, height = 2, command = lambda: click_boton("/"))
boton_Mult = Button(ventana, text = "x", width = 5, height = 2, command = lambda: click_boton("*"))
boton_Igual = Button(ventana, text = "=", width = 5, height = 2, command = lambda: hacer_operacion())
boton_Borrar = Button(ventana, text = chr(9003), width = 5, height = 2, command = lambda: borrar_texto())
boton_Parentesis1= Button(ventana, text = "(", width = 5, height = 2, command = lambda: click_boton("("))
boton_Parentesis2 = Button(ventana, text = ")", width = 5, height = 2, command = lambda: click_boton(")"))
boton_Punto = Button(ventana, text = ".", width = 5, height = 2, command = lambda: click_boton("."))
#Mostrar Botones en pantalla
#Fila 1
boton_Parentesis1.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_Parentesis2.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_Punto.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_Borrar.grid(row = 1, column = 3, padx = 5, pady = 5)

#Fila 2
boton9.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton7.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_Sumar.grid(row = 2, column = 3, padx = 5, pady = 5)

#Fila 3
boton6.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton4.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_Restar.grid(row = 3, column = 3, padx = 5, pady = 5)

#Fila 4
boton3.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton1.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_Div.grid(row = 4, column = 3, padx = 5, pady = 5)
#Fila 5
boton0.grid(row = 5, column = 0,columnspan = 2, padx = 5, pady = 5)
boton_Igual.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_Mult.grid(row = 5, column = 3, padx = 5, pady = 5)



ventana.mainloop()#El codigo que permite el funcionamiento de todo lo que se encuentre dentro de el