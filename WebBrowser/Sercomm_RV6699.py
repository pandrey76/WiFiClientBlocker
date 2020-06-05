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


class Sercomm_RV6699(base_class):

    def __init__(self, url, login, password, data):
        """

        :param url:
        :param login:
        :param password:
        """
        super().__init__(url, login, password, data)

    def block_devices(self):
        """

        :return:
        """
        # Run browser
        self.run_default_browser()

        # Login admin
        sleep(self.delay_before_enter_login)
        self.login_administrator()

        # Make blocking actions
        sleep(self.delay_after_enter_login)
        i = 0
        while i < 15:
            pg.press("tab")
            i += 1

        pg.press("enter")
        sleep(2)
        pg.press("enter")
        sleep(5)
        base_class.close_active_window()
        sleep(5)
        base_class.close_active_window()

    def recover_devices(self):
        """

        :return:admin
        """
        return None

    def check_data(self):
        """

        :return:
        """
        raise Exception("No implement")


if __name__ == '__main__':
    obj = Sercomm_RV6699("http://IP/index.htm", "admin", "")
    obj.blocking()
