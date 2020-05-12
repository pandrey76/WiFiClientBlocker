import netifaces
import os
from getmac import get_mac_address
import webbrowser
import time
import pyautogui as pg


def run_default_browser(url):
    webbrowser.open_new(url)


def open_close_rv6699_panel(url):
    run_default_browser(url)
    time.sleep(2)
    pg.hotkey("ctrl", "c")
    os.system("python3 run-browser.py")


class NetworkInformer:
    """

    """
    def __init__(self):
        """

        """
        self._GWS = netifaces.gateways()

    def getting_connected_router_ip(self):
        """

        :return:
        """
        return self._GWS['default'][netifaces.AF_INET][0]

    def getting_mac_address_of_current_device(self):
        """

        :return:
        """
        addrs = netifaces.ifaddresses(self._GWS['default'][netifaces.AF_INET][1])
        return addrs[netifaces.AF_LINK][0]['addr']

    @classmethod
    def get_connected_router_ip(cls):
        """

        :return:
        """
        gws = netifaces.gateways()
        return gws['default'][netifaces.AF_INET][0]

    @classmethod
    def get_mac_address_by_ip(cls, ip):
        """

        :param ip:
        :return:
        """
        return get_mac_address(ip=ip)

    @classmethod
    def get_mac_address_of_current_device(cls):
        """

        :param ip:
        :return:
        """

        gws = netifaces.gateways()
        addrs = netifaces.ifaddresses(gws['default'][netifaces.AF_INET][1])
        return addrs[netifaces.AF_LINK][0]['addr']


if __name__ == '__main__':
    gws = netifaces.gateways()
    print(gws)
    gws1 = gws['default'][netifaces.AF_INET][0]
    print("Router IP: ", gws1)

    ip_mac = get_mac_address(ip=gws['default'][netifaces.AF_INET][0])
    print("Router Mac address: ", ip_mac)

    addrs = netifaces.ifaddresses(gws['default'][netifaces.AF_INET][1])
    print("Current device MAC address: ", addrs[netifaces.AF_LINK][0]['addr'])

    print("By class methods!")
    router_ip = NetworkInformer.get_connected_router_ip()
    print("Router IP: ", router_ip)
    print("Router MAC: ", NetworkInformer.get_mac_address_by_ip(router_ip))
    print("Current device MAC address: ", NetworkInformer.get_mac_address_of_current_device())

    print("By object methods!")
    net_informer = NetworkInformer()
    router_ip = net_informer.getting_connected_router_ip()
    print("Router IP: ", router_ip)
    print("Router MAC: ", NetworkInformer.get_mac_address_by_ip(router_ip))
    print("Current device MAC address: ", net_informer.getting_mac_address_of_current_device())


    # url = 'http://192.168.1.254/index.htm'
    # open_close_rv6699_panel(url)
