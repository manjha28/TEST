'''
Author : Manish Jha
Date : 20210524
'''


import os
from selenium import webdriver

'''These are the imports required for implementing Explicit wait'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

'''This aproach won't work here, need to go with explicit wait'''
# progress = driver.find_element_by_class_name('progress-label')
# driver.implicitly_wait(30)
# print(f"{progress.text}")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        'Complete!'
    )
)
logger.info(f"The text is matched")