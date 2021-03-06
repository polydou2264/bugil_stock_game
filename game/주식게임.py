from tkinter import *
import tkinter
import tkinter.font
from tkinter import messagebox
import tkinter.ttk
import numpy as np
import os
import sys

global player
global player_tot_money
global num #입력받은 주 개수 값


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#stock_name = ["씨젠", "삼성바이오로직스", "삼성", "애플", "LG화학", "롯데케미칼", "GS칼텍스", "SK이노베이션", "한미약품", "녹십자", "농심", "오뚜기"]
stock_name = ["식품B", "식품A", "제약B", "제약A", "에너지B", "에너지A", "화학B", "화학A", "IT_A", "IT_B", "바이오B", "바이오A"]

first_but_stock = [[0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0]]

year = int(2013)
stock_money = [[220000,670000,1466000,604000,911000,640000,514000,627000],[280000,318000,430000,282000,380000,211500,217000,401500],[130000,124000,256500,139500,226000,119500,137000,406000], [139000,68000,672000,263000,550000,367000,265000,383000],[55000,46000,41000,56000,66000,61000,52000,45000],[171000,127000,86000,172000,154000,204000,199000,260500],[143000,232000,289000,340000,364000,430000,319000,186000],[230000,303000,127000,215000,426000,447500,283500,1050000],[157000,290000,262000,287000,421000,376000,676000,1260000], [282000,248000,256000,362000,563000,387000,565000,810000], [0,0,0,150000,370000,330000,270000,830000], [20000,16000,29000,18000,14000,8000,15000,130000]]
'''
    listbox.insert(0,"씨젠")
    listbox.insert(0,"삼성바이오로직스")
    listbox.insert(0,"삼성")
    listbox.insert(0,"애플")
    listbox.insert(0,"LG화학")
    listbox.insert(0,"롯데케미칼")
    listbox.insert(0,"GS칼텍스")
    listbox.insert(0,"SK이노베이션")
    listbox.insert(0,"한미약품")
    listbox.insert(0,"녹십자")
    listbox.insert(0,"농심")
    listbox.insert(0,"오뚜기")
'''
num = 0

#플레이어 지갑
player_tot_money = [[1000000,0,0,0,0,0,0,0,0,0,0,0,0],[1000000,0,0,0,0,0,0,0,0,0,0,0,0],[1000000,0,0,0,0,0,0,0,0,0,0,0,0],[1000000,0,0,0,0,0,0,0,0,0,0,0,0],[1000000,0,0,0,0,0,0,0,0,0,0,0,0]]
real_money = [0,0,0,0,0]

i=0
while i<5:
    real_money[i] = player_tot_money[i][0]
    i = i+1

root = tkinter.Tk()
root.title("독보기 주식게임")
#photo = PhotoImage(file=resource_path('money.ico'))
root.geometry("750x950+180+20")
root.iconbitmap(resource_path('money.ico'))
root['bg'] = '#404040'

font_1=tkinter.font.Font(family="Black Han Sans", size=26)
font_2=tkinter.font.Font(family="Rix열정도", size=35)
font_3=tkinter.font.Font(family="카카오 Regular", size=16)


def krw_to_korean_won(arg): 

    amount = str(arg).replace(',','')

    if int(amount) > 99999999:
        return '{0}억 {1}만 {2}원'.format(amount[0:-8], amount[-8:-4], amount[-4:])
    
    elif int(amount) > 9999:
        return '{0}만 {1}원'.format(amount[-8:-4], amount[-4:])

    else:
        return '{0}원'.format(amount[-4:])

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

