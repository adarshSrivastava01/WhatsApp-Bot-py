from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.chrome.options import Options
import time
option=Options()
option.add_argument('user-data-dir=selenium')
print("WHATSAPP-JARVIS by Adarash Srivastava")
print("ENTER ANY KEY TO CONTINUE")
input("")

driver = webdriver.Chrome('C:\webdrivers\chromedriver', options=option)
driver.get("https://web.whatsapp.com/")
input("After Scanning enter any Key To Continue:    ")

def name_input():
    user_name = input('Whom do you want to send the Message:  ')
    chat = driver.find_element_by_xpath('//span[text()="%s"]'%(user_name))
    chat.click()

def text():
    block = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    times = int(input('Enter The No. of Times You want to send Message: '))
    message = input('Enter the Text you want to send: ')
    for i in range(1,times+1):
            block.send_keys(message)
            block.send_keys(Keys.RETURN)
            time.sleep(3)

