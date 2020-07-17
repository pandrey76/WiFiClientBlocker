import os
import pyautogui as pg
from time import sleep
import importlib.util
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from IRouterWebInterfaceController import IRouterWebInterfaceController

base_module_name = "IRouterWebInterfaceController"
base_class_name = "IRouterWebInterfaceController"

path_to_scripts = os.path.dirname(os.path.realpath(__file__))
path_to_scripts = os.path.join(path_to_scripts, base_module_name + '.py')
spec = importlib.util.spec_from_file_location(base_module_name, path_to_scripts)
base_module = importlib.util.module_from_spec(spec)
sys.modules[base_module_name] = base_module
spec.loader.exec_module(base_module)

base_class = getattr(base_module, base_class_name)


class Huawei_R100_1(base_class):

    def __init__(self, url, login, password, data):
        """

        :param url:
        :param login:
        :param password:
        """
        super().__init__(url, login, password, data)


    def prepare(self):
        """
        """
        i = 0
        while i < 7:
            pg.press("tab")
            i += 1
            sleep(1)

        pg.press("enter")
        sleep(5)

        i = 0
        while i < 13:
            pg.press("tab")
            i += 1
            sleep(1)

        pg.press("enter")
        sleep(5)

        i = 0
        while i < 18:
            pg.press("tab")
            i += 1
            sleep(1)

    def activate(self):
        """
        """
        i = 0
        while i < 4:
            pg.press("tab")
            i += 1
            sleep(1)
            
        pg.moveTo(590, 230)
        sleep(5)
        pg.leftClick()
        
    def block_devices(self):
        """

        :return:
        """
        browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

        browser.get(self.url)
        try:
            #assert 'Yahoo' in browser.title
            sleep(5)
            self.login_administrator()
            sleep(5)
            elem = browser.find_element_by_id("Admin_0_5")
            elem.click()
            browser.implicitly_wait(5)
            elem = browser.find_element_by_id("Admin_0_5_1")
            elem.click()
            sleep(3)
            elem = browser.find_element_by_id("MACblackSelected1")
            elem.click()
            sleep(3)
            elem = browser.find_element_by_id("btnApplyId")
            elem.click()
            sleep(3)
        except:
            pass
        browser.quit()

        # # Run browser
        # self.run_default_browser()
        #
        # # Login admin
        # sleep(15)
        # self.login_administrator()
        #
        # # Make blocking actions
        # # sleep(15)
        # # self.prepare()
        # #
        # # sleep(5)
        # # pg.moveTo(607, 270)
        # # pg.leftClick()
        # #
        # # sleep(5)
        # # self.activate()
        # #
        # # #sleep(15)
        # # #current_mposition_x, current_mposition_y = pg.position()
        # # #print("x: ", current_mposition_x)
        # # #print("y: ", current_mposition_y)
        #
        # sleep(10)
        # base_class.close_active_window()

    def recover_devices(self):
        """

        :return:admin
        """

        browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

        browser.get(self.url)
        try:
            #assert 'Yahoo' in browser.title
            sleep(5)
            self.login_administrator()
            sleep(5)
            elem = browser.find_element_by_id("Admin_0_5")
            elem.click()
            browser.implicitly_wait(5)
            elem = browser.find_element_by_id("Admin_0_5_1")
            elem.click()
            sleep(3)
            elem = browser.find_element_by_id("MACDisableSelected1")
            elem.click()
            sleep(3)
            elem = browser.find_element_by_id("btnApplyId")
            elem.click()
            sleep(3)
        except:
            pass
        browser.quit()

        # from selenium import webdriver
        # from selenium.webdriver.common.keys import Keys
        #
        # driver = webdriver.Firefox()
        # driver.get("http://www.python.org")
        # assert "Python" in driver.title
        # elem = driver.find_element_by_name("q")
        # elem.clear()
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        # driver.close()
        # return None


if __name__ == '__main__':
    obj = Huawei_R100_1("http://IP/index.htm", "admin", "")
    obj.blocking()
