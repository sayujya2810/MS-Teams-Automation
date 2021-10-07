import datetime
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# print('hello')

# Specify the path of teams.exe
# Make sure you are signed in to the teams before running the py code

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://teams.microsoft.com/go#')
time.sleep(6)


emailID = driver.find_element_by_id("i0116")
print(emailID)
emailID.send_keys("")
emailID.send_keys(Keys.RETURN)
time.sleep(3)

pswrd = driver.find_element_by_id("i0118")
time.sleep(5)
pswrd.send_keys("")
pswrd.send_keys(Keys.RETURN)
time.sleep(5)

# dontshowagain = driver.find_element_by_id("KmsiCheckboxField")
# dontshowagain.send_keys(Keys.RETURN)
time.sleep(2)
SignInYes = driver.find_element_by_id("idSIButton9")
SignInYes.send_keys(Keys.RETURN)

time.sleep(30)


# driver.quit()


className = driver.find_elements_by_class_name("team-card")
time.sleep(3)
teamBtn = driver.find_element_by_id("app-bar-2a84919f-59d8-4441-a975-2a8c2643b741")


def joinClass(index):
    className[index].click()

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
    joinClass(3)
    waituntilThis(t,1130)
    goHome()
    waituntilThis(t,1502)
    joinClass(8)
    waituntilThis(t,1550)
    goHome()
    waituntilThis(t,1602)
    joinClass(7)
    waituntilThis(t,1650)
    goHome()
    waituntilThis(t,1702)
    joinClass(6)
    waituntilThis(t,1750)
    goHome()

if(d == "Tuesday"):
    waituntilThis(t,1140)
    joinClass(9)
    waituntilThis(t,1320)
    goHome()
    waituntilThis(t,1400)
    joinClass(6)
    waituntilThis(t,1450)
    goHome()
    waituntilThis(t,1500)
    joinClass(1)
    waituntilThis(t,1550)
    goHome()
    waituntilThis(t,1660)
    joinClass(4)
    waituntilThis(t,1650)
    goHome()
    waituntilThis(t,1660)
    joinClass(5)
    waituntilThis(t,1650)
    goHome()


if(d == "Wednesday"):
    waituntilThis(t,951)
    joinClass(9)
    waituntilThis(t,1130)
    goHome()
    waituntilThis(t,1400)
    joinClass(5)
    waituntilThis(t,1450)
    goHome()
    waituntilThis(t,1600)
    joinClass(8)
    waituntilThis(t,1650)
    goHome()
    waituntilThis(t,1700)
    joinClass(7)
    waituntilThis(t,1750)
    goHome()

if(d == "Thursday"):
    waituntilThis(t,1140)
    joinClass(2)
    waituntilThis(t,1310)
    goHome()
    waituntilThis(t,1140)
    joinClass(2)
    waituntilThis(t,1310)
    goHome()
    waituntilThis(t,1400)
    joinClass(7)
    waituntilThis(t,1450)
    goHome()
    waituntilThis(t,1500)
    joinClass(6)
    waituntilThis(t,1550)
    goHome()
    waituntilThis(t,1600)
    joinClass(1)
    waituntilThis(t,1650)
    goHome()

if(d == "Friday"):
    waituntilThis(t,1200)
    joinClass(10)
    waituntilThis(t,1250)
    goHome()
    waituntilThis(t,1400)
    joinClass(4)
    waituntilThis(t,1450)
    goHome()
    waituntilThis(t,1500)
    joinClass(5)
    waituntilThis(t,1550)
    goHome()
