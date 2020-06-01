import os
import pyautogui as pg
from time import sleep
import importlib.util
import sys
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


class iPhone6SE(base_class):

    def __init__(self, url, login, password):
        """

        :param url:
        :param login:
        :param password:
        """
        super().__init__(url, login, password)

    def blocking(self):
        """

        :return:
        """
        # Run browser
        self.run_default_browser()

        # Login admin
        sleep(2)
        self.login_administrator()

        # Make blocking actions
        sleep(2)
        i = 0
        while i < 15:
            pg.press("tab")
            i += 1

        pg.press("enter")
        sleep(2)
        pg.press("enter")
        sleep(2)
        base_class.close_active_window()

    def unblocking(self):
        """

        :return:admin
        """
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys

        driver = webdriver.Firefox()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()
        return None


if __name__ == '__main__':
    obj = iPhone6SE("http://IP/index.htm", "admin", "")
    #obj.blocking()
    obj.unblocking()
