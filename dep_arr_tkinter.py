from tkinter import *

dep_arr = []

def seoul():
    global city
    city='서울'
def busan():
    global city
    city='부산'
def daejeon():
    global city
    city='대전'
def daegu():
    global city
    city='대구'


arr_window = Tk()
arr_window.title('출발지 입력')
arr_window.geometry('500x300')

label_1 = Label(arr_window, text='안녕하세요. 도착지를 골라주세요')
label_1.grid(row=0,column=0)
label_2 = Label(arr_window, text='서울,부산,대전,대구 중에 골라주세요')
label_2.grid(row=1,column=0)

# 다음 창을 생성하기 위해 이전 창 제거 버튼 추가
button_next = Button(arr_window,width=10, text='다음',bg='black',fg='white',command=arr_window.quit)
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

dep_arr.append(city)
print(dep_arr)

dep_window = Tk()
dep_window.title('출발지 입력')
dep_window.geometry('500x300')

label_1 = Label(dep_window, text='안녕하세요. 출발지를 골라주세요')
label_1.grid(row=0,column=0)
label_2 = Label(dep_window, text='서울,부산,대전,대구 중에 골라주세요')
label_2.grid(row=1,column=0)

# 선택 완료 버튼 추가
button_next = Button(dep_window,width=10, text='선택완료',bg='black',fg='white',command=dep_window.quit)
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

# dep_arr[0]이 출발지, dep_arr[1]은 도착지
dep_arr.append(city)
print(dep_arr)