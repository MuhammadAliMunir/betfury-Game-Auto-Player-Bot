from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from fake_useragent import UserAgent
import random
import time
import csv
from csv import writer
import os
from os import path
import random
import threading
import multiprocessing
import datetime
import zipfile

value = 1678
totalScroll = int(value/100)
# Searchword = "Ethereum"
def SearchWord(driver,wait,Searchword):
    rand = random.randint(3,10)
    ScrollPage(driver,rand * 100)
    wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div/div/input'))).click()
    searchBar = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div/div/input')))
    searchBar.clear()
    # Searchword = "bitcoin"
    characterList = list(Searchword)
    n=8
    characterList = [(Searchword[i:i+n]) for i in range(0, len(Searchword), n)]
    founded = True
    # time.sleep(1000)
    for character in characterList:
        searchBar.send_keys(character)
 
        lenth = 1
        checker = True
        time.sleep(5)

        while checker and lenth <= 5:
            try:
                subWait = WebDriverWait(driver, 5)                               #/html/body/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/ul[2]/li[1]/a/span[2]
                elem = subWait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/ul[2]/li['+str(lenth)+']/a/span[2]')))
                searchname = elem.text.lower()
                searchname = searchname.split(' (')
                searchname = searchname[0]
                
                searchkey = Searchword.lower()
                # print("searchkey: "+searchkey)
                # print("founname: "+searchname)
                if searchname == searchkey:
                    print('match')
                    difference = random.uniform(1,3)
                    time.sleep(difference)
                    wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/ul[2]/li['+str(lenth)+']/a'))).click()
                    # wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[4]/div/div/div/div/div[2]/div/div[2]/a['+str(lenth)+']/div'))).click()
                    # print('clicked...........................')
                    checker = False
                    founded = False
            except TimeoutException as ex:
                print(ex)
                # print('..................un clicked...........................')
                checker = True
            lenth = lenth + 1
        if not founded:
            break
    if  founded:
        print("note found")
        SearchWord(driver,wait,Searchword)
        # time.sleep(500)
        # driver.get("https://coinmarketcap.com/currencies/decoin/")
        print(driver.current_url)
    time.sleep(1)

def clickPairDesk(driver,wait):
    checker = False
    counter = 0
    while not checker and counter <= 5:
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="navigationTabMarketsChoice"]'))).click()
            searchBar = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div[8]/div/div[2]/div[2]/div/div[2]/div/div[1]/table/tbody[2]/tr[1]/td[3]/a')))
            searchBar.click()
            time.sleep(15)
            checker = True
        except:
            checker = False
            counter = counter + 1
            driver.execute_script("window.scrollBy(0, 300);")


def ScrollPage(driver,speed = 100):
    # scrollHight = driver.execute_script("return document.body.scrollHeight;")
    scrollHight = 500
    # print(scrollHight)
    totalScroll = int(scrollHight/speed)
    randomScroll = random.randint(0,totalScroll)
    totalScrollDown = randomScroll * speed
    # print('totalScrol Down: '+str(totalScrollDown)) 
    for i in range(randomScroll):
        # print('down')
        scrollDownSleep = random.randint(0,1)
        time.sleep(scrollDownSleep)
        driver.execute_script("window.scrollBy(0, "+str(speed)+");")
    # scrollBackWait = random.randint(0,2)
    # time.sleep(scrollBackWait)
    while totalScrollDown > -1:
        # print('up:'+str(totalScrollDown))
        scrollUpSleep = random.randint(0,1)
        time.sleep(scrollUpSleep)
        driver.execute_script("window.scrollTo(0, "+str(totalScrollDown)+");")
        totalScrollDown = totalScrollDown - speed
    driver.execute_script("window.scrollTo(0, 0);")
    driver.execute_script("window.scrollTo(0, 0);")
    # time.sleep(10)
def ScrollPageDown(driver,speed = 100):
    driver.execute_script("window.scrollBy(0, "+str(speed)+");")



def getDriver():
    
    options = Options()
    # options.add_extension(pluginfile)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_extension('proxy.zip')
    # path = 'C:\\pythonScripts\\cripto\\SEO automation\\cmc\\Cache\\Google\\Chrome\\User Data'
    # options.add_argument('--user-data-dir='+path)
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars") #// disabling infobars
    # options.add_argument("--disable-dev-shm-usage") #// overcome limited resource problems
    # options.add_argument("--no-sandbox") #// Bypass OS security model
    # options.add_argument('log-level=3')
    # prefs = {'profile.default_content_setting_values': {'stylesheet':2,'font':2,'permissions.default.stylesheet':2, 'images': 2,
    #                     'plugins': 2, 'popups': 2, 'geolocation': 2, 
    #                     'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
    #                     'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
    #                     'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
    #                     'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
    #                     'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
    #                     'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
    #                     'durable_storage': 2}}

    # options.add_experimental_option('prefs', prefs)

    # caps = DesiredCapabilities().CHROME
    # caps["pageLoadStrategy"] = "eager"
    # driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=options)
    driver = webdriver.Chrome( chrome_options=options)
    # driver = webdriver.Chrome()
    return driver

driver = getDriver()

wait = WebDriverWait(driver, 3)
driver.get("https://betfury.io/live/auto-roulette-2")
wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div/div/nav/div[2]/div/button[1]'))).click()
email = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div/div/div[1]/form/div[1]/div/input')))
email.clear()
email.send_keys("bet.fury@yandex.com")
password = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div/div/div[1]/form/div[2]/div/input')))
password.clear()
password.send_keys("Betfury.1")
wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div/div/div[1]/form/button'))).click()
input("Please select the game on browser and wait for load then press enter:")
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div/div/iframe"))
## Insert text via xpath ##
# elem = driver.find_element_by_xpath("/html/body/p")
# driver.switch_to.default_content()
# currentVallue = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div/span'))).text
# print(currentVallue)
# exit()
# profitArray = []
# for e in driver.find_elements_by_xpath("//*[name()='svg']/*[name()='g']") :
#     print e.get_attribute("id")
lastvalue = 0
while 2 > 1:                                                               #/html/body/div[4]/div/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div/span
    currentVallue = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div/span'))).text
    print("currentVallue"+str(currentVallue))
    if currentVallue == lastvalue:
        # print()
        continue
    try:
                                                              #/html/body/div[4]/div/div/div/div[3]/div[2]/div/div[1]/div/svg/g/path[38]
        # wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/div[2]/div/div[1]/div/svg/g/path[38]')))#.click()
        # wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/div[2]/div/div[1]/div/svg/g/path[39]')))#.click()
        base = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div/div/div/div[3]/div[2]/div/div[1]/div")))
        # elem = base.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[name()='svg']/*[name()='g']")))
        elem = base.find_element_by_xpath("//*[name()='svg']/*[name()='g']")
        # elem = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[name()='svg']/*[name()='g']/*[name()='path' and @data-bet-spot-id='middle2to1']")))
        print('click')

        print(elem.et_attribute("class"))
        print('click')
        lastvalue = currentVallue
    except:
        print('No click')

        continue



time.sleep(10)
# <svg height="840" version="1.1" width="757" xmlns="http://www.w3.org/2000/svg" style="overflow: hidden; position: relative;">
#             <image x="0" y="0" width="757" height="840" preserveAspectRatio="none">
#             <circle cx="272.34" cy="132.14">
#             <rect x="241.47" y="139.23">
#             <text style="text-anchor: middle; x="272.47" y="144.11">
#         </svg>