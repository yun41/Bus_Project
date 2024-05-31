import pyttsx3  # TTS 모듈 import 
import speech_recognition as sr  # STT 모듈 import
from tkinter import *

# 버스 시간(hour 단위)

# seoul_daejeon = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# seoul_daegu = [0,1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
# seoul_busan = [1,2,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# daejeon_seoul = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# daejeon_daegu = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# daejeon_busan = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# daegu_seoul = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# daegu_daejeon = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# daegu_busan = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# busan_seoul = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# busan_daejeon = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# busan_daegu = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

bus_time = [[[],
             [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
             [0,1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
             [1,2,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
            [[6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
             [],
             [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
             [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
            [[6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
             [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
             [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
             []]]

# 텍스트를 음성으로 변환하는 함수
def text_to_speech(text, callback=None):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    if callback:
        callback()  # 음성 출력 후 콜백 함수 호출

# 음성을 텍스트로 변환하는 함수
def speech_to_text(callback=None):
    global result
    while result not in city:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                label.config(text='음성을 입력하세요...')
                audio = r.listen(source)
                try:  # 예외처리 구문
                    result = r.recognize_google(audio, language='ko-KR')
                    label.config(text='음성 변환: ' + result)
                except sr.UnknownValueError:
                    result = '오디오 인식 불가'
                    label.config(text=result)
                except sr.RequestError as e:
                    result = '에러 발생: {}'.format(e)
                    label.config(text=result)
        except KeyboardInterrupt:
            pass
        
        if callback:
            callback(result)  # 음성 변환 후 콜백 함수 호출

# 음성 출력 후 음성을 입력받고 다시 음성으로 출력하는 함수
def handle_speech_to_text():
    result = speech_to_text()
    text_to_speech(result)

# Tkinter 윈도우가 열릴 때 자동으로 음성 출력
def on_window_load(string_input):
    initial_text = string_input
    text_to_speech(initial_text, handle_speech_to_text)

def seoul_departure():
    global result
    result = '서울'

def daejeon_departure():
    global result
    result = '대전'

def daegu_departure():
    global result
    result = '대구'

def busan_departure():
    global result
    result = '부산'

result = " "
# 버스 출발지/도착지
city = ['서울','대전','대구','부산']

# Tkinter 윈도우 생성 및 설정, Main_window는 출발지 입력을 위한 window
Main_window = Tk()
Main_window.title('음성안내 버스예매시스템')
Main_window.geometry("500x300")

label = Label(Main_window, text='안녕하세요.')
label.pack(pady=20)

# 다음 창을 생성하기 위해 이전 창 제거
button_next = Button(Main_window,text='다음',bg='white',fg='black',command=Main_window.quit)
button_next.pack()

f = Frame(Main_window)
f.pack()
# 음성인식이 안될 경우 버튼으로 선택
city_button_1 = Button(f,text='서울',bg='blue',fg='white',command=seoul_departure)
city_button_1.pack(side=LEFT)
city_button_2 = Button(f,text='대전',bg='black',fg='white',command=daejeon_departure)
city_button_2.pack(side=LEFT)
city_button_3 = Button(f,text='대구',bg='red',fg='white',command=daegu_departure)
city_button_3.pack(side=LEFT)
city_button_4 = Button(f,text='부산',bg='green',fg='black',command=busan_departure)
city_button_4.pack(side=LEFT)

# Tkinter 버튼 생성 (음성 입력 버튼은 수동으로 입력받기 위한 용도로 남겨둠)
listen_button = Button(Main_window, text="음성 입력", command=speech_to_text)
listen_button.pack(pady=10)

# Tkinter 이벤트 루프 시작 전에 자동 음성 출력을 예약
read_input = "안녕하세요. 음성 안내 버스예매 시스템입니다. 버스를 이용하실 출발지를 말씀해주세요."
Main_window.after(2000, on_window_load(read_input))

# Tkinter 이벤트 루프 시작
Main_window.mainloop()

result_departure = result
print(result_departure)

# 버스 노선도가 있는 도시 입력받으면 창 종료
if result_departure in city:
    Main_window.quit

result = ''

# 도착지 설정을 위한 두번째 화면 설정
second_window = Tk()
second_window.title('음성 안내 버스 예매 시스템')
second_window.geometry('500x300')

label = Label(second_window, text='안녕하세요.')
label.pack(pady=20)

listen_button = Button(second_window, text="음성 입력", command=speech_to_text)
listen_button.pack(pady=10)

button_next = Button(second_window,text='다음',bg='white',fg='black',command=second_window.quit)
button_next.pack()

f = Frame(second_window)

city_button_1 = Button(f,text='서울',bg='blue',fg='white',command=seoul_departure)
city_button_1.pack(side=LEFT)
city_button_2 = Button(f,text='대전',bg='black',fg='white',command=daejeon_departure)
city_button_2.pack(side=LEFT)
city_button_3 = Button(f,text='대구',bg='red',fg='white',command=daegu_departure)
city_button_3.pack(side=LEFT)
city_button_4 = Button(f,text='부산',bg='green',fg='black',command=busan_departure)
city_button_4.pack(side=LEFT)

f.pack()

# Tkinter 이벤트 루프 시작 전에 자동 음성 출력을 예약
read_input = "안녕하세요."+result+"를 선택하셨습니다. 도착지를 말씀해주세요."
second_window.after(1000, on_window_load(read_input))

result_arrival = result
print(result_arrival)
if result_arrival in city:
    second_window.quit()

# Tkinter 이벤트 루프 시작
second_window.mainloop()

print(result_departure, result_arrival)