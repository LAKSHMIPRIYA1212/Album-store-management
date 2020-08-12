from tkinter import *
import os
from PIL import ImageTk,Image
sroot=Tk()
def first():
	sroot.destroy()
	if __name__ == '__main__':
		import login
		login.vp_start_gui()

sroot.geometry('481x322+429+209')
spath="/home/lakshmi/Documents/welcome.png"
simg=ImageTk.PhotoImage(Image.open(spath))
my=Label(sroot,image=simg)
my.image=simg
my.place(x=0,y=0)
sroot.after(3000,first)
sroot.overrideredirect(1)
sroot.mainloop()