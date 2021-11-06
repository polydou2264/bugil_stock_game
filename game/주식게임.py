﻿from tkinter import *
import tkinter
import tkinter.font
from tkinter import messagebox
import tkinter.ttk

global player
global player_tot_money
global num #입력받은 주 개수 값

num = 0

#플레이어 지갑
player_tot_money = [[100000,0,0,0,0,0,0,0,0,0,0,0,0],[10000,0,0,0,0,0,0,0,0,0,0,0,0],[10000,0,0,0,0,0,0,0,0,0,0,0,0],[10000,0,0,0,0,0,0,0,0,0,0,0,0],[10000,0,0,0,0,0,0,0,0,0,0,0,0]]

root = tkinter.Tk()
root.title("독보기 주식게임")
root.geometry("750x950+180+20")
root.iconbitmap('money.ico')
root['bg'] = '#404040'

font_1=tkinter.font.Font(family="Black Han Sans", size=26)
font_2=tkinter.font.Font(family="Rix열정도", size=35)
font_3=tkinter.font.Font(family="카카오 Regular", size=16)

#돈 한글로 표시하는 법
def get_kor_amount_string(num_amount, ndigits_round=0, str_suffix='원'):
    """숫자를 자릿수 한글단위와 함께 리턴한다 """
    assert isinstance(num_amount, int) and isinstance(ndigits_round, int)
    assert num_amount >= 1, '최소 1원 이상 입력되어야 합니다'
    ## 일, 십, 백, 천, 만, 십, 백, 천, 억, ... 단위 리스트를 만든다.
    maj_units = ['만', '억', '조', '경', '해', '자', '양', '구', '간', '정', '재', '극'] # 10000 단위
    units     = [' '] # 시작은 일의자리로 공백으로하고 이후 십, 백, 천, 만...
    for mm in maj_units:
        units.extend(['십', '백', '천']) # 중간 십,백,천 단위
        units.append(mm)
    
    list_amount = list(str(round(num_amount, ndigits_round))) # 라운딩한 숫자를 리스트로 바꾼다
    list_amount.reverse() # 일, 십 순서로 읽기 위해 순서를 뒤집는다
    
    str_result = '' # 결과
    num_len_list_amount = len(list_amount)
    
    for i in range(num_len_list_amount):
        str_num = list_amount[i]
        # 만, 억, 조 단위에 천, 백, 십, 일이 모두 0000 일때는 생략
        if num_len_list_amount >= 9 and i >= 4 and i % 4 == 0 and ''.join(list_amount[i:i+4]) == '0000':
            continue
        if str_num == '0': # 0일 때
            if i % 4 == 0: # 4번째자리일 때(만, 억, 조...)
                str_result = units[i] + str_result # 단위만 붙인다
        elif str_num == '1': # 1일 때
            if i % 4 == 0: # 4번째자리일 때(만, 억, 조...)
                str_result = str_num + units[i] + str_result # 숫자와 단위를 붙인다
            else: # 나머지자리일 때
                str_result = units[i] + str_result # 단위만 붙인다
        else: # 2~9일 때
            str_result = str_num + units[i] + str_result # 숫자와 단위를 붙인다
    str_result = str_result.strip() # 문자열 앞뒤 공백을 제거한다 
    if len(str_result) == 0:
        return None
    if not str_result[0].isnumeric(): # 앞이 숫자가 아닌 문자인 경우
        str_result = '1' + str_result # 1을 붙인다
    return str_result + str_suffix # 접미사를 붙인다

#command=lambda:[player_window(), player_1()] <-- 함수 여러개 사용 

