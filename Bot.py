# Bot pentru instagram cu Mircea Test commit form browsers
import random
from time import sleep
from selenium import webdriver
import datetime
parola="acum vrei sa mi vezi si parola... da un follow macar la id-ul ala"
id="cats_on_screens"
#codul de securitate ( trebuie sa fie un cod de  securitate universal valid, nu cel din mesaj)
cod='10294387'
# durata intre 2 reprize de unfollow ( in secunde )
d= 7200
# numarul de unfollow pentru o repriza
n=35
# timp extra, daca calculatorul tau merge mai greu si nu are timp sa incarce pagina, mai baga niste tinmp. este in secunde
extra= 0;
# variabila pe eroare
ero=1;
def unfollow():
    print('sunt in functie  ')
    sleep(extra + 30 + 5 + random.uniform(-2, 2))
    c= 1;
    da=3;
    global ero
    for i in range(n + int(random.uniform(-3,3))):
        if i %20==0 and i!=0 :
            browser.get('https://www.instagram.com/cats_on_screens/following/')
            sleep(extra + 10 + 5 + random.uniform(-2, 2))
            while ero == 1:
                ero = 0;
                try:
                    browser.find_element_by_partial_link_text('following').click()
                except:
                    ero = 1;
                    print('a aparut o eroare, incercam remedierea acesteia ')
                    sleep(10);
            ero = 1;
            sleep(extra + 30 + 5 + random.uniform(-2, 2))
            c=1
        while ero == 1:
            ero = 0;
            try:
                browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[' + str(c)+']/div/div['+str (da)+']/button').click()

            except:
                ero = 1;
                print('a aparut o eroare, incercam remedierea acesteia, fix aici frate')
                if(da == 2 ):
                    da=3;
                else:
                    da=2;
                sleep(10);
        ero = 1;

        sleep(extra + 5 + random.uniform(-2, 2))
        while ero == 1:
            ero = 0;
            try:
                browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
            except:
                ero = 1;
                print('a aparut o eroare, incercam remedierea acesteia ')
                sleep(10);
        ero = 1;

        print( 'am dat '+ str(i+1)+' unfollow');
        sleep(extra + 5 + random.uniform(-2, 2))
        c=c+1
    print('am terminat cu unfollow ')
    print(datetime.datetime.now())
    return 0
while 1:
    browser = webdriver.Chrome('D:\\Python\\Bot Insta\\chromedriver')
    browser.get('https://www.instagram.com/accounts/login/')
    sleep(extra + 5 + random.uniform(-2,2))
    # introducem id-il
    while ero==1:
        ero=0;
        try:
            browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(id)
            print('am bagat id-ul')
        except:
            ero=1;
            print('a aparut o eroare, incercam remedierea acesteia ')
            sleep(10);
    ero = 1;
    # introducem si parola
    sleep(extra + 5 + random.uniform(-2,2))
    while ero==1:
        ero=0;
        try:
            browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(parola)
            print('am bagat id-ul')
        except:
            ero=1;
            print('a aparut o eroare, incercam remedierea acesteia ')
            sleep(10);
    ero = 1;
    # dam click pe log in
    sleep(extra +5 + random.uniform(-2,2))
    while ero==1:
        ero=0;
        try:
            browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]').click()
            print('am apasat log in')
        except:
            ero=1;
            print('a aparut o eroare, incercam remedierea acesteia ')
            sleep(10);
    ero=1;
    # aici daca vrei cu cod e putin mai complicat, momentan lasam fara, dar optiunea se poate realiza
    # introduc codul de pe teleofn
    # sleep(extra +5 + random.uniform(-2,2))
    # browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input').send_keys(cod)
    # # dau click
    # sleep(extra +5 + random.uniform(-2,2))
    # browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/button').click()
    # #apasa ca nu vrei acum sa setezi ca un browser sigur
    # sleep(extra +5 + random.uniform(-2,2))
    # browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()

    # nu salvezi datele de logare
    sleep(extra +5 + random.uniform(-2,2))
    while ero==1:
        ero=0;
        try:
            browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
            print('am trecut de salvarea parolei  ')
        except:
            ero=1;
            print('a aparut o eroare, incercam remedierea acesteia ')
            sleep(10);
    ero = 1;

    # nu vrei notificari acum
    sleep(extra +5 + random.uniform(-2,2))
    eroare1 = '/html/body/div[4]/div/div/div/div[3]/button[2]'
    while ero==1:
        ero=0;
        try:


            browser.find_element_by_xpath(eroare1).click()

            print('am trecut de notificari ')
        except:
            ero=1;
            eroare1='/html/body/div[1]/section/main/div/div/div/div/button'
            print('am inlocuit xpathul')
            print('a aparut o eroare, incercam remedierea acesteia ')
            sleep(10);
    ero = 1;

    # du-te la persoanele pe care le  urmaresti
    sleep(extra +5 + random.uniform(-2,2))
    browser.get('https://www.instagram.com/cats_on_screens/following/')
    sleep(extra +10 +5 + random.uniform(-2,2))
    while ero==1:
        ero=0;
        try:
            browser.find_element_by_partial_link_text('following').click()
            print('am deschis fereasta de following  ')
        except:
            ero=1;
            print('a aparut o eroare, incercam remedierea acesteia ')
            sleep(10);
    ero = 1;

    # acum dam unfollow
    unfollow()
    print('am iesit din functie ')
    browser.close()
    print(' am inchis')
    sleep(d + random.uniform(-1800, 1800))
    print('am terminat de asteptat')


# Sa ai o zi frumoasa!



