import tkinter as tk

window = tk.Tk()

window.columnconfigure(0, minsize=50)
window.rowconfigure([0, 1], minsize=50)

label1 = tk.Label(text="100", bg="black", fg="white")
label2 = tk.Label(text="0", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0, sticky="nsew")

window.mainloop()

from leitor import Leitor

leitor = Leitor("COM2", 9600, 2)

leitor.exec(100)