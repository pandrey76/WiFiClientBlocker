import os
import pyautogui as pg
from time import sleep
import importlib.util
# from IRouterWebInterfaceController import IRouterWebInterfaceController

path_to_scripts = os.path.dirname(os.path.realpath(__file__))
path_to_scripts = os.path.join(path_to_scripts, 'IRouterWebInterfaceController.py')
spec1 = importlib.util.spec_from_file_location("IRouterWebInterfaceController.IRouterWebInterfaceController", path_to_scripts)
i_router_web_interface_controller = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(i_router_web_interface_controller)


class Sercomm_RV6699(i_router_web_interface_controller.IRouterWebInterfaceController):

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
        i_router_web_interface_controller.IRouterWebInterfaceController.close_active_window()
        sleep(5)
        i_router_web_interface_controller.IRouterWebInterfaceController.close_active_window()

    def unblocking(self):
        """

        :return:admin
        """
        return None


if __name__ == '__main__':
    obj = Sercomm_RV6699("http://IP/index.htm", "admin", "")
    obj.blocking()