#매입, 매도 선택 메뉴 창
def choose_menu(player):
    choose_menu=Tk()
    choose_menu.title("메뉴 선택_학생"+str(player+1))
    choose_menu.geometry("440x180+750+350")
    choose_menu.iconbitmap(resource_path('money.ico'))
    choose_menu['bg'] = '#404040'

    blank_4 = Label(choose_menu, text="", height=3, bg="#404040")
    blank_4.grid(column=0, row=0)
    blank_4 = Label(choose_menu, text="", height=3, bg="#404040")
    blank_4.grid(column=1, row=1)

    def menu_destroy():
        choose_menu.destroy()

    blank_4 = Label(choose_menu, text="", height=3, bg="#404040")
    blank_4.grid(column=2, row=1)
    blank_4 = Label(choose_menu, text="            ", height=3, bg="#404040")
    blank_4.grid(column=3, row=1)
    buy =Button(choose_menu, text="   매입   ", font = tkinter.font.Font(choose_menu, family="카카오 Bold", size=27), height=1, command=lambda:[player_buy(player)])
    buy.grid(column=5, row=1)
    blank_4 = Label(choose_menu, text="      ", height=3, bg="#404040")
    blank_4.grid(column=6, row=1)
    buy =Button(choose_menu, text="   매도   ", font = tkinter.font.Font(choose_menu, family="카카오 Bold", size=27), height=1, command=lambda:[player_sell(player)])
    buy.grid(column=7, row=1)
    
    choose_menu.mainloop()



