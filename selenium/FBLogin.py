from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def FBlogin(mail_address, password):
    # Login Page
    driver.get(
        'https://www.facebook.com/')
    
    # input Gmail
    driver.find_element_by_id("email").send_keys(mail_address)
    # driver.find_element_by_id("identifierNext").click()
    # driver.implicitly_wait(10)
  
    # input Password
    driver.find_element_by_id("pass").send_keys(password)
    driver.implicitly_wait(3)
    driver.find_element_by_id("loginbutton").click()
    driver.implicitly_wait(10)
  
    # # go to google home page
    # driver.get('https://google.com/')
    # driver.implicitly_wait(100)


opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
  
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Firefox(executable_path="C:\\Automation\\selenium\\drivers\\geckodriver.exe")

mail_address = ''
password = ''

FBlogin(mail_address, password)
