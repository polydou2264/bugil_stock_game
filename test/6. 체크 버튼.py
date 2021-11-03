from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

chkvar = IntVar() #chkvar에 int 형으로 값을 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select()
chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) #0: 체크해체, 1: 체크
    print(chkvar2.get()) #0: 체크해체, 1: 체크


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()