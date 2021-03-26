import random , sys , traceback
from time import sleep
from selenium import webdriver
import datetime

c=1;

browser = webdriver.Chrome('D:\\Python\\Bot Insta\\chromedriver')
browser.get('https://google.com')
while c== 1:
    c=0
    try:
        browser.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[1]/ytd-topbar-logo-renderer/a/div[1]').click()
        print('am rulat ')
    except:
        c=1
        sleep(2)
        print('sunte in exceptie ')


print('gata')
# while browser.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[1]/ytd-topbar-logo-renderer/a/div[1]')==[]:
#     print("nu e bine nu gasim ce trebuie ")
#     sleep(2)
# print('am gasit')





#browser.close()
#browser.quit()