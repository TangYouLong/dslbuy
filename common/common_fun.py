from base_view.base_view import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv

class Commom(BaseView):

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x,y

    def getTime(self):
        self.now = time.strftime("$Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self,csv_file,line):
        logging.info('=====get_csv_data======')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row

if __name__=='__main__':
    driver = appium_desired()
    com = Commom(driver)
