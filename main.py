from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
import time
from Run import credential as cred

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
home_page = "https://1xbet.ng"

def login():
    # Getting the page
    driver.get(home_page)
    driver.implicitly_wait(10)

    # Clicking the login button
    login_btn = driver.find_element(By.CSS_SELECTOR, "span[class='user-control-panel__group user-control-panel__group--auth'] button")
    login_btn.click()

    auth_id = driver.find_element(By.CSS_SELECTOR, "input[id='username']")
    auth_id.send_keys(cred.id)
    
    auth_passwd = driver.find_element(By.CSS_SELECTOR, "input[id='username-password']")
    auth_passwd.send_keys(cred.password)

    # # submit form
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()
    # # Submitting password

login()
# privent driver from closing
time.sleep(30)
