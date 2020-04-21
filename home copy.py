from subprocess import call
from tkinter import *
from tkinter import ttk

def multi_reg():
    call(["python", "multi_reg.py"])


root = Tk()

content = ttk.Frame(root, padding=(5, 5, 5, 5))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=200)
label_name = ttk.Label(content, text="Prototype")

ok = ttk.Button(content, text="Enter")
cancel = ttk.Button(content, text="Exit")

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=4, sticky=(N, S, E, W))
label_name.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)

ok.grid(column=3, row=3)
ok.configure(command=multi_reg)

cancel.grid(column=4, row=3)
cancel.configure(command=quit)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()
