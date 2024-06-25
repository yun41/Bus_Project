from tkinter import *
class User:
    def __init__(self, name, phone, birth):
        self.__name=name
        self.__phone=phone
        self.__birth=birth
    def setname(self, name):
        self.__name=name
    def setphone(self, phone):
        self.__phone=phone
    def birth(self, birth):
        self.__birth=birth
    def getname(self):
        return self.__name
    def getphone(self):
        return self.__phone
    def getbirth(self):
        return self.__birth
    def __str__(self):
        return '이름 : {}, 전화번호 : {}, 생년월일 : {}\n'.format(self.__name, self.__phone, self.__birth)
    
s=open('information.txt', 'w')
s.close()
def clickbutton():
    user=User(infoname.get(), infophone.get(), infobirth.get())
    f=open('information.txt', 'a+', encoding='UTF-8')
    f.write(user.__str__())
    f.close()
    infoname.delete(0,END)
    infophone.delete(0, END)
    infobirth.delete(0, END)
    w=Tk()
    wow=Label(w, text='정보를 저장하였습니다!')
    wow.pack()
    cmd=w.destroy
    wowbutton=Button(w, text='확인', command=cmd)
    wowbutton.pack()

dep_arr=[]
def departure():
    def seoul():
        global city1
        city1='서울'
    def busan():
        global city1
        city1='부산'
    def daejeon():
        global city1
        city1='대전'
    def daegu():
        global city1
        city1='대구'
    dep_window = Tk()
    dep_window.title('출발지 입력')
    dep_window.geometry('500x300')
    label_1 = Label(dep_window, text='안녕하세요. 출발지를 골라주세요')
    label_1.grid(row=0,column=0)
    label_2 = Label(dep_window, text='서울,부산,대전,대구 중에 골라주세요')
    label_2.grid(row=1,column=0)

    # 선택 완료 버튼 추가
    button_next = Button(dep_window,width=10, text='다음',bg='black',fg='white',command=dep_window.destroy)
    button_next.grid(row=2,column=0)

    city_button_1 = Button(dep_window,width=5, text='서울',bg='blue',fg='white',command=seoul)
    city_button_2 = Button(dep_window,width=5, text='부산',bg='yellow',fg='black',command=busan)
    city_button_3 = Button(dep_window,width=5, text='대전',bg='purple',fg='white',command=daejeon)
    city_button_4 = Button(dep_window,width=5, text='대구',bg='red',fg='white',command=daegu)
    city_button_1.grid(row=0,column=1)
    city_button_2.grid(row=0,column=2)
    city_button_3.grid(row=1,column=1)
    city_button_4.grid(row=1,column=2)

    dep_window.mainloop()
    dep_arr.append(city1)
    print(dep_arr)
    string='출발지 : {}, 도착지 : {}'.format(dep_arr[1], dep_arr[0])
    file=open('information.txt', 'a', encoding='UTF-8')
    file.write(string)
    file.close()
    

def arrival():
    def seoul():
        global city2
        city2='서울'
    def busan():
        global city2
        city2='부산'
    def daejeon():
        global city2
        city2='대전'
    def daegu():
        global city2
        city2='대구'
    arr_window = Tk()
    arr_window.title('도착지 입력')
    arr_window.geometry('500x300')

    label_1 = Label(arr_window, text='안녕하세요. 도착지를 골라주세요')
    label_1.grid(row=0,column=0)
    label_2 = Label(arr_window, text='서울,부산,대전,대구 중에 골라주세요')
    label_2.grid(row=1,column=0)

    # 다음 창을 생성하기 위해 이전 창 제거 버튼 추가 #quit가 제대로 작동을 안 해서 destroy로 변경하였습니다.
    button_next = Button(arr_window,width=10, text='선택완료',bg='black',fg='white',command=arr_window.destroy) 
    button_next.grid(row=2,column=0)

    city_button_1 = Button(arr_window,width=5, text='서울',bg='blue',fg='white',command=seoul)
    city_button_2 = Button(arr_window,width=5, text='부산',bg='yellow',fg='black',command=busan)
    city_button_3 = Button(arr_window,width=5, text='대전',bg='purple',fg='white',command=daejeon)
    city_button_4 = Button(arr_window,width=5, text='대구',bg='red',fg='white',command=daegu)
    city_button_1.grid(row=0,column=1)
    city_button_2.grid(row=0,column=2)
    city_button_3.grid(row=1,column=1)
    city_button_4.grid(row=1,column=2)

    arr_window.mainloop()
    dep_arr.append(city2)
    print(dep_arr)
    

  
