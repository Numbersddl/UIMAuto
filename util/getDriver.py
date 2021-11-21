import selenium
from time import sleep
from selenium import webdriver

def get_alert_msg():
    msg = DriverUtil.get_driver().find_element_by_id('id').text()
    return msg

class DriverUtil(object):

    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver == None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.get('http://www.baidu.com')
            cls.__driver.maximize_window()
            sleep(3)
        return cls.__driver;

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            sleep(3)
        cls.__driver.quit()
        cls.__driver = None

if __name__ == '__main__':
    # my___driver = __DriverUtil()
    # my___driver.get___driver()
    # sleep(2)
    # my___driver.quit___driver()
    DriverUtil.get_driver()
    sleep(2)
    DriverUtil.quit_driver()