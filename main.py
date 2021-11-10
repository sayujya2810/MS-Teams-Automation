from ctypes import pythonapi, set_last_error
import datetime
from functools import cache
import os
import time
import pyautogui
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
driver = webdriver.Chrome(executable_path=PATH)

# driver2 = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://teams.microsoft.com/go#')
time.sleep(6)


emailID = driver.find_element_by_id("i0116")
print("Entering Email ID...")
emailID.send_keys(emailAddress)
emailID.send_keys(Keys.RETURN)
time.sleep(3)

pswrd = driver.find_element_by_id("i0118")
print("Entering Password...")
time.sleep(5)
pswrd.send_keys(password)
pswrd.send_keys(Keys.RETURN)
time.sleep(5)

# dontshowagain = driver.find_element_by_id("KmsiCheckboxField")
# dontshowagain.send_keys(Keys.RETURN)
time.sleep(2)
SignInYes = driver.find_element_by_id("idSIButton9")
print("Entered yes button")
SignInYes.send_keys(Keys.RETURN)

time.sleep(20)
print("Loading MS Teams...")

# driver.quit()


className = driver.find_elements_by_class_name("team-card")
time.sleep(3)
teamBtn = driver.find_element_by_id(
    "app-bar-2a84919f-59d8-4441-a975-2a8c2643b741")


def enterClass(day, index):
    className[index].click()
    time.sleep(3)
    print("Entered the class")
    try:
        changeChannel(day, index)
    except:
        print("No need to change any channel / Some error occured")

    time.sleep(3)
    join_btn = listenForJoinBtn()
    time.sleep(3)
    join_btn.click()
    time.sleep(3)
    # givePermissions()
    # time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    print('Allowed Cam and Mic permissions')
    time.sleep(2)
    try:
        cam = driver.find_element_by_css_selector(
            "span[title='Turn camera off']")
        cam.click()
        time.sleep(1)
        mic = driver.find_element_by_css_selector(
            "span[title='Mute microphone']")
        mic.click()
    except:
        print("Mic and Cam already off")

    try:
        time.sleep(2)
        join = driver.find_element_by_css_selector(
            "button[ng-click='ctrl.joinMeeting()']")
        join.click()
    except:
        print("Err in joinings")


def currentTime():
    t = int(datetime.datetime.now().strftime("%H%M"))
    return t


def currentDay():
    d = datetime.datetime.now().strftime("%A")
    return d


def wait_until_found(sel, timeout, driver):
    try:
        element_present = EC.visibility_of_element_located(
            (By.CSS_SELECTOR, sel))
        WebDriverWait(driver, timeout).until(element_present)
        return driver.find_element_by_css_selector(sel)
    except exceptions.TimeoutException:
        print(f"Timeout waiting for element: {sel}")
        return None


def waituntilThis(curr_t, class_time, end_time, index, day):
    curr_t = currentTime()
    while curr_t < class_time:
        print("Waiting...")
        time.sleep(3)
        if curr_t > class_time:
            break
        curr_t = currentTime()
        print("Time: ", curr_t)
        break
    if(curr_t > class_time and curr_t < end_time):
        enterClass(day, index)
    if(curr_t > end_time):
        goHome()


def changeChannel(day, index):
    if(day == "Wednesday" and index == 5):
        time.sleep(3)
        labChannel = driver.find_element_by_id(
            "channel-19:1IaV-1OEkQRheFliEQ8oaB3Sf6KetAzX5LLDJ2PIvSY1@thread.tacv2")
        labChannel.click()

    if(day == "Monday" and index == 7):
        time.sleep(3)
        monChannel = driver.find_element_by_css_selector("a[title = 'Monday']")
        monChannel.click()
    if(day == "Wednesday" and index == 7):
        time.sleep(3)
        monChannel = driver.find_element_by_css_selector(
            "a[title = 'Wednesday']")
        monChannel.click()
    if(day == "Thursday" and index == 7):
        time.sleep(3)
        monChannel = driver.find_element_by_css_selector(
            "a[title = 'Thursday']")
        monChannel.click()


def goHome():
    teamBtn.click()
    time.sleep(2)
    print("You are at home")


def listenForJoinBtn():
    joinBtn = wait_until_found(
        "button[ng-click='ctrl.joinCall()']", 10, driver)
    while(joinBtn is None):
        print("Waiting for class to be started")
        time.sleep(4)
        joinBtn = wait_until_found(
            "button[ng-click='ctrl.joinCall()']", 10, driver)
    return joinBtn


# def givePermissions():
#     time.sleep(3)
#     opt = Options()
#     opt.add_argument("--disable-infobars")
#     opt.add_argument("start-maximized")
#     opt.add_argument("--disable-extensions")
#     opt.add_experimental_option("prefs", { \
#         "profile.default_content_setting_values.media_stream_mic": 1,
#         "profile.default_content_setting_values.media_stream_camera": 1,
#         "profile.default_content_setting_values.notifications": 1
#     })
#     driver = webdriver.Chrome(options=opt)

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
    waituntilThis(t, 951, 1130, 3, d)
    waituntilThis(t, 1500, 1550, 8, d)
    waituntilThis(t, 1600, 1650, 7, d)
    waituntilThis(t, 1700, 1750, 6, d)
    print("End of the Day brother!!")

if(d == "Tuesday"):
    waituntilThis(t, 957, 1320, 9, d)
    waituntilThis(t, 1400, 1450, 6, d)
    waituntilThis(t, 1500, 1550, 1, d)
    waituntilThis(t, 1600, 1650, 4, d)
    waituntilThis(t, 1700, 1750, 5, d)
    print("End of the Day brother!!")


if(d == "Wednesday"):
    waituntilThis(t, 1700, 1750, 7, d)
    waituntilThis(t, 1600, 1650, 8, d)
    waituntilThis(t, 1400, 1450, 5, d)
    waituntilThis(t, 951, 1130, 9, d)
    print("End of the Day brother!!")

if(d == "Thursday"):
    waituntilThis(t, 1600, 1650, 1, d)
    waituntilThis(t, 1500, 1550, 6, d)
    waituntilThis(t, 1400, 1450, 7, d)
    waituntilThis(t, 1140, 1310, 2, d)
    print("End of the Day brother!!")

if(d == "Friday"):
    waituntilThis(t, 1500, 1550, 5, d)
    waituntilThis(t, 1400, 1450, 4, d)
    waituntilThis(t, 1200, 1250, 10, d)
    print("End of the Day brother!!")
