from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

btn1 = Button(root, text="버튼")
btn1.pack()

btn2 = Button(root, padx=5, pady= 10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady= 5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="img.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 눌렸습니다.")

btn7 = Button(root, text="버튼", command=btncmd)
btn7.pack()




root.mainloop()


