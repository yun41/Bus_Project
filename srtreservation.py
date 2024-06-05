# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service

def open_browser():
    chrome_driver_path = "C:/chromedriver-win64/chromedriver.exe"  # 경로를 조정하세요
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    return driver

def login(driver, login_id, login_psw):
    driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'srchDvNm01').send_keys(str(login_id))
    driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(str(login_psw))
    driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
    driver.implicitly_wait(5)
    return driver

def search_train(driver, dpt_stn, arr_stn, dpt_dt, dpt_tm, num_trains_to_check=2):
    is_booked = False  # 예약 완료 되었는지 확인용

    driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')  # 기차 조회 페이지로 이동
    driver.implicitly_wait(5)

    # 출발지/도착지/출발날짜/출발시간 입력
    elm_dpt_stn = driver.find_element(By.ID, 'dptRsStnCdNm')
    elm_dpt_stn.clear()
    elm_dpt_stn.send_keys(dpt_stn)  # 출발지
    elm_arr_stn = driver.find_element(By.ID, 'arvRsStnCdNm')
    elm_arr_stn.clear()
    elm_arr_stn.send_keys(arr_stn)  # 도착지
    elm_dptDt = driver.find_element(By.ID, "dptDt")
    driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptDt)
    Select(driver.find_element(By.ID, "dptDt")).select_by_value(dpt_dt)  # 출발날짜
    elm_dptTm = driver.find_element(By.ID, "dptTm")
    driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptTm)
    Select(driver.find_element(By.ID, "dptTm")).select_by_visible_text(dpt_tm)  # 출발시간

    print("기차를 조회합니다")
    print(f"출발역:{dpt_stn}, 도착역:{arr_stn}\n날짜:{dpt_dt}, 시간: {dpt_tm}시 이후\n{num_trains_to_check}개의 기차 중 예약")

    driver.find_element(By.XPATH, "//input[@value='조회하기']").click()  # 조회하기 버튼 클릭
    driver.implicitly_wait(5)
    time.sleep(1)

    for i in range(1, num_trains_to_check + 1):
        try:
            standard_seat = driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7)").text

            if "예약하기" in standard_seat:
                print("예약 가능")
                driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7) > a").click()  # CSS Selector로 변경
                is_booked = True
                break
        except:
            continue

    if not is_booked:
        print("매진입니다")

    return driver

if __name__ == "__main__":
    driver = open_browser()
    driver = login(driver, 'srt아이디 입력', '비번 입력') #아이디와 비번 입력 부분 자신 껄로 입력
    search_train(driver, "동탄", "동대구", "20240613", "08")  # 기차 출발 시간은 반드시 짝수
