import tkinter

def mostrar():
    name = textVar.get()
    msg.configure(text="Hello madafaca " + name)

top = tkinter.Tk()
top.title("Interfaz Mela")
top.minsize(width=500,height=350)

msg = tkinter.Label(top, text="Hola", width=20)
msg.grid(row=0,column=1)

textVar = tkinter.StringVar("")
entrada = tkinter.Entry(top, textvariable=textVar, width=17)
entrada.grid(row=1, column=1)

quitButton = tkinter.Button(top, text="Quit", width=10,command=top.destroy)
quitButton.grid(row=2,column=1)

anotherButton = tkinter.Button(top, text="Acción", width=10, command=mostrar)
anotherButton.grid(row=3,column=1)

tkinter.mainloop()