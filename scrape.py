import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()
USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("https://smartinterviews.in/")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

Login = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/layout-header/nav/div/div[2]/ul/li[6]/a/span/span')))
Login.click()

UserName = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="autofocus"]')))
UserName.send_keys(USER_NAME)

Password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
Password.send_keys(PASSWORD)

driver.find_element_by_xpath('/html/body/app-root/auth-page/div/div/mat-card/form/button').click()

time.sleep(10)
driver.find_element_by_xpath('/html/body/app-root/layout-header/nav/div/div[2]/ul/li[5]/a/span/span').click()

time.sleep(10)
driver.find_element_by_xpath('//*[@id="mat-chip-list-0"]/div/mat-chip').click()

time.sleep(15)
driver.find_element_by_xpath('/html/body/app-root/app-leaderboard/div/div/div[3]/a/mat-icon').click()

## Done Util Opening Batch Report

# TODO: Add batch data to mogodb database