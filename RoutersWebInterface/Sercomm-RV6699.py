import pyautogui as pg
import time

from IRouterWebInterfaceController import IRouterWebInterfaceController


class Sercomm_RV6699(IRouterWebInterfaceController):

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
        time.sleep(self.delay_before_enter_login)
        self.login_administrator()

        # Make blocking actions
        time.sleep(self.delay_after_enter_login)
        i = 0
        while i < 15:
            pg.press("tab")
            i += 1

        pg.press("enter")
        time.sleep(2)
        pg.press("enter")
        time.sleep(5)
        IRouterWebInterfaceController.close_active_window()

    def unblocking(self):
        """

        :return:
        """
        return None


if __name__ == '__main__':
    obj = Sercomm_RV6699("http://192.168.1.254/index.htm", "admin", "xWCNyyiizc76")
    obj.blocking()
