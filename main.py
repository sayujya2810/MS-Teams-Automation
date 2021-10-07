import datetime
import selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions
from webdriver_manager.chrome import ChromeDriverManager
# print('hello')

# Specify the path of teams.exe
# Make sure you are signed in to the teams before running the py code

# Getting the credentials from the .env file
load_dotenv()
password = os.getenv("PASSWORD")
emailAddress = os.getenv("EMAIL")




PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(executable_path = PATH)

driver2 = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://teams.microsoft.com/go#')
time.sleep(6)


emailID = driver.find_element_by_id("i0116")
emailID.send_keys(emailAddress)
emailID.send_keys(Keys.RETURN)
time.sleep(3)

pswrd = driver.find_element_by_id("i0118")
time.sleep(5)
pswrd.send_keys(password)
pswrd.send_keys(Keys.RETURN)
time.sleep(5)

# dontshowagain = driver.find_element_by_id("KmsiCheckboxField")
# dontshowagain.send_keys(Keys.RETURN)
time.sleep(2)
SignInYes = driver.find_element_by_id("idSIButton9")
SignInYes.send_keys(Keys.RETURN)

time.sleep(20)


# driver.quit()


className = driver.find_elements_by_class_name("team-card")
time.sleep(3)
teamBtn = driver.find_element_by_id("app-bar-2a84919f-59d8-4441-a975-2a8c2643b741")


def enterClass(index):
    className[index].click()
    time.sleep(3)
    joinBtn = driver.find_element_by_class_name("ts-calling-join-button")
    time.sleep(3)
    joinBtn.click()
    time.sleep(3)
    givePermissions()


def currentTime():
    t = int(datetime.datetime.now().strftime("%H%M"))
    return t

def currentDay():
    d = datetime.datetime.now().strftime("%A")
    return d

def waituntilThis(curr_t, class_time):
    while(curr_t < class_time):
        print("Waiting...")
        time.sleep(3)
        curr_t = currentTime()
        print("Time: ",curr_t)

def goHome():
    teamBtn.click()
    time.sleep(2)
    print("You are at home")

def listenForJoinBtn():
    while(len(joinBtn) < 1):
        print("Waiting for class to be started")
        time.sleep(4)


def givePermissions():
    time.sleep(3)
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.notifications": 1
    })
    driver = webdriver.Chrome(options=opt)

t = currentTime()
d = currentDay()
print(t)
print(d)

# if(d == "Wednesday"):
#     while(t < 951):
#         time.sleep(3)
#         print("waiting...")
#         current_time = int(datetime.datetime.now().strftime("%H%M"))
#         print(current_time)
#         continue
#     print("opening the class page")
#     className[0].click()
#     print("opened the class page")

#     while(t<1400):
#         time.sleep(3)
#         print("waiting...")

if(d == "Monday"):
    waituntilThis(t,951)
    enterClass(3)
    waituntilThis(t,1130)
    goHome()
    waituntilThis(t,1502)
    enterClass(8)
    waituntilThis(t,1550)
    goHome()
    waituntilThis(t,1602)
    enterClass(7)
    waituntilThis(t,1650)
    goHome()
    waituntilThis(t,1702)
    enterClass(6)
    waituntilThis(t,1750)
    goHome()

if(d == "Tuesday"):
    waituntilThis(t,1140)
    enterClass(9)
    waituntilThis(t,1320)
    goHome()
    waituntilThis(t,1400)
    enterClass(6)
    waituntilThis(t,1450)
    goHome()
    waituntilThis(t,1500)
    enterClass(1)
    waituntilThis(t,1550)
    goHome()
    waituntilThis(t,1660)
    enterClass(4)
    waituntilThis(t,1650)
    goHome()
    waituntilThis(t,1660)
    enterClass(5)
    waituntilThis(t,1650)
    goHome()


if(d == "Wednesday"):
    waituntilThis(t,951)
    enterClass(9)
    waituntilThis(t,1130)
    goHome()
    waituntilThis(t,1400)
    enterClass(5)
    waituntilThis(t,1450)
    goHome()
    waituntilThis(t,1600)
    enterClass(8)
    waituntilThis(t,1650)
    goHome()
    waituntilThis(t,1700)
    enterClass(7)
    waituntilThis(t,1750)
    goHome()

if(d == "Thursday"):
    waituntilThis(t,1140)
    enterClass(2)
    waituntilThis(t,1310)
    goHome()
    waituntilThis(t,1140)
    enterClass(2)
    waituntilThis(t,1310)
    goHome()
    waituntilThis(t,1400)
    enterClass(7)
    waituntilThis(t,1450)
    goHome()
    waituntilThis(t,1500)
    enterClass(6)
    waituntilThis(t,1550)
    goHome()
    waituntilThis(t,1600)
    enterClass(1)
    waituntilThis(t,1650)
    goHome()

if(d == "Friday"):
    waituntilThis(t,1200)
    enterClass(10)
    waituntilThis(t,1250)
    goHome()
    waituntilThis(t,1400)
    enterClass(4)
    waituntilThis(t,1450)
    goHome()
    waituntilThis(t,1500)
    enterClass(5)
    waituntilThis(t,1550)
    goHome()
