from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time 
import os
import getopt
import sys
from webdriver_manager.chrome import ChromeDriverManager

# GLOBAL VARS
given_arg = ""
users = ["test", "ryan"]
passwords = ["test", "test"]
test_room = 172

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def GetArgs(): 
    # setting options
    try:
        opts,args = getopt.getopt(sys.argv[1:], "ci:")
    except:
        print(f"{bcolors.FAIL}Argument doesn't exist. Please use '-c' or no arguments to start, program closing...{bcolors.ENDC}")
        sys.exit(2)

    # No args given do standard
    if len(opts) == 0:
        return

    # Check args
    for opt,args in opts:
        if opt == "-c":
            print("Creating project")
            global given_arg
            given_arg = 'creating'
            return

def Login(name, password):
    # wait till the input can be filled, than fill the login
    selected_driver = 0
    for drive in driver:

        drive.implicitly_wait(3)
        name_input = drive.find_element(By.NAME, "login")
        pw_input = drive.find_element(By.NAME, "password")
        print("Trying to log in with: " + name[selected_driver] + " " + password[selected_driver])
        # fill the fields and login
        name_input.clear()
        name_input.send_keys(name[selected_driver])
        pw_input.clear()
        pw_input.send_keys(password[selected_driver])
        pw_input.submit()
        selected_driver += 1

def JoinProject(id):
    # Go to join page
    for drive in driver:
        
        # need to wait for transistion to be done
        time.sleep(1)

        join_element = drive.find_element(By.CLASS_NAME, "fa-arrow-right-to-bracket")
        join_element.click()
    
    if not CheckByMultipleUrl('http://codojo.made-by-s.id:8060/JoinProject'):
        print(f"{bcolors.FAIL}Failed to go to JoinprojectPage. Drivers closing...{bcolors.ENDC}")
        CloseDrivers()

    for drive in driver:

        # entering code and go to editor
        time.sleep(1)

        new_proj_input = drive.find_element(By.NAME, "newproj")
        new_proj_input.send_keys(id)
        new_proj_input.submit()
        print("Joining room...")

    if not CheckByMultipleUrl('http://codojo.made-by-s.id:8060/Editor'):
        print(f"{bcolors.FAIL}Failed to go to EditorPage. Drivers closing...{bcolors.ENDC}")
        CloseDrivers()
    else:
        print(f"{bcolors.OKGREEN}Join succesful, joined room {id}{bcolors.ENDC}")

def CreateProject(id):
    print(id)

def CheckRoomMembers():

    parent_element = driver[0].find_element(By.CLASS_NAME, "popover-content")
    joined_users = driver[0].find_elements(By.TAG_NAME, "h6")
    print(parent_element)
    for user in joined_users:
        print(user.text)

def SendRoomMessage():
    msg_amount = 0
    print("sending messages...")
    for drive in driver:
        
        # need to wait for transistion to be done
        time.sleep(1)

        # open chat
        chat_element = drive.find_element(By.CLASS_NAME, "fa-message")
        chat_element.click()

        # send messages
        chat_input = drive.find_element(By.CLASS_NAME, "message-text")
        chat_input.send_keys("Hey!")
        chat_input.submit()

        # change the count so we can compare them
        msg_amount += 1

        # compare amount of divs
        element_amount = len(drive.find_elements(By.CLASS_NAME, "user-message"))
        element_amount += len(drive.find_elements(By.CLASS_NAME, "user-message-public"))

    if element_amount == msg_amount:
        print(f"{bcolors.OKGREEN}{element_amount}/{msg_amount} messages sent{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}{element_amount}/{msg_amount} messages sent{bcolors.ENDC}")

def CheckByMultipleUrl(supposed_url):
    # rather use cookies for login
    # for now just return if we are on the page
    time.sleep(1)
    for drive in driver:
        if drive.current_url != supposed_url:
            return False
    return True

def CloseDrivers():
    for drive in driver:
        print(f"closed on {drive.current_url}")
        drive.quit()
    exit()

GetArgs()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = [ webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options), webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options) ]

# start driver
for drive in driver:
    drive.get("http://codojo.made-by-s.id:8060/")

# wrong login
Login(["hoi", "doei"], ["wat", "oke"])

if not CheckByMultipleUrl('http://codojo.made-by-s.id:8060/Home'):
    print(f"{bcolors.OKGREEN}Login should be incorrect and it should be{bcolors.ENDC}")

# correct login
Login(users, passwords)
# make sure both are correct
if CheckByMultipleUrl('http://codojo.made-by-s.id:8060/Home'):
    print(f"{bcolors.OKGREEN}Login correct, logging in...{bcolors.ENDC}")
else:
    print(f"{bcolors.FAIL}Login incorrect. Drivers closing...{bcolors.ENDC}")
    CloseDrivers()

if given_arg == "creating":
    CreateProject(105)
else:
    JoinProject(test_room)

SendRoomMessage()

# end driver
CloseDrivers()
