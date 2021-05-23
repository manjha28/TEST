from  selenium import webdriver
import BestDealBot.constants as const
import os
#TODO: Need to understand this super class
#FIXME: Need to look at the path variable problrm of seleniuum
class Booking():
    def __init__(self,teardown=False):
        self.teardown = teardown
        # self.driver_path = driver_path
        # os.environ['PATH'] += self.driver_path
        self.driver = webdriver.Chrome(r"C:\Users\manis\driver\chromedriver.exe")

        # super(Booking,self).__init__()

    # def __exit__(self, exc_type, exc_val, exc_tb):#working of context manager
    #     if self.teardown:
    #         self.driver.quit()

    def first_page(self):
        # driver = self.driver
        self.driver.get(const.BASE_URL)