def mainprogram():
    window.quit
    Main_window = Tk() ; Main_window.title('음성안내 버스예매시스템')

    # Main_window 화면 구성
    Title_label = Label(Main_window, text='음성안내 버스예매시스템', font="Arial 30 bold")
    Title_label.grid(row=0, column=0, columnspan=5, pady=10)
    Subtitle_label = Label(Main_window, text='안녕하세요. 출발지와 도착지를 입력해주세요.')
    Subtitle_label.grid(row=1, column=0, columnspan=5, pady=5)
    Blank1 = Label(Main_window)
    Blank1.grid(row=2, column=0, columnspan=5, pady=10)
    Departure_label = Label(Main_window, text='출발지')
    Departure_label.grid(row=3, column=1, pady=5, sticky=S)
    Departure_entry = Button(Main_window, text='출발지 선택', command=departure)
    Departure_entry.grid(row=4, column=1, pady=5, padx=5, sticky=E+W)
    Arrow_label = Label(Main_window, text='->', font = '10')
    Arrow_label.grid(row=4, column=2, pady=5)
    Arrival_label = Label(Main_window, text='도착지')
    Arrival_label.grid(row=3, column=3, pady=5, sticky=S)
    Arrival_entry = Button(Main_window, text='도착지선택', command=arrival)
    Arrival_entry.grid(row=4, column=3, pady=5, padx=5, sticky=E+W)
    Blank2 = Label(Main_window)
    Blank2.grid(row=4, column=4)
    Enter_button = Button(Main_window, text='확인', bg='white', fg='black', command=Main_window.quit)
    Enter_button.grid(row=5, column=1, columnspan=3, pady=20, sticky=E+W)
    Main_window.mainloop()

#TK인터가 여러 개 필요해서 각 TK인터가 나오는 것을 def로 해버렸더니 나중에 작동하는 mainloop부터 실행이 되어서 순서를 좀 바꿨습니다.

window=Tk()
window.title('사용자 정보 입력 창')
word=Label(window, text='사용자 정보를 입력해주세요 !', font='Arial 30 bold', fg='black')
word.grid(row=0, column=0, columnspan=4, ipady=10)
nname=Label(window, text='이름 : ', font='Arial 20')
nname.grid(row=1, column=0)
infoname=Entry(window, width=20, bg='white')
infoname.grid(row=1, column=1, columnspan=2, sticky=W+E, ipady=5)
pphone=Label(window, text='전화번호 :', font='Arial 20')
pphone.grid(row=2, column=0)
infophone=Entry(window, width=10, bg='white')
infophone.grid(row=2, column=1, columnspan=2, sticky=W+E, ipady=5)
bbirth=Label(window, text='생년월일 :', font='Arial 20')
bbirth.grid(row=3, column=0)
infobirth=Entry(window, width=10, bg='white')
infobirth.grid(row=3, column=1, columnspan=2, sticky=W+E, ipady=5)
btn=Button(window, text='확인', command=clickbutton)
btn.grid(row=4, column=1, columnspan=2, sticky=W+E, ipady=5, pady=5)
caution=Label(window, text='생년월일은 8자리로 입력해주세요', font='Arial 10')
caution.grid(row=4, column=0)
go=Button(window, text='예매 창 넘어가기', font='Arial 12 bold', bg='black', fg='white', command=mainprogram)
go.grid(row=4, column=3, pady=5)
window.mainloop()
