from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Clock')

def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)  

lbl = Label(root, font = ('Digital-7', 70, 'bold'),
			background = 'black',
			foreground = '#42f5e9')

lbl.pack(anchor = 'center')
time()
mainloop()