#플레이어 지정
def player_buy(player):
    player_=Tk()
    player_.title("주식 매수")
    player_.geometry("690x750+1000+60")
    player_.iconbitmap(resource_path('money.ico'))
    player_['bg'] = '#404040'

    blank_p = Label(player_, text="", width=5, bg="#404040")
    blank_p.pack()

    font_p = tkinter.font.Font(player_, family="Rix열정도", size=23)
    player_num = Label(player_, text="팀"+str(player+1), fg="orange", font=tkinter.font.Font(player_, family="Rix열정도", size=31), bg="#404040")
    player_num.pack()

    blank_p = Label(player_, text="", width=5, bg="#404040")
    blank_p.pack()

    frame=tkinter.Frame(player_)

    scrollbar=tkinter.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    listbox = Listbox(frame, selectmode="extended", height=6, yscrollcommand = scrollbar.set, font=tkinter.font.Font(family='맑은 고딕', size='4'))
    #바이오, IT, 화학, 에너지, 제약, 식품 
    #총 12개 종목
    listbox.insert(0,"바이오A") #시젠
    listbox.insert(0,"바이오B") #삼성바이오
    listbox.insert(0,"IT_B") #삼성
    listbox.insert(0,"IT_A") #애플
    listbox.insert(0,"화학A") #LG화학
    listbox.insert(0,"화학B") #롯데케미칼
    listbox.insert(0,"에너지A") #SK이노베이션
    listbox.insert(0,"에너지B") #GS케미칼
    listbox.insert(0,"제약A") #한미약품
    listbox.insert(0,"제약B") #녹십자
    listbox.insert(0,"식품A") #농심
    listbox.insert(0,"식품B") #오뚜기
    listbox.pack()

    '''
    listbox.insert(0,"씨젠")
    listbox.insert(0,"삼성바이오로직스")
    listbox.insert(0,"삼성")
    listbox.insert(0,"애플")
    listbox.insert(0,"LG화학")
    listbox.insert(0,"롯데케미칼")
    listbox.insert(0,"GS칼텍스")
    listbox.insert(0,"SK이노베이션")
    listbox.insert(0,"한미약품")
    listbox.insert(0,"녹십자")
    listbox.insert(0,"농심")
    listbox.insert(0,"오뚜기")
'''

    scrollbar["command"]=listbox.yview
    frame.pack()

    blank_p = Label(player_, text="", height=1, bg="#404040")
    blank_p.pack()

    #stock_money = [100,200,300,400,500,600,700,800,900,1000,1100,1200] #주가 가격, 나중에 2차원 배열로 만들어 수정

    global pr_money
    global hoho
    pr_money = "0₩"

    def show_me_the_money(self): #주가 가격 얼마인지 보여주는 함수
        menu_ = listbox.curselection()
        menu = int(menu_[0])
        #hoho = str(stock_money[menu])
        #pr_money = hoho + "₩"
        show_money.configure(text = "1주: "+format(stock_money[menu][year-2013], ',d')+ "₩")
    
    show_money = Label(player_, text="1주: "+pr_money, fg   ="orange", font=font_p, bg="#404040")
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
        global num
        num = int(input_text.get()) #입력받은 값
        global menu 
        menu = int(menu_[0]) #선택된 항목

        ca_num = int(stock_money[menu][year-2013]) * num #총 결과
        show_money_ls.configure(text = "총 매수 가격: "+format(ca_num, ',d')+ "₩") #출력 값 실시간변경

    btn_choose = Button(player_, text="계산", font=tkinter.font.Font(player_, family="카카오 Bold", size=15), command=calculate_money) #계산 버튼
    btn_choose.pack()

    show_money_ls = Label(player_, text="총 매수 가격: "+money_2, fg="white", font=font_p, bg="#404040") #게산된 값 출력
    show_money_ls.pack()

    player_money = Label(player_, text="재산: "+format(player_tot_money[player][0], ',d')+ "₩", fg="#9DD84B", font=font_p, bg="#404040")
    player_money.pack()

    def buy_stock():
        global ca_num

        if player_tot_money[player][0] < ca_num:
            tkinter.messagebox.showerror("매입 오류","보유 현금이 부족합니다.")
        else:

            if ca_num == 0:
                tkinter.messagebox.showerror("매입 오류","매입이 정상적으로 완료하지 못했습니다.")
            else:

                player_tot_money[player][0] = player_tot_money[player][0] - ca_num
                i=0
                tot = 0
            
                player_money.configure(text = "남은 현금: "+format(player_tot_money[player][0], ',d')+ "₩")

                #처음 구매 가격 알기
                if player_tot_money[player][menu+1] == 0:
                    first_but_stock[player][menu] = stock_money[menu][year-2013]

                player_tot_money[player][menu+1] =  player_tot_money[player][menu+1] + num

                while i<12:
                    tot_1 = int(player_tot_money[player][i+1]) * int(stock_money[i][year-2013])
                    tot = tot + tot_1
                    i = i+1
                
                real_money[player] = player_tot_money[player][0] + int(tot)
                

                if player == 0:
                    money_p1.configure(text=format(real_money[player], ',d')+ "₩")

                elif player == 1:
                    money_p2.configure(text=format(real_money[player],',d')+ "₩")
    
                elif player == 2:
                    money_p3.configure(text=format(real_money[player], ',d')+ "₩")

                elif player == 3:
                    money_p4.configure(text=format(real_money[player], ',d')+ "₩")

                elif player == 4:
                    money_p5.configure(text=format(real_money[player], ',d')+ "₩")
                tkinter.messagebox.showinfo("매입","매입이 정상적으로 완료되었습니다!")
                input_text.delete(0,"end")
                input_text.insert(END, "0")
                show_money_ls.configure(text = "가격: 0원")
                ca_num = 0




    buy_button = Button(player_, text="       매입       ", font = tkinter.font.Font(player_, family="카카오 Bold", size=20), command=buy_stock, height=3) #매입 버튼
    buy_button.place(x=100, y=500)

    player_.mainloop()

