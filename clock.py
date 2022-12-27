#Import whole module
from tkinter import *
from tkinter.ttk import *
#strtime to retrieve system time
from time import strftime 
#create tkinter window
root = Tk() 
root.title('Clock') 
#Func to display time on label

def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
#style label widget 
lbl = Label(root, font = ('franklin gothic', 40, 'bold'), 
    background = 'black', 
    foreground = 'white') 
#place clock at the center of tkinter window 
lbl.pack(anchor = 'center') 
time()  
mainloop()