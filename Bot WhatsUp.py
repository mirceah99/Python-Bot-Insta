from random import *
from selenium import webdriver
from time import sleep
def text():
    litere=['e','i','u','b','s','c','t',' ']
    t='';
    for i in range(9):
        t=t + litere[randint(0,7)]
    return t;

bara='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'
''
browser = webdriver.Chrome('D:\\Python\\Bot Insta\\chromedriver')
browser.get('https://web.whatsapp.com/')
sleep(20)

bara=browser.find_element_by_xpath(bara);
bara.send_keys('incepem');
sleep(2)

trimite=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')

trimite.click();
c=1
while c==1:

    t=text()
    bara.send_keys(t)
    sleep(0.3)
    ero =1
    while  ero==1:
        ero=0
        try:
            trimite=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
            trimite.click()
        except:
            sleep(0.3)
            ero=1

    if t=='te iubesc mult':
        c=0
        break

#print (len('bcccllmubc c'))
#print('lungimea este ' + str(len('te iubesc mult')))
c=1
# while c==1:
#     t = text()
#     print(t)
#     print(str(len(t))+ ' ' + str(len('te iubesc')))
#     if t=='te iubesc':
#         break
#         c=0