#매도 --------------------------------------------------------------------------------------------------------------------------
def player_sell(player):
    player_1=Tk()
    player_1.title("주식 매도")
    player_1.geometry("690x750+1000+60")
    player_1.iconbitmap(resource_path('money.ico'))
    player_1['bg'] = '#404040'
    
    blank_p = Label(player_1, text="", width=5, bg="#404040")
    blank_p.pack()

    font_p = tkinter.font.Font(player_1, family="Rix열정도", size=23)
    player_num = Label(player_1, text="팀"+str(player+1), fg="orange", font=tkinter.font.Font(player_1, family="Rix열정도", size=31), bg="#404040")
    player_num.pack()

    blank_p = Label(player_1, text="", width=5, bg="#404040")
    blank_p.pack()

    frame=tkinter.Frame(player_1)

    scrollbar=tkinter.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    listbox_ = Listbox(frame, selectmode="extended", height=8, yscrollcommand = scrollbar.set, font=tkinter.font.Font(family='맑은 고딕', size='4'), width=28)
    #바이오, IT, 화학, 에너지, 제약, 식품 
    #총 12개 종목
    listbox_.insert(0,"씨젠 - " + str(player_tot_money[player][12]) + "개")
    listbox_.insert(0,"삼성바이오로직스 - " + str(player_tot_money[player][11]) + "개")
    listbox_.insert(0,"삼성 - " + str(player_tot_money[player][10]) + "개")
    listbox_.insert(0,"애플 - " + str(player_tot_money[player][9]) + "개")
    listbox_.insert(0,"LG화학 - " + str(player_tot_money[player][8]) + "개")
    listbox_.insert(0,"롯데케미칼 - " + str(player_tot_money[player][7]) + "개")
    listbox_.insert(0,"GS칼텍스 - " + str(player_tot_money[player][6]) + "개")
    listbox_.insert(0,"SK이노베이션 - " + str(player_tot_money[player][5]) + "개")
    listbox_.insert(0,"한미약품 - " + str(player_tot_money[player][4]) + "개")
    listbox_.insert(0,"녹십자 - " + str(player_tot_money[player][3]) + "개")
    listbox_.insert(0,"농심 - " + str(player_tot_money[player][2]) + "개")
    listbox_.insert(0,"오뚜기 - " + str(player_tot_money[player][1]) + "개")
    listbox_.pack()

    scrollbar["command"]=listbox_.yview
    frame.pack()
    
    global pr_money
    global hoho
    pr_money = "0₩"

    def show_me_the_money(self): #주가 가격 얼마인지 보여주는 함수
        mm = listbox_.curselection()
        menu = int(mm[0])
        #hoho = str(stock_money[menu])
        #pr_money = hoho + "₩"
        show_money.configure(text = "현재가: "+ format(stock_money[menu][year-2013], ',d')+ "₩")
    
    show_money = Label(player_1, text="현재가: "+pr_money, fg="orange", font=font_p, bg="#404040")
    show_money.pack()

    listbox_.bind("<<ListboxSelect>>", show_me_the_money) #휠

    blank_p = Label(player_1, text="", height=1, bg="#404040") #공백
    blank_p.pack()

    input_text = Entry(player_1, width=5, font=font_p) #주식 개수 입력 받기
    input_text.pack()
    input_text.insert(END, "0")

    blank_p = Label(player_1, text="", height=1, bg="#404040") #공백
    #blank_p.pack()

    global money_3
    money_3= "0원"

    def calculate_money(): #주가 가격 얼마인지 보여주는 함수 
        global ca_num_
        global menu_1
        menu_1 = listbox_.curselection()
        global num_
        num_ = int(input_text.get()) #입력받은 값

        if player_tot_money[player][int(menu_1[0])+1] < num_:
            tkinter.messagebox.showerror("매도 오류","현재 보유 주식 개수에 맞게 입력해주세요.")

        else:   
            global menu
            menu = int(menu_1[0]) #선택된 항목

            ca_num_ = int(stock_money[menu][year-2013]) * num_ #총 결과
            show_money_ls1.configure(text = "총 매도 가격: "+ format(ca_num_,',d')+ "₩") #출력 값 실시간변경

    btn_choose = Button(player_1, text="계산", font=tkinter.font.Font(player_1, family="카카오 Bold", size=15), command=calculate_money) #계산 버튼

    btn_choose.pack()

    show_money_ls1 = Label(player_1, text="총 매도 가격: "+money_3, fg="white", font=font_p, bg="#404040") #게산된 값 출력
    show_money_ls1.pack()

    player_money = Label(player_1, text="보유 현금: "+format(player_tot_money[player][0], ',d')+ "₩", fg="#9DD84B", font=font_p, bg="#404040")
    player_money.pack()

    def sell_stock():
        global ca_num_

        if ca_num_ == 0:
            tkinter.messagebox.showerror("매도 오류","매입이 정상적으로 완료하지 못했습니다.")
        else:
            player_tot_money[player][0] = player_tot_money[player][0] + ca_num_
            i=0
            tot = 0
            
            player_money.configure(text = "남은 현금: "+format(player_tot_money[player][0], ',d')+ "₩")
            player_tot_money[player][menu+1] =  player_tot_money[player][menu+1] - num_

            #다 팔았을 때 처음 가격 0원
            if player_tot_money[player][menu] == 0:
                first_but_stock[player][menu] = 0

            while i<12:
                tot_1 = int(player_tot_money[player][i+1]) * int(stock_money[i][year-2013])
                tot = tot + tot_1
                i = i+1

            real_money[player] = player_tot_money[player][0] + int(tot)

            if player == 0:
                money_p1.configure(text=format(real_money[player], ',d')+ "₩")

            elif player == 1:
                money_p2.configure(text=format(real_money[player], ',d')+ "₩")
    
            elif player == 2:
                money_p3.configure(text=format(real_money[player], ',d')+ "₩")

            elif player == 3:
                money_p4.configure(text=format(real_money[player], ',d')+ "₩")

            elif player == 4:
                money_p5.configure(text=format(real_money[player], ',d')+ "₩")

            tkinter.messagebox.showinfo("매도","매도가 정상적으로 완료되었습니다!")
            listbox_.delete(0, 11)
            listbox_.insert(0,"씨젠 - " + str(player_tot_money[player][12]) + "개")
            listbox_.insert(0,"삼성바이오로직스 - " + str(player_tot_money[player][11]) + "개")
            listbox_.insert(0,"삼성 - " + str(player_tot_money[player][10]) + "개")
            listbox_.insert(0,"애플 - " + str(player_tot_money[player][9]) + "개")
            listbox_.insert(0,"LG화학 - " + str(player_tot_money[player][8]) + "개")
            listbox_.insert(0,"롯데케미칼 - " + str(player_tot_money[player][7]) + "개")
            listbox_.insert(0,"GS칼텍스 - " + str(player_tot_money[player][6]) + "개")
            listbox_.insert(0,"SK이노베이션 - " + str(player_tot_money[player][5]) + "개")
            listbox_.insert(0,"한미약품 - " + str(player_tot_money[player][4]) + "개")
            listbox_.insert(0,"녹십자 - " + str(player_tot_money[player][3]) + "개")
            listbox_.insert(0,"농심 - " + str(player_tot_money[player][2]) + "개")
            listbox_.insert(0,"오뚜기 - " + str(player_tot_money[player][1]) + "개")
            
            input_text.delete(0,"end")
            input_text.insert(END, "0")
            show_money_ls1.configure(text = "가격: 0원")
            ca_num_ = 0

    buy_button = Button(player_1, text="       매도       ", font = tkinter.font.Font(player_1, family="카카오 Bold", size=20), command=sell_stock, height=3) #매입 버튼
    buy_button.place(x=100, y=500)

    player_1.mainloop()

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


