from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time

DayLightSavings = True

driver = webdriver.Chrome()

driver.get("http://localhost:1337/")

# Create user1 example
def CreateUser():
    
    element = driver.find_element_by_id("signup")
    
    element.click()
    
    element = driver.find_element_by_name("fname")
    
    element.send_keys("user")
    
    element = driver.find_element_by_name("lname")
    
    element.send_keys("1")
    
    element = driver.find_element_by_name("tel")
    
    element.send_keys("07XXXXXXXXX")
    
    element = driver.find_element_by_id("nPass")
    
    element.send_keys("pass1")
    
    element = driver.find_element_by_id("pConf")
    
    element.send_keys("pass1")
    
    element = driver.find_element_by_id("sBForm")

    element.submit()
    
    
# Login as a user1 example
def LoginAsUser():
    
    driver.get("http://localhost:1337/")
    
    element = driver.find_element_by_name("username")

    element.send_keys("user1")

    element = driver.find_element_by_name("password")

    element.send_keys("pass1")

    element = driver.find_element_by_id("lBForm")

    element.submit()
    

# Schedule a message
def ScheduleAMessage():
    
    if DayLightSavings == True:
        TimeDifference = 1
    else:
        TimeDifference = 0
    Now = datetime.now() + timedelta(hours=TimeDifference)
    Now = Now + timedelta(minutes=5)
    NowDate = str(Now)[0:10]
    Year = NowDate[0:4]
    Month = NowDate[5:7]
    Day = NowDate[8:10]
    NowDate = Day + "/" + Month + "/" + Year
    NowTime = str(Now)[11:16]
    
    element = driver.find_element_by_name("date")

    element.send_keys(NowDate)

    element = driver.find_element_by_name("time")

    element.send_keys(NowTime)

    element = driver.find_element_by_id("login")

    element.click()


CreateUser()
time.sleep(5)
LoginAsUser()
time.sleep(5)
ScheduleAMessage()
