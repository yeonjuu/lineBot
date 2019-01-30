import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

f= open('info.txt', 'r')
while 1:
    data = f.readline()
    if not data : break
    else :
        c = data.split('/')         
        a = c[0] 
        b = c[1].strip() 

        url='https://notify-api.line.me/api/notify'

        token={}
        token['Authorization']='Bearer '+b 

        year =a

        driver = webdriver.Chrome('C:\\Users\\COM\\Desktop\\chromedriver_win32\\chromedriver')
        driver.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%9A%B4%EC%84%B8")
        #input_year = driver.find_element_by_name_id('srch_txt').send_keys('19981221')

        input_year = driver.find_element_by_xpath('//*[@id="srch_txt"]')
        input_year.send_keys(year)

        click_btn = driver.find_element_by_xpath('//*[@id="fortune_birthCondition"]/div[1]/fieldset/input').click()
        time.sleep(3)

        fortune1 = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/p')
        luck = fortune1.text
        print("★총운★\n"+luck)

        time.sleep(3)
        driver.find_element_by_class_name('birth_love').click()
        fortune2 = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/p')
        luck2 = fortune2.text
        print("♥애정운♥\n"+luck2)


        time.sleep(3)
        driver.find_element_by_class_name('birth_money').click()
        fortune3 = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/p')
        luck3 = fortune3.text
        print("§금전운§\n"+luck3)

        message = "\n'오늘의 운세'를 알려줄께!!\n\n" +"★총운★\n"+luck +"\n♥애정운♥\n"+luck2 +"\n§금전운§\n"+luck3+"\n\n\n그럼 안녕!"

        parameter = {'message' : message, "stickerId":117, "stickerPackageId":1}

        response = requests.post(
            url, headers=token, data =parameter)

        print(response.text)


 # time.sleep(3)
# driver.find_element_by_class_name('birth_company').click()
# fortune4 = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/p')
# print("♨직장운♨\n"+fortune4.text)

# time.sleep(3)
# driver.find_element_by_class_name('birth_study').click()
# fortune5 = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/p')
# print("♬학업운♬\n"+fortune5.text)