#힌트 구매 
def buy_hint(player):
    buy_hint = Tk()
    buy_hint.title("힌트 구매")
    buy_hint.geometry("600x200+1050+150")
    buy_hint.iconbitmap(resource_path('money.ico'))
    buy_hint['bg'] = "#404040"

    player_num = Label(buy_hint, text="힌트 구매(%로 입력하세요)", fg="orange", font=tkinter.font.Font(buy_hint, family="Rix열정도", size=31), bg="#404040")
    player_num.pack()

    blank_3 = Label(buy_hint, text="", width=1, bg="#404040") #오른쪽3 여백
    blank_3.pack()

    input_text_ = Entry(buy_hint, width=15, font=tkinter.font.Font(buy_hint, family="Rix열정도", size=23)) #주식 개수 입력 받기
    input_text_.pack()
    input_text_.insert(END, "0")
    blank_3 = Label(buy_hint, text="", width=1, bg="#404040") #오른쪽3 여백
    blank_3.pack()

    def edit_hit(player):

        real_money[player] =  real_money[player] * (100-int(input_text_.get())) / 100

        money_p1.configure(text = format(int(real_money[0]), ',d')+ "₩")
        money_p2.configure(text = format(int(real_money[1]), ',d')+ "₩")
        money_p3.configure(text = format(int(real_money[2]), ',d')+ "₩")
        money_p4.configure(text = format(int(real_money[3]), ',d')+ "₩")
        money_p5.configure(text = format(int(real_money[4]), ',d')+ "₩")

        tkinter.messagebox.showinfo("힌트 구매","힌트 구매가 정상적으로 완료되었습니다!")

    btn = Button(buy_hint, text="구매", font=tkinter.font.Font(buy_hint, family="Rix열정도", size=17), width=20, command=lambda:[edit_hit(player)])
    btn.pack()



