import os
from selenium import webdriver
import logging
# os.environ['PATH'] += "<Driver Folder path>"
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

driver = webdriver.Chrome(r"C:\Users\manis\driver\chromedriver.exe")

logger.info("Opening the provided website")
try:
    driver.get('https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html')
    logger.info("Successfuly opened")
except Exception as e:
    logger.error("Could not open the provided website")
    logger.error(f"Ther error is {e}")

'''implicitly_wait a better method than time.sleep as it would move on if the page loads before specified time'''
driver.implicitly_wait(5)

download = driver.find_element_by_id('downloadButton')
download.click()
