import time
from tkinter import Label
from tkinter import *
def time_current():
    a = time.strftime("%I:%M:%S %p")
    time_display.config(text = a)
    time_display.after(200,time_current)
tk_window=Tk()
tk_window.title("DIGI CLOCK BY HARDIK RASTOGI")
time_display = Label(tk_window , font =("Arial",145,"bold","italic"),bg = "Light yellow" , fg = "black")
time_display.pack()
time_current()
tk_window.mainloop()