#재산 수정
def edit(player):
    edit = Tk()
    edit.title("재산 수정")
    edit.geometry("600x200+1050+150")
    edit.iconbitmap(resource_path('money.ico'))
    edit['bg'] = "#404040"

    player_num = Label(edit, text="재산 수정", fg="orange", font=tkinter.font.Font(edit, family="Rix열정도", size=31), bg="#404040")
    player_num.pack()

    blank_3 = Label(edit, text="", width=1, bg="#404040") #오른쪽3 여백
    blank_3.pack()

    input_text_ = Entry(edit, width=15, font=tkinter.font.Font(edit, family="Rix열정도", size=23)) #주식 개수 입력 받기
    input_text_.pack()
    input_text_.insert(END, "0")
    blank_3 = Label(edit, text="", width=1, bg="#404040") #오른쪽3 여백
    blank_3.pack()

    def edit_cm(player):

        real_money[player] = int(input_text_.get())

        money_p1.configure(text = format(int(real_money[0]), ',d')+ "₩")
        money_p2.configure(text = format(int(real_money[1]), ',d')+ "₩")
        money_p3.configure(text = format(int(real_money[2]), ',d')+ "₩")
        money_p4.configure(text = format(int(real_money[3]), ',d')+ "₩")
        money_p5.configure(text = format(int(real_money[4]), ',d')+ "₩")

        tkinter.messagebox.showinfo("Edit","재산 수정이 정상적으로 완료되었습니다!")

    btn = Button(edit, text="Edit", font=tkinter.font.Font(edit, family="Rix열정도", size=17), width=20, command=lambda:[edit_cm(player)])
    btn.pack()

    


