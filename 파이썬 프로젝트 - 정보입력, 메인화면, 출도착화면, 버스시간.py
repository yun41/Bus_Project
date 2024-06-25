from tkinter import *
import datetime as dt
import speech_recognition as sr  # STT 모듈 import
import pyttsx3 # TTS 모듈 import
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
    

#TK인터가 여러 개 필요해서 각 TK인터가 나오는 것을 def로 해버렸더니 나중에 작동하는 mainloop부터 실행이 되어서 순서를 좀 바꿨습니다.
def readtime_gettime():
    nowtime=dt.datetime.now()
    h=nowtime.hour
    seoul_daejeon = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    seoul_daegu = [0,1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    seoul_busan = [1,2,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    daejeon_seoul = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    daejeon_daegu = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    daejeon_busan = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    daegu_seoul = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    daegu_daejeon = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    daegu_busan = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    busan_seoul = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    busan_daejeon = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    busan_daegu = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    if dep_arr[1]=='서울':
        if dep_arr[0]=='대전':
            for i in range(seoul_daejeon):
                if h>i:
                    seoul_daejeon.remove(i)   
            readtime='가장 빠른 출발 시간 : {}시'.format(seoul_daejeon[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()
        elif dep_arr[0]=='대구':
            for i in range(seoul_daegu):
                if h>i:
                    seoul_daegu.remove(i)
            readtime='가장 빠른 출발 시간 : {}시'.format(seoul_daegu[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()
        elif dep_arr[0]=='부산':
            for i in range(seoul_busan):
                if h>i:
                    seoul_busan.remove(i)
            readtime='가장 빠른 출발 시간 : {}시'.format(seoul_busan[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()
    elif dep_arr[1]=='대전':
        if dep_arr[0]=='서울':
            for i in range(daejeon_seoul):
                if h>i:
                    daejeon_seoul.remove(i)
            readtime='가장 빠른 출발 시간 : {}시'.format(daejeon_seoul[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()
        elif dep_arr[0]=='대구':
            for i in range(daejeon_daegu):
                if h>i:
                    daejeon_daegu.remove(i)
            readtime='가장 빠른 출발 시간 : {}시'.format(daejeon_daegu[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()
        elif dep_arr[0]=='부산':
            for i in range(daejeon_busan):
                if h>i:
                    daejeon_busan.remove(i)
            readtime='가장 빠른 출발 시간 : {}시'.format(daejeon_busan[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()
    elif dep_arr[1]=='대구':
        if dep_arr[0]=='서울':
            for i in range(daegu_seoul):
                if h>i:
                    daegu_seoul.remove(i)
            readtime='가장 빠른 출발 시간 : {}시'.format(daegu_seoul[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()
        elif dep_arr[0]=='대전':
            for i in range(daegu_daejeon):
                if h>i:
                    daegu_daejeon.remove(i)
            readtime='가장 빠른 출발 시간 : {}시'.format(daegu_daejeon[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()
        elif dep_arr[0]=='부산':
            for i in range(daegu_busan):
                if h>i:
                    daegu_busan.remove(i)
            readtime='가장 빠른 출발 시간 : {}시'.format(daegu_busan[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()
    elif dep_arr[1]=='부산':
        if dep_arr[0]=='서울':
            for i in range(busan_seoul):
                if h>i:
                    busan_seoul.remove(i)
            readtime='가장 빠른 출발 시간 : {}시'.format(busan_seoul[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()
        elif dep_arr[0]=='대전':
            for i in range(busan_daejeon):
                if h>i:
                    busan_daejeon.remove(i)
            readtime='가장 빠른 출발 시간 : {}시'.format(busan_daejeon[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()
        elif dep_arr[0]=='대구':
            for i in range(busan_daegu):
                if h>i:
                    busan_daegu.remove(i)
            readtime='가장 빠른 출발 시간 : {}시'.format(busan_daegu[0])            
            filename=open('information.txt', 'a')
            filename.write(readtime)
            filename.close()

def callingSTT1():
    engine = pyttsx3.init()

    # 이름 받아오기
    text_name = "안녕하세요. 음성 버스예매 시스템입니다. 성함을 말씀해주세요. 음성을 받는 시간은 10초입니다."
    engine.say(text_name)
    engine.runAndWait()
    name_result = ""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                audio = r.listen(source, timeout=10, phrase_time_limit=10)  # 타임아웃 설정

                try:  
                    name_result = r.recognize_google(audio, language='ko-KR')
                    infoname.delete(0,END)
                    infoname.insert(END, name_result)
                    break
                except sr.UnknownValueError:
                    engine.say('오디오 인식 불가, 성함을 다시 말씀해주세요.')
                    engine.runAndWait()
                
                except sr.RequestError as e:
                    result = '에러 발생: {}'.format(e)
                    infoname.delete(0,END)
                    infoname.insert(END, result)
        
    except KeyboardInterrupt:
        pass
    
    # 전화번호 받아오기
    text_phone = name_result + "님. 핸드폰 전화번호를 말씀해주세요. 음성을 받는 시간은 15초입니다."
    engine.say(text_phone) 
    engine.runAndWait()
    phone_result = ""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=15, phrase_time_limit=15)  # 타임아웃 설정

            try:  # 예외처리 구문
                phone_result = r.recognize_google(audio, language='ko-KR')
                if '-' in phone_result:
                    phone_result = phone_result.replace('-','')
                
                while True:
                    if int(len(phone_result)) != 11:
                        phoneLen_error = '전화번호가 11자리가 아닙니다. 다시 말씀해주세요'
                        engine.say(phoneLen_error)
                        engine.runAndWait()
                        phone_result = ""
                        audio = r.listen(source, timeout=15, phrase_time_limit=15)  # 타임아웃 설정
                        phone_result = r.recognize_google(audio, language='ko-KR')
                        
                        if '-' in phone_result:
                            phone_result = phone_result.replace('-','')
                        print(phone_result)
                    
                    else:
                        break
                    
                infophone.delete(0,END)
                infophone.insert(END, phone_result)
            except sr.UnknownValueError:
                phone_result = '오디오 인식 불가'
                infophone.delete(0,END)
                infophone.insert(END, phone_result)
            except sr.RequestError as e:
                result = '에러 발생: {}'.format(e)
                infophone.delete(0,END)
                infophone.insert(END, phone_result)
        
    except KeyboardInterrupt:
        pass

    # 생년월일 받아오기
    text_birth = name_result + "님. 생년월일을 8자로 숫자만 말씀해주세요. 음성을 받는 시간은 15초입니다."
    engine.say(text_birth) 
    engine.runAndWait()
    brith_result = ""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=15, phrase_time_limit=15)  # 타임아웃 설정

            try:  # 예외처리 구문
                birth_result = r.recognize_google(audio, language='ko-KR')
                if '-' in birth_result:
                    birth_result = birth_result.replace('-','')
                    
                while True:
                    if int(len(birth_result)) != 8:
                        birthLen_error = '생년월일이 8자리가 아닙니다. 다시 말씀해주세요'
                        engine.say(birthLen_error)
                        engine.runAndWait()
                        birth_result = ""
                        audio = r.listen(source, timeout=15, phrase_time_limit=15)  # 타임아웃 설정
                        birth_result = r.recognize_google(audio, language='ko-KR')
                        if '-' in birth_result:
                            birth_result = birth_result.replace('-','')
                        print(birth_result)
                    
                    else:
                        break
                    
                infobirth.delete(0,END)
                infobirth.insert(END, birth_result)
            except sr.UnknownValueError:
                birth_result = '오디오 인식 불가'
                infobirth.delete(0,END)
                infobirth.insert(END, birth_result)
            except sr.RequestError as e:
                result = '에러 발생: {}'.format(e)
                infobirth.delete(0,END)
                infobirth.insert(END, birth_result)
        
    except KeyboardInterrupt:
        pass

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
go=Button(window, text='예매 창 넘어가기', font='Arial 12 bold', bg='black', fg='white', command=window.destroy)
go.grid(row=4, column=3, pady=5)
soundget=Button(window, text='음성안내', font='Arial 20',bg="#FFD700", command=callingSTT1) # 저시력자들이 잘 보는 짙은 노란색 사용
soundget.grid(row=3,column=3)
window.mainloop()

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
Enter_button = Button(Main_window, text='확인', bg='white', fg='black', command=readtime_gettime)
Enter_button.grid(row=5, column=1, columnspan=3, pady=20, sticky=E+W)
Main_window.mainloop()