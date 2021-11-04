from tkinter import *
import tkinter
import tkinter.font

global player

root = Tk()
root.title("독보기 주식게임")
root.geometry("570x950+670+20")
root['bg'] = '#404040'



font_1=tkinter.font.Font(family="Black Han Sans", size=26)
font_2=tkinter.font.Font(family="Rix열정도", size=35)
font_3=tkinter.font.Font(family="카카오 Regular", size=16)

#플레이어 지정
def player_1():
    player = "학생1"

def player_2():
    player = "학생2"

def player_3():
    player = "학생3"

def player_4():
    player = "학생4"

def player_5():
    player = "학생5"


def player_window():
    player_=Tk()
    player_.title("주식 매수")
    player_.geometry("570x750+670+60")
    player_['bg'] = '#404040'


    player_num = Label(player_, text="학생")
    player_num.pack()

    
    player_.mainloop()




root.resizable(False, False)

blank_0 = Label(root, text="", width=7, bg="#404040") #위쪽 여백
blank_0.grid(column=0, row=0)
blank_1 = Label(root, text="", width=5, bg="#404040")
blank_1.grid(column=0, row=1)
blank_2 = Label(root, text="", width=5, bg="#404040")
blank_2.grid(column=0, row=2)
blank_3 = Label(root, text="", width=5, bg="#404040")
blank_3.grid(column=0, row=3)
blank_4 = Label(root, text="", width=5, bg="#404040")
blank_4.grid(column=0, row=4)

title = Label(root, text="독보기 주식 게임", fg="orange", font=font_2, bg="#404040")
title.place(x="115",y="5")

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽1 여백
blank_3.grid(row=5, column=0)

btn_p1 = Button(root, text="학생1", width=6, height=1, font=font_1, command=lambda:[player_window(), player_1()])
btn_p1.grid(row=5,column=1)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽2 여백
blank_3.grid(row=5, column=2)

btn_p2 = Button(root, text="학생2", width=6, height=1, font=font_1)
btn_p2.grid(row=5,column=3)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=5, column=4)

btn_p3 = Button(root, text="학생3",  width=6, height=1, font=font_1)
btn_p3.grid(row=5,column=5)



btn_p4 = Button(root, text="학생4",  width=6, height=1, font=font_1)
btn_p4.place(x=130,y=200)

btn_p5 = Button(root, text="학생5", width=6, height=1, font=font_1)
btn_p5.place(x=305, y=200)

btn_setting = Button(root, text="  설정  ", font=font_3)
btn_setting.place(x=480, y=880)









root.mainloop()