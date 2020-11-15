import logging
from common.common_fun import Commom,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
import time
import unittest

class LoginView(Commom):
    '''
    封装登录及后续检测的一系列操作
    '''
    username_element = (By.ID,'com.dsl.newwiki:id/edit_phone_number')
    password_element = (By.ID,'com.dsl.newwiki:id/edit_code')
    login_element = (By.ID,'com.dsl.newwiki:id/login')
    advert_close_element = (By.ID,'com.dsl.newwiki:id/iv_close')
    update_cancel_element = (By.ID,'com.dsl.newwiki:id/btn_update_cancel')
    battery_authorization_element = (By.ID,'android:id/button1')
    tv_name_element = (By.ID,'com.dsl.newwiki:id/tv_name')
    my_element = (By.ID,'com.dsl.newwiki:id/ll_my')
    change_release_element = (By.ID, 'com.dsl.newwiki:id/tv_change_release_url')
    change_test_element = (By.ID, 'com.dsl.newwiki:id/ll_change_test_url')
    switch_test_confirm_element = (By.ID,'com.dsl.newwiki:id/btn_positive')
    USERNAME_VALUE = '13432457764'
    PASSWORD_VALUE = '1'


    def login_action(self,username,password):
        '''
        登录操作
        :param username: 用户名
        :param password: 验证码/密码
        :return:
        '''
        logging.info("======logging_action======")
        logging.info('username is :%s'%username)
        self.driver.find_element(*self.username_element).send_keys(username)

        logging.info('password is:%s'%password)
        self.driver.find_element(*self.password_element).send_keys(password)

        logging.info("click login")
        self.driver.find_element(*self.login_element).click()
        time.sleep(3)
        logging.info("login finished")

    def check_update(self):
        '''
        检查更新弹窗，如果有非强制更新，则点击暂不更新
        :return:
        '''
        logging.info("===check_update===")
        try:
            element = self.driver.find_element(*self.update_cancel_element)
        except NoSuchElementException:
            logging.info("===no_update===")
            pass
        else:
            logging.info("===click update later===")
            element.click()
            time.sleep(5)

    def check_advert(self):
        '''
        检查弹窗广告，如果有则关闭
        :return:
        '''
        logging.info("===check_advert===")
        try:
            element = self.driver.find_element(*self.advert_close_element)
        except NoSuchElementException:
            logging.info("===no_advert===")
            pass
        else:
            logging.info("===advert_close===")
            element.click()

    def check_battery_authorization(self):
        '''
        检查电池授权
        :param self:
        :return:
        '''
        try:
            element = self.driver.find_element(*self.battery_authorization_element)
        except NoSuchElementException:
            logging.info("===no_battery_authorization===")
            pass
        else:
            logging.info("===battery_authorization===")
            element.click()


    def check_enviroment(self,username,password):
        self.driver.find_element(*self.my_element).click()
        try:
            element = self.driver.find_element(*self.change_test_element)
        except NoSuchElementException:
            pass
        else:
            self.switch_test(username,password)

    def switch_test(self,username,password):
        element = self.driver.find_element(*self.change_test_element)
        for i in range(1, 9):
            element.click()
        self.driver.find_element(*self.switch_test_confirm_element).click()
        self.login_action(username,password)
        self.check_update()
        self.check_advert()

    def check_login_status(self,username):
        logging.info("====check_loginStatus======")
        try:
            value = self.driver.find_element(*self.tv_name_element).text
        except NoSuchElementException:
            logging.error("login_fail")
            self.getScreenShot('login_fail')
            return False
        else:










if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('13432457764','1')
    l.check_update()
    l.check_advert()
    l.check_enviroment()


