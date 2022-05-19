import time, os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def login(Username, Key):
    username_input = driver.find_element(By.NAME, "login")
    key_input = driver.find_element(By.NAME, "password")

    driver.implicitly_wait(3)

    username_input.send_keys(Username)
    key_input.send_keys(Key)

    key_input.submit()

def clearfields():
    username_input = driver.find_element(By.NAME, "login")
    key_input = driver.find_element(By.NAME, "password")

    username_input.clear()
    key_input.clear()

Checklink = lambda target : driver.current_url == target

driver.get("http://codojo.made-by-s.id:8060/")

# login("hoi", "doei")
# print(f"{Checklink('http://codojo.made-by-s.id:8060/Home')},(should be false)")

# clearfields()

login("test", "test")
print(f"{Checklink('http://codojo.made-by-s.id:8060/Home')},(should be true)")
