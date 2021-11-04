from tkinter import *
import tkinter
import tkinter.font

global player

root = tkinter.Tk()
root.title("독보기 주식게임")
root.geometry("570x950+670+20")
root.iconbitmap('money.ico')
root['bg'] = '#404040'

font_1=tkinter.font.Font(family="Black Han Sans", size=26)
font_2=tkinter.font.Font(family="Rix열정도", size=35)
font_3=tkinter.font.Font(family="카카오 Regular", size=16)

#command=lambda:[player_window(), player_1()] <-- 함수 여러개 사용

#플레이어 지정
def player_1():
    player = "1"
    player_=Tk()
    player_.title("주식 매수")
    player_.geometry("570x750+670+60")
    player_.iconbitmap('money.ico')
    player_['bg'] = '#404040'

    blank_p = Label(player_, text="", width=5, bg="#404040")
    blank_p.pack()

    font_p = tkinter.font.Font(player_, family="Rix열정도", size=23)
    player_num = Label(player_, text="학생1", fg="orange", font=tkinter.font.Font(player_, family="Rix열정도", size=31), bg="#404040")
    player_num.pack()
    
    buy_button = Button(player_, text="  매입  ", font = tkinter.font.Font(player_, family="카카오 Bold", size=20)) #매입 버튼
    buy_button.place(x=100, y=650)

    blank_p = Label(player_, text="", width=5, bg="#404040")
    blank_p.pack()

    frame=tkinter.Frame(player_)

    scrollbar=tkinter.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    listbox = Listbox(frame, selectmode="extended", height=6, yscrollcommand = scrollbar.set, font=tkinter.font.Font(family='맑은 고딕', size='4'))
    #바이오, IT, 화학, 에너지, 제약, 식품 
    #총 12개 종목
    listbox.insert(0,"바이오A")
    listbox.insert(0,"바이오B")
    listbox.insert(0,"IT_A")
    listbox.insert(0,"IT_B")
    listbox.insert(0,"화학A")
    listbox.insert(0,"화학B")
    listbox.insert(0,"에너지A")
    listbox.insert(0,"에너지B")
    listbox.insert(0,"제약A")
    listbox.insert(0,"제약B")
    listbox.insert(0,"식품A")
    listbox.insert(0,"식품B")
    listbox.pack()

    scrollbar["command"]=listbox.yview
    frame.pack()

    blank_p = Label(player_, text="", height=1, bg="#404040")
    blank_p.pack()

    stock_money = [100,200,300,400,500,600,700,800,900,1000,1100,1200]

    global pr_money
    global hoho
    pr_money = "0₩"

    def show_me_the_money(self): #주가 가격 얼마인지 보여주는 함수
        menu_ = listbox.curselection()
        menu = int(menu_[0])
        hoho = str(stock_money[menu])
        pr_money = hoho + "₩"
        show_money.configure(text = "1주: "+pr_money)
        print(pr_money)
    
    show_money = Label(player_, text="1주: "+pr_money, fg="orange", font=font_p, bg="#404040")
    show_money.pack()

    listbox.bind("<<ListboxSelect>>", show_me_the_money)

    blank_p = Label(player_, text="", height=1, bg="#404040")
    blank_p.pack()

    input_text = Entry(player_, width=5, font=font_p)
    input_text.pack()

    blank_p = Label(player_, text="", height=1, bg="#404040")
    blank_p.pack()

    global money_2
    money_2= "0₩"

    def buy(): #주식 총 가격 계산 결과 출력
        #money_2 = int(input_text.get())*int(hoho)
        print(pr_money)
        print(int(pr_money.replace("₩","")))

    btn_choose = Button(player_, text="계산", font=tkinter.font.Font(player_, family="카카오 Bold", size=15), command=buy)
    btn_choose.pack()

    show_money_ls = Label(player_, text="가격:"+money_2, fg="orange", font=font_p, bg="#404040")
    show_money_ls.pack()



    player_.mainloop()

def player_2():
    player = "2"
    player_=Tk()
    player_.title("주식 매수")
    player_.geometry("570x750+670+60")
    player_['bg'] = '#404040'


    player_num = Label(player_, text="학생2")
    player_num.pack()

    
    player_.mainloop()

def player_3():
    player = "2"
    player_=Tk()
    player_.title("주식 매수")
    player_.geometry("570x750+670+60")
    player_['bg'] = '#404040'


    player_num = Label(player_, text="학생3")
    player_num.pack()

    
    player_.mainloop()

def player_4():
    player = "4"
    player_=Tk()
    player_.title("주식 매수")
    player_.geometry("570x750+670+60")
    player_['bg'] = '#404040'


    player_num = Label(player_, text="학생4")
    player_num.pack()

    
    player_.mainloop()

def player_5():
    player = "5"
    player_=Tk()
    player_.title("주식 매수")
    player_.geometry("570x750+670+60")
    player_['bg'] = '#404040'


    player_num = Label(player_, text="학생5")
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

title = Label(root, text="독보기 주식 게임", fg="orange", font=tkinter.font.Font(family="Rix열정도", size=35),bg="#404040")
title.place(x="115",y="5")

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽1 여백
blank_3.grid(row=5, column=0)

btn_p1 = Button(root, text="학생1", width=6, height=1, font=font_1, command=player_1)
btn_p1.grid(row=5,column=1)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽2 여백
blank_3.grid(row=5, column=2)

btn_p2 = Button(root, text="학생2", width=6, height=1, font=font_1,command=player_2)
btn_p2.grid(row=5,column=3)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=5, column=4)

btn_p3 = Button(root, text="학생3",  width=6, height=1, font=font_1,command=player_3)
btn_p3.grid(row=5,column=5)



btn_p4 = Button(root, text="학생4",  width=6, height=1, font=font_1,command=player_4)
btn_p4.place(x=130,y=200)

btn_p5 = Button(root, text="학생5", width=6, height=1, font=font_1,command=player_5)
btn_p5.place(x=305, y=200)

btn_setting = Button(root, text="  설정  ", font=font_3)
btn_setting.place(x=480, y=880)









root.mainloop()