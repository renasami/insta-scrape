#coding=utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import random
import time
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path='static/chromedriver')

class User():
    def __init__(self, userName, passWord, use_chrome=True):
        self.userName = userName
        self.passWord = passWord
        self.use_chrome = use_chrome
        self.driver = self.init_driver()

    def init_driver(self):
        if self.use_chrome:
            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Chrome(executable_path='static/chromedriver')
        else:
            driver = webdriver.PhantomJS()
        return driver
    
    def login(self):
        driver.get('https://www.instagram.com')
        time.sleep(3)
        idSelector = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
        pwSelector = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
        idSelector.send_keys(self.userName)
        pwSelector.send_keys(self.passWord)
        button = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
        button.click()
        time.sleep(5)

    def search(self, Word):
        search = 'https://www.instagram.com/explore/tags/'+ Word +'/'
        driver.get(search)
        time.sleep(5)
        for n in range(10):
            for m in range(3):
                posted = driver.find_element_by_css_selector('#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(' + str(n + 1) + ') > div:nth-child(' + str(m + 1) + ') > a')
                posted.click()
                time.sleep(2)
                follow = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button')
                if follow.text == 'フォローする':
                    follow.click()
                back = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button')
                back.click()
                time.sleep(2)
    
    def unfollow(self):
        driver.get('https://www.instagram.com/' + self.userName)
        followingNum = driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span').text
        following = driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a ')
        n = int(followingNum)
        print(n)
        time.sleep(5)
        following.click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        for s in range(30):
            button = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(' + str(n - s) + ') > div > div.Pkbci > button')
            button.click()
            time.sleep(0.5)
    
    def getFollower(self, accountId):
        print()
        
        
def main():
    print('hello')
    print('Welcome to Instagram-Scraper')
    print('')
    name = input('type your instagram username >')
    print('')
    pas = input('type your password >')
    st = User(name, pas)
    print('type the number what you wanna do')
    print('1:フォロー,2:フォロー解除\n3:特定アカウントのフォロワーのフォロー,4:いいね')
    change = input('>')
    if change == "1":
        print("mode 1")
        Word = input("type word for serach >")
        st.login()
        st.search(Word)
    elif change == "2":
        print("mode 2")
        st.login()
        st.unfollow()
    elif change == "3":
        print("mode 3")
        accountId = input('type the account you get follower>')
        st.login()
        st.getFollower(accountId)
    elif change == "4":
        print("mode 4")
    else:
        print("fuck")    
    st.login()


main()
        

