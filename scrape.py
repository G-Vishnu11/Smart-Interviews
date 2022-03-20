import time
import os
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

from update import updateRecordInDB

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

def getStudentDetails(driver, ind):
  ROLL = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[2]/span").text
  NAME = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[3]/div/span[1]").text
  try:
    USERNAME = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[5]/a").text
  except:
    USERNAME = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[5]/span").text
  return [ROLL, NAME, USERNAME]

def getStudentRank(driver, ind):
  RANK = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[1]").text
  TEMP = RANK.split(" ")
  LRANK = TEMP[0]
  GRANK = TEMP[1][1:-1]
  return [LRANK, GRANK]

def getStudentBranch(driver, ind):
  try:
    BRANCH = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[4]/span").text
    return [BRANCH]
  except:
    return [""]

def getHackerRankScores(driver, ind):
  DS = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[6]/span").text
  ALGO = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[7]/span").text
  TOT = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind +  "]/td[8]/span").text
  return [DS, ALGO, TOT]

def getSmartInterviewsScores(driver, ind):
  BASIC = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[9]/span").text
  PRIMARY = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[10]/span").text
  return [BASIC, PRIMARY]

def getLeetCodeScores(driver, ind):
  LCPS = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[11]/span").text
  LCNC = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[12]/span").text
  LCR = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[13]/span").text
  TOT = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[14]/span").text
  return [LCPS, LCNC, LCR, TOT]

def getInterviewBitScores(driver, ind):
  IBS = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[15]/span").text
  TOT = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[16]/span").text
  return [IBS, TOT]

def getCodeChefScores(driver, ind):
  CCPS = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[17]/span").text
  CCNC = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[18]/span").text
  CCR = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[19]/span").text
  TOT = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[20]/span").text
  return [CCPS, CCNC, CCR, TOT]

def getCodeForcesScores(driver, ind):
  CFPS = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[21]/span").text
  CFNC = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[22]/span").text
  CFR = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[23]/span").text
  TOT = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[24]/span").text
  return [CFPS, CFNC, CFR, TOT]

def getSpojScores(driver, ind):
  SPS = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[25]/span").text
  SP = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[26]/span").text
  TOT = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[27]/span").text
  return [SPS, SP, TOT]

def getInternalContestScores(driver, ind):
  IC1 = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[29]").text
  IC2 = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[30]").text
  try:
    int(IC1)
  except:
    IC1 = '0'
  try:
    int(IC2)
  except:
    IC2 = '0'
  return [IC1, IC2]

def getTotalScore(driver, ind):
  TOTAL = driver.find_element_by_xpath("/html/body/app-root/app-report/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[" + ind + "]/td[28]/span").text
  return [TOTAL]


def getDetails(driver, i):
  DET = getStudentDetails(driver, str(i))
  RANK = getStudentRank(driver, str(i))
  BRANCH = getStudentBranch(driver, str(i))
  HR  = getHackerRankScores(driver, str(i))
  SI  = getSmartInterviewsScores(driver, str(i))
  LC  = getLeetCodeScores(driver, str(i))
  IB  = getInterviewBitScores(driver, str(i))
  CC  = getCodeChefScores(driver, str(i))
  CF  = getCodeForcesScores(driver, str(i))
  SJ  = getSpojScores(driver, str(i))
  IC  = getInternalContestScores(driver, str(i))
  TOT = getTotalScore(driver, str(i))
  return [DET, RANK, BRANCH, HR, SI, LC, IB, CC, CF, SJ, IC, TOT]


collection = connectToDB()
driver = chromeConfigurations()
newDriver = openSIReport(driver)

for i in range(1, 129):
  details = getDetails(newDriver, i)
  updateRecordInDB(collection, details)