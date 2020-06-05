import webbrowser
from time import sleep
import pyautogui as pg


class IRouterWebInterfaceController:
    """
    """

    def __init__(self, url, login, password):
        """

        :param url:
        :param login:
        :param password:
        """
        self._URL = url
        self._Login = login
        self._Password = password
        self.__delay_before_enter_login = 15
        self.__delay_after_enter_login = 15

    url = property(lambda self: self._URL)
    """
    """

    login = property(lambda self: self._Login)
    """
    """

    @property
    def delay_before_enter_login(self):
        """

        :return:
        """
        return self.__delay_before_enter_login

    @property
    def delay_after_enter_login(self):
        """

        :return:
        """
        return self.__delay_after_enter_login

    def block_devices(self):
        """
        """
        raise Exception("No implement")

    def recover_devices(self):
        """

        :return:
        """
        raise Exception("No implement")

    def run_default_browser(self):
        """

        :return:
        """
        webbrowser.open_new(self._URL)

    def login_administrator(self):
        """

        :return:
        """
        pg.typewrite(self._Login, 0.1)
        pg.press("tab")
        pg.typewrite(self._Password, 0.1)
        pg.press("enter")

    @classmethod
    def close_active_window(cls):
        """

        :return:
        """
        pg.hotkey("alt", "f4")

    @classmethod
    def check_support_interface_methods(cls, method_name):
        """

        :param method_name:
        :return:
        """
        support_methods = [
            "block_devices",
            "recover_devices",
            "change_wifi_password"
            ]
        if method_name in support_methods:
            return True
        return False


if __name__ == '__main__':

    obj = IRouterWebInterfaceController("http://IP/index.htm", "admin", "")
    obj.run_default_browser()

    sleep(obj.delay_before_enter_login)
    obj.login_administrator()

    # time.sleep(5)
    # IRouterWebInterfaceController.close_active_window()
    # time.sleep(5)
    # IRouterWebInterfaceController.close_active_window()

    # browser = webbrowser.get()
    # browser.open_new("http://192.168.1.254/index.htm")
    # sleep(3)
    # IRouterWebInterfaceController.close_active_window()