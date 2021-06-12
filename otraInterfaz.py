import tkinter

ventana = tkinter.Tk()
ventana.title("Otra interfaz mela")
ventana.minsize(width=800, height=300)

frame = tkinter.Frame(ventana)
frame.pack()

frame.config(bg="lightblue")

frame.config(width=280, height=120)

label_msg = tkinter.Label(ventana, bg = "lightblue", text="Hello", font=("Helvetica", 14, "bold"))

label_msg.pack()

tkinter.mainloop()
