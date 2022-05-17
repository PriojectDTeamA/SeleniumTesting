from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time 
import os
from webdriver_manager.chrome import ChromeDriverManager

# GLOBAL VARS
dir_path = os.path.dirname(os.path.realpath(__file__))
PATH = f"{dir_path}/driver/chromedriver.exe"
driver = webdriver.Chrome(service = Service(PATH))

# too lazy to download chromedriver urself? use this line.
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def Login(name, password):
    # wait till the input can be filled, than fill the login
    driver.implicitly_wait(3)
    name_input = driver.find_element(By.NAME, "login")
    pw_input = driver.find_element(By.NAME, "password")

    # fill the fields and login
    name_input.clear()
    name_input.send_keys(name)
    pw_input.clear()
    pw_input.send_keys(password)
    pw_input.submit()

def CheckByUrl(supposed_url):
    # rather use cookies for login
    # for now just return if we are on the page
    time.sleep(0.1)
    return driver.current_url == supposed_url

# start driver
driver.get("http://codojo.made-by-s.id:8060/")

# wrong login
Login("hoi", "doei")
print(f"{CheckByUrl('http://codojo.made-by-s.id:8060/Home')},(should be false)")

# correct login
Login("test", "test")
print(f"{CheckByUrl('http://codojo.made-by-s.id:8060/Home')},(should be true)")

# end driver
driver.quit()