from common.myunit import StartEnd
from business_view.login_view import LoginView
import unittest
import logging


class TestLogin(StartEnd):

    def test_login_administration(self):
        logging.info("===test_login_administration===")
        l = LoginView(self.driver)
        l.login_action('15700741068','1')
        l.check_update()
        l.check_advert()
        l.check_battery_authorization()
        l.check_enviroment('15700741068','1')

    def test_login_store(self):
        logging.info("===test_login_administration===")
        l = LoginView(self.driver)
        l.login_action('13432457764', '1')
        l.check_update()
        l.check_advert()
        l.check_battery_authorization()

if __name__ == '__main__':
    unittest.main()