#플레이어 지정
def player(player):
    player_=Tk()
    player_.title("주식 매수")
    player_.geometry("690x750+1000+60")
    player_.iconbitmap('money.ico')
    player_['bg'] = '#404040'

    blank_p = Label(player_, text="", width=5, bg="#404040")
    blank_p.pack()

    font_p = tkinter.font.Font(player_, family="Rix열정도", size=23)
    player_num = Label(player_, text="학생"+str(player+1), fg="orange", font=tkinter.font.Font(player_, family="Rix열정도", size=31), bg="#404040")
    player_num.pack()

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
    listbox.insert(0,"삼성")
    listbox.insert(0,"애플")
    listbox.insert(0,"화학A")
    listbox.insert(0,"화학B")
    listbox.insert(0,"에너지A")
    listbox.insert(0,"에너지B")
    listbox.insert(0,"제약A")
    listbox.insert(0,"제약B")
    listbox.insert(0,"농심")
    listbox.insert(0,"오뚜기")
    listbox.pack()

    scrollbar["command"]=listbox.yview
    frame.pack()

    blank_p = Label(player_, text="", height=1, bg="#404040")
    blank_p.pack()

    stock_money = [100,200,300,400,500,600,700,800,900,1000,1100,1200] #주가 가격, 나중에 2차원 배열로 만들어 수정

    global pr_money
    global hoho
    pr_money = "0₩"

    def show_me_the_money(self): #주가 가격 얼마인지 보여주는 함수
        menu_ = listbox.curselection()
        menu = int(menu_[0])
        #hoho = str(stock_money[menu])
        #pr_money = hoho + "₩"
        show_money.configure(text = "1주: "+get_kor_amount_string(stock_money[menu]))
    
    show_money = Label(player_, text="1주: "+pr_money, fg="orange", font=font_p, bg="#404040")
    show_money.pack()

    listbox.bind("<<ListboxSelect>>", show_me_the_money) #휠

    blank_p = Label(player_, text="", height=1, bg="#404040") #공백
    blank_p.pack()

    input_text = Entry(player_, width=5, font=font_p) #주식 개수 입력 받기
    input_text.pack()
    input_text.insert(END, "0")

    blank_p = Label(player_, text="", height=1, bg="#404040") #공백
    #blank_p.pack()

    global money_2
    money_2= "0원"

    def calculate_money(): #주가 가격 얼마인지 보여주는 함수
        global ca_num
        global menu_
        menu_ = listbox.curselection()
        num = int(input_text.get()) #입력받은 값
            
        menu = int(menu_[0]) #선택된 항목
        ca_num = int(stock_money[menu]) * num #총 결과
        show_money_ls.configure(text = "가격: "+get_kor_amount_string(ca_num)) #출력 값 실시간변경

    btn_choose = Button(player_, text="계산", font=tkinter.font.Font(player_, family="카카오 Bold", size=15), command=calculate_money) #계산 버튼
    btn_choose.pack()

    show_money_ls = Label(player_, text="가격:"+money_2, fg="white", font=font_p, bg="#404040") #게산된 값 출력
    show_money_ls.pack()

    player_money = Label(player_, text="재산:"+get_kor_amount_string(player_tot_money[player][0]), fg="#9DD84B", font=font_p, bg="#404040")
    player_money.pack()

    def buy_stock():
        global ca_num
        #player_.wm_attributes("-topmost", 1)
        player_tot_money[player][0] = player_tot_money[player][0] - ca_num
        #if player_money[0][0]
        player_money.configure(text = "재산: "+get_kor_amount_string(player_tot_money[player][0]))
        player_tot_money[player][menu_[0]] =  player_tot_money[player][menu_[0]] + num
        money_p1.configure(text=get_kor_amount_string(player_tot_money[player][0]))

        if ca_num == 0:
            tkinter.messagebox.showerror("매입","매입이 정상적으로 완료하지 못했습니다.")
        else:
            tkinter.messagebox.showinfo("매입","매입이 정상적으로 완료되었습니다!")
            input_text.delete(0,"end")
            input_text.insert(END, "0")
            show_money_ls.configure(text = "가격: 0원")
            ca_num = 0



    buy_button = Button(player_, text="       매입       ", font = tkinter.font.Font(player_, family="카카오 Bold", size=20), command=lambda:[buy_stock()], height=3) #매입 버튼
    buy_button.place(x=100, y=500)




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
title.place(x="205",y="5")

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽1 여백
blank_3.grid(row=5, column=0)

#플레이어가 가지고 있는 주식 개수 확인 함수
def check_money(player):
    check_money=Tk()
    check_money.title("보유 주식 확인")
    check_money.geometry("690x750+1000+60")
    check_money.iconbitmap('money.ico')
    check_money['bg'] = '#404040'

    player_num = Label(check_money, text="학생"+str(player+1), fg="orange", font=tkinter.font.Font(check_money, family="Rix열정도", size=31), bg="#404040")
    player_num.pack()

    treeview=tkinter.ttk.Treeview(check_money, columns=["one", "two","three"], displaycolumns=["one","two","three"])
    treeview.pack()

    treeview.column("#0", width=180,)
    treeview.heading("#0", text="주식 종목", font=tkinter.font.Font(check_money, family="Rix열정도", size=31), fg="black")

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="보유수", anchor="center")









#학생1
btn_p1 = Button(root, text="학생1", width=6, height=1, font=font_1, command=lambda:[player(0)])
btn_p1.grid(row=5,column=1)
blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=5, column=2)
money_p1 = Button(root, text=get_kor_amount_string(player_tot_money[0][0]), fg="#9DD84B", font=tkinter.font.Font(root, family="Rix열정도", size=22), bg="#404040", activebackground="#404040", activeforeground = "#9DD84B", command=lambda:[check_money(0)])
money_p1.grid(row=5,column=3)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=6, column=1)

#학생2
btn_p2 = Button(root, text="학생2", width=6, height=1, font=font_1,command=lambda:[player(1)])
btn_p2.grid(row=7,column=1)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=8, column=1)

#학생3
btn_p3 = Button(root, text="학생3",  width=6, height=1, font=font_1,command=lambda:[player(2)])
btn_p3.grid(row=9,column=1)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=10, column=1)

#학생4
btn_p4 = Button(root, text="학생4",  width=6, height=1, font=font_1,command=lambda:[player(3)])
btn_p4.grid(row=11,column=1)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=12, column=1)

#학생5
btn_p5 = Button(root, text="학생5", width=6, height=1, font=font_1,command=lambda:[player(4)])
btn_p5.grid(row=13,column=1)

btn_setting = Button(root, text="  설정  ", font=font_3)
btn_setting.place(x=660, y=890)



root.mainloop()