#플레이어가 가지고 있는 주식 개수 확인 함수
def check_money(player):
    check_money=Tk()
    check_money.title("보유 주식 확인")
    check_money.geometry("690x750+1000+60")
    check_money.iconbitmap(resource_path('money.ico'))
    check_money['bg'] = '#404040'


    player_num = Label(check_money, text="팀"+str(player+1), fg="orange", font=tkinter.font.Font(check_money, family="Rix열정도", size=31), bg="#404040")
    player_num.pack()

    treeview=tkinter.ttk.Treeview(check_money, columns=["one", "two","three", "four"], displaycolumns=["one","two","three","four"])
    treeview.pack()

    treeview.column("#0", width=100, anchor="center")
    treeview.heading("#0", text="종목명")

    treeview.column("#1", width=180, anchor="center")
    treeview.heading("#1", text="매입금액", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("#2", text="주식수", anchor="center")

    treeview.column("#3", width=180, anchor="center")
    treeview.heading("#3", text="현재금액", anchor="center")

    treeview.column("#4", width=100, anchor="center")
    treeview.heading("#4", text="수익률", anchor="center")

    edit_money = Button(check_money, text="Edit", font=tkinter.font.Font(check_money, family="Rix열정도", size=17), width=10, command=lambda:[edit(player)])
    edit_money.place(x=40, y=650)

    hint_money = Button(check_money, text="Hint", font=tkinter.font.Font(check_money, family="Rix열정도", size=17), width=10, command=lambda:[buy_hint(player)])
    hint_money.place(x=260, y=650)

    b=0

    #수익률 계산 함수
    def per(a, b):

        tp = round(b / a * 100, 2)
        tp = tp - 100

        kam = str(tp) + "%"

        
        return str(kam)
    
    while b<12:
        if player_tot_money[player][b+1] != 0:
            #주식이름/첫 구매 가격/보유 주식 수/현재 금액/수익률
            treeview.insert('', 'end', text=str(stock_name[b]), values=(str(first_but_stock[player][b]), str(player_tot_money[player][b+1]), str(stock_money[b][year-2013]), per(int(first_but_stock[player][b]), int(stock_money[b][year-2013]))), iid =b)

        b = b + 1

    i=0

    check_money.mainloop()

#다음년도 버튼
def next_year():
    global year

    MsgBox = tkinter.messagebox.askquestion ('경고',"다음년도로 이동할까요?",icon = 'warning')
    if MsgBox == 'yes':
        if year == 2019:
            year = year + 1
            btn_year.configure(text = "게임종료", font = tkinter.font.Font(family="Black Han Sans", size=30))
    
        elif year == 2020:
            tkinter.messagebox.showinfo("게임 종료", "프로그램을 종료해주세요!")
    
        else:
            year = year + 1
        i=0
        gg=0
        tot=0
        while gg<5:
            while i<12:
                tot_1 = int(player_tot_money[gg][i+1]) * int(stock_money[i][year-2013])
                tot = tot + tot_1
                real_money[gg] = tot + player_tot_money[gg][0]
                i = i + 1
            tot = 0
            i=0
            gg = gg + 1
        
        



    money_p1.configure(text = format(int(real_money[0]), ',d')+ "₩")
    money_p2.configure(text = format(int(real_money[1]), ',d')+ "₩")
    money_p3.configure(text = format(int(real_money[2]), ',d')+ "₩")
    money_p4.configure(text = format(int(real_money[3]), ',d')+ "₩")
    money_p5.configure(text = format(int(real_money[4]), ',d')+ "₩")

    show_year.configure(text = str(year)+"년")

#전년도 버튼(실수 방지)
def back_year():
    global year
    
    if year > 2013:
        year = year - 1
    
        i=0
        gg=0
        tot=0
        while gg<5:
            while i<12:
                tot_1 = int(player_tot_money[gg][i+1]) * int(stock_money[i][year-2013])
                tot = tot + tot_1
                real_money[gg] = tot + player_tot_money[gg][0]
                i = i + 1
            tot = 0
            i=0
            gg = gg + 1

    money_p1.configure(text = format(int(real_money[0]), ',d')+ "₩")
    money_p2.configure(text = format(int(real_money[1]), ',d')+ "₩")
    money_p3.configure(text = format(int(real_money[2]), ',d')+ "₩")
    money_p4.configure(text = format(int(real_money[3]), ',d')+ "₩")
    money_p5.configure(text = format(int(real_money[4]), ',d')+ "₩")

    show_year.configure(text = str(year)+"년")


#현재 년도
show_year=Label(root, text = str(year) + "년",fg = "#FFFFFF", font = tkinter.font.Font(family="Black Han Sans", size=50) ,  bg="#404040")
show_year.place(x=270, y=565)

#다음년도 버튼
btn_year = Button(root, text="NEXT YEAR", font = font_1, command=next_year, height=2, width= 10)
btn_year.place(x=260,y=680)

btn_bkyear = Button(root, text="BACK", font = tkinter.font.Font(family="Black Han Sans", size=17), command=back_year, height=1)
btn_bkyear.place(x=30,y=850)

#학생1
btn_p1 = Button(root, text="팀1", width=6, height=1, font=font_1, command=lambda:[choose_menu(0)])
btn_p1.grid(row=5,column=1)
blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=5, column=2)
money_p1 = Button(root, text=format(real_money[0], ',d')+ "₩", fg="#9DD84B", font=tkinter.font.Font(root, family="Rix열정도", size=22), bg="#404040", activebackground="#404040", activeforeground = "#9DD84B", command=lambda:[check_money(0)], width=24)
money_p1.grid(row=5,column=3)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=6, column=1)

