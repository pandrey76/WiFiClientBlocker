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

# webbrowser.open('http://net-informations.com', new=0)

# Running default web brouser
# webbrowser.open_new('http://net-informations.com')


#webbrowser.open_new('http://192.168.1.254/index.htm')
#print(webbrowser.get())

# time.sleep(3)
# pg.hotkey("alt", "f4")

#time.sleep(2)
#pg.hotkey("ctrl", "c")
#
#os.system("python3 run-browser.py")


if __name__ == '__main__':
    gws = netifaces.gateways()
    print(gws)
    print("Router IP: ", gws['default'][netifaces.AF_INET][0])

    addrs = netifaces.ifaddresses(gws['default'][netifaces.AF_INET][1])

    print("Current device MAC address: ", addrs[netifaces.AF_LINK][0]['addr'])

    ip_mac = get_mac_address(ip=gws['default'][netifaces.AF_INET][0])
    print("Router Mac address: ", ip_mac)

    url = 'http://192.168.1.254/index.htm'
    open_close_rv6699_panel(url)