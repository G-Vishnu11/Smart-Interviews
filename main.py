import time
import os
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv() # Loading Environment Varialbles

def getMongoCloud():
  return os.environ.get("MONGO_CLOUD")

def getUserName():
  return os.environ.get("USER_NAME")

def getPassword():
  return os.environ.get("PASSWORD")

def connectToDB():
  client = MongoClient(getMongoCloud())
  db = client["SmartInterviews"]
  collection = db["GRIET2023"]
  return collection

def chromeConfigurations():
  options = webdriver.ChromeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging'])
  driver = webdriver.Chrome(options=options)
  return driver

def openSIReport(driver):
  driver.get("https://smartinterviews.in/")
  driver.maximize_window()

  wait = WebDriverWait(driver, 20)

  Login = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/layout-header/nav/div/div[2]/ul/li[6]/a/span/span')))
  Login.click()

  UserName = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="autofocus"]')))
  UserName.send_keys(getUserName())

  Password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
  Password.send_keys(getPassword())

  driver.find_element_by_xpath('/html/body/app-root/auth-page/div/div/mat-card/form/button').click()
  time.sleep(10)

  driver.execute_script("window.open('https://smartinterviews.in/report/GRIET-2023')")
  time.sleep(15)
  driver.switch_to.window(driver.window_handles[-1])

  driver.find_element_by_xpath('/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/mat-toolbar/button[2]/span[1]/mat-icon').click()
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="mat-menu-panel-4"]/div/button[1]').click()
  time.sleep(10)
  return driver

def getStudentDetails(driver, i):
  return

def getHackerRankScores(driver, i):
  return

def getSmartInterviewsScores(driver, i):
  return

def getLeetCodeScores(driver, i):
  return

def getInterviewBitScores(driver, i):
  return

def getCodeChefScores(driver, i):
  return

def getCodeForcesScores(driver, i):
  return

def getSpojScores(driver, i):
  return

def getInternalContestScores(driver, i):
  return

def getTotalScore(driver, i):
  return

def insertToDB(driver, collection):
  for i in range(1, 129):
    DET = getStudentDetails(driver, i)
    HR  = getHackerRankScores(driver, i)
    SI  = getSmartInterviewsScores(driver, i)
    LC  = getLeetCodeScores(driver, i)
    IB  = getInterviewBitScores(driver, i)
    CC  = getCodeChefScores(driver, i)
    CF  = getCodeForcesScores(driver, i)
    SJ  = getSpojScores(driver, i)
    IC  = getInternalContestScores(driver, i)
    TOT = getTotalScore(driver, i)
    break # To test for initial values

collection = connectToDB()
driver = chromeConfigurations()
newDriver = openSIReport(driver)
insertToDB(newDriver)

# TODO: Finalise schema of DataBase
# TODO: Add batch data to MongoDB Database