#학생2
btn_p2 = Button(root, text="팀2", width=6, height=1, font=font_1,command=lambda:[choose_menu(1)])
btn_p2.grid(row=7,column=1)
money_p2 = Button(root, text=format(real_money[1], ',d') + "₩", fg="#9DD84B", font=tkinter.font.Font(root, family="Rix열정도", size=22), bg="#404040", activebackground="#404040", activeforeground = "#9DD84B", command=lambda:[check_money(1)], width=24)
money_p2.grid(row=7,column=3)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=8, column=1)

#학생3
btn_p3 = Button(root, text="팀3",  width=6, height=1, font=font_1,command=lambda:[choose_menu(2)])
btn_p3.grid(row=9,column=1)
money_p3 = Button(root, text=format(real_money[2], ',d') + "₩", fg="#9DD84B", font=tkinter.font.Font(root, family="Rix열정도", size=22), bg="#404040", activebackground="#404040", activeforeground = "#9DD84B", command=lambda:[check_money(2)], width=24)
money_p3.grid(row=9,column=3)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=10, column=1)

#학생4
btn_p4 = Button(root, text="팀4",  width=6, height=1, font=font_1,command=lambda:[choose_menu(3)])
btn_p4.grid(row=11,column=1)
money_p4 = Button(root, text=format(real_money[3], ',d') + "₩", fg="#9DD84B", font=tkinter.font.Font(root, family="Rix열정도", size=22), bg="#404040", activebackground="#404040", activeforeground = "#9DD84B", command=lambda:[check_money(3)], width=24)
money_p4.grid(row=11,column=3)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=12, column=1)

#학생5
btn_p5 = Button(root, text="팀5", width=6, height=1, font=font_1,command=lambda:[choose_menu(4)])
btn_p5.grid(row=13,column=1)
money_p5 = Button(root, text=format(real_money[4], ',d') + "₩", fg="#9DD84B", font=tkinter.font.Font(root, family="Rix열정도", size=22), bg="#404040", activebackground="#404040", activeforeground = "#9DD84B", command=lambda:[check_money(4)], width=24)
money_p5.grid(row=13,column=3)

blank_3 = Label(root, text="", width=1, bg="#404040") #오른쪽3 여백
blank_3.grid(row=14, column=1)

#풀 매도 함수
def sell_all_stock():
    ca = 0
    i=0
    player = 0

    MsgBox = tkinter.messagebox.askquestion ('경고',"풀매수를 진행할까요?",icon = 'warning')
    if MsgBox == 'yes':
        while player < 5:
            while i<12:
                if player_tot_money[player][i+1] != 0:
                    ca = player_tot_money[player][i+1] * stock_money[i][year-2013]
                    player_tot_money[player][0] = player_tot_money[player][0] + ca
                    player_tot_money[player][i+1] = 0

                print("i:" + str(i))
                i = i + 1
            print("player: " + str(player))
            player = player + 1
            i=0
        print("end")

#풀매수 버튼
btn_buy_all = Button(root, text="ALL매도", width=6, height=1, font=font_1,command=sell_all_stock)
btn_buy_all.grid(row=15,column=1)

btn_setting = Button(root, text="  설정  ", font=font_3)
btn_setting.place(x=660, y=890)

#정ㅁ말 tlqkf 드디어 끝낸다

root.mainloop()