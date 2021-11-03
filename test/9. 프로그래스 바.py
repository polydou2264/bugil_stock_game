from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start(10)
progressbar.pack()

def btncmd():
    progressbar.stop()

btn = Button(root, text="중지", command=btncmd)
btn.pack()


root.mainloop()