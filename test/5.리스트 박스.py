from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(2, "딸기")
listbox.insert(3, "포도")
listbox.insert(END, "김치")
listbox.pack()

def btncmd():
    #listbox.delete(END)
    print("리스트에는", listbox.size(), "개가 있어요")

    #항목확인
    print("1번쨰부터 3번짜까지의 황목: ", listbox.get(0,2))

    print("선택된 항목: ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()


