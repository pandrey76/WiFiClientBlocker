import os
import pyautogui as pg
from time import sleep
import importlib.util
import sys
from selenium import webdriver

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

    def block_devices1(self):
        """

        :return:
        """
        browser = webdriver.Chrome('/usr/lib/chrome/chromedriver')

        browser.get(self.url)
        try:
            sleep(5)
            self.login_administrator()
            sleep(5)
            elem = browser.find_element_by_id("Menu1Txt1")
            elem.click()
            browser.implicitly_wait(3)
            elem = browser.find_element_by_id("Menu1Txt1")
            elem.click()
            sleep(3)
            elem = browser.find_element_by_id("Menu2Txt3")
            elem.click()
            sleep(3)

            all_wifi_types = browser.find_elements_by_name("w_band")
            for wifi_type in all_wifi_types:
                if wifi_type.get_attribute("value") == '2':
                    wifi_type.click()
                    browser.implicitly_wait(3)
                    deny_types = browser.find_elements_by_name("mac_mode_radio")
                    for deny_type in deny_types:
                        value = deny_type.get_attribute("value")
                        if value == "deny":
                            deny_type.click()
                            browser.implicitly_wait(3)
                    break

            all_wifi_types = browser.find_elements_by_name("w_band")
            for wifi_type in all_wifi_types:
                if wifi_type.get_attribute("value") == '5':
                    wifi_type.click()
                    browser.implicitly_wait(3)
                    deny_types = browser.find_elements_by_name("mac_mode_radio")
                    for deny_type in deny_types:
                        value = deny_type.get_attribute("value")
                        if value == "deny":
                            deny_type.click()
                            browser.implicitly_wait(3)
                    break
            # Save
            save_elem = browser.find_element_by_name("save")
            if save_elem:
                save_elem.click()
                browser.implicitly_wait(3)

            # Apply
            elements = browser.find_elements_by_tag_name('a')
            for elem in elements:
                if elem.get_attribute("languagecode") == "Apply":
                    elem.click()
                    break

            # <a href="javascript:applyAP()" languagecode="Apply">Применить</a>
            sleep(10)
        except Exception as ex:
            print(ex)
        browser.quit()

        # # Run browser
        # self.run_default_browser()
        #
        # # Login admin
        # sleep(self.delay_before_enter_login)
        # self.login_administrator()
        #
        # # Make blocking actions
        # sleep(self.delay_after_enter_login)
        # i = 0
        # while i < 15:
        #     pg.press("tab")
        #     i += 1
        #
        # pg.press("enter")
        # sleep(2)
        # pg.press("enter")
        # sleep(5)
        # base_class.close_active_window()
        # sleep(5)
        # base_class.close_active_window()

    def __init__(self, url, login, password, data):
        """

        :param url:
        :param login:
        :param password:
        """
        super().__init__(url, login, password, data)

    def save(self, browser: webdriver):
        """

        """
        save_elem = browser.find_element_by_name("save")
        if save_elem:
            save_elem.click()

    def click_a_element_by_languagecode_name(self, browser: webdriver, name: str):
        """

        """
        elements = browser.find_elements_by_tag_name('a')
        for elem in elements:
            if elem.get_attribute("languagecode") == name:
                elem.click()
                break

    def apply(self, browser: webdriver):
        """

        """
        self.click_a_element_by_languagecode_name(browser, "Apply")

    def reboot(self, browser: webdriver):
        """

        """
        self.click_a_element_by_languagecode_name(browser, "Reboot")

    def exit(self, browser: webdriver):
        """

        """
        self.click_a_element_by_languagecode_name(browser, "Logout")

    def go_to_mac_filtration(self, browser: webdriver):
        """

        """
        elem = browser.find_element_by_id("Menu1Txt1")
        elem.click()
        elem = browser.find_element_by_id("Menu1Txt1")
        elem.click()
        elem = browser.find_element_by_id("Menu2Txt3")
        elem.click()

    def activate_mac_filtration(self, browser: webdriver, action: str):
        """

        """
        if action == "deny" or action == "allow" or action == "disable":
            all_wifi_types = browser.find_elements_by_name("w_band")
            for wifi_type in all_wifi_types:
                if wifi_type.get_attribute("value") == '2':
                    wifi_type.click()
                    browser.implicitly_wait(3)
                    deny_types = browser.find_elements_by_name("mac_mode_radio")
                    for deny_type in deny_types:
                        value = deny_type.get_attribute("value")
                        if value == action:
                            deny_type.click()

                    break
            self.save(browser)
            browser.implicitly_wait(3)

            all_wifi_types = browser.find_elements_by_name("w_band")
            for wifi_type in all_wifi_types:
                if wifi_type.get_attribute("value") == '5':
                    wifi_type.click()
                    browser.implicitly_wait(3)
                    deny_types = browser.find_elements_by_name("mac_mode_radio")
                    for deny_type in deny_types:
                        value = deny_type.get_attribute("value")
                        if value == action:
                            deny_type.click()

                    break
            self.save(browser)
            browser.implicitly_wait(3)

        else:
            raise TypeError("The entering params must be allow, deny or disable")

    def block_devices(self):
        """

        """
        browser = webdriver.Chrome('/usr/lib/chrome/chromedriver')

        browser.get(self.url)
        try:
            sleep(5)
            self.login_administrator()
            sleep(5)

            self.go_to_mac_filtration(browser)
            browser.implicitly_wait(3)
            self.activate_mac_filtration(browser, "deny")
            browser.implicitly_wait(3)
            self.apply(browser)
            browser.implicitly_wait(60)

            # After sleep must be function calling to correct work.
            self.exit(browser)
        except Exception as ex:
            print(ex)
        browser.quit()

    def recover_devices(self):
        """

        :return:admin
        """
        browser = webdriver.Chrome('/usr/lib/chrome/chromedriver')

        browser.get(self.url)
        try:
            sleep(5)
            self.login_administrator()
            sleep(5)

            self.go_to_mac_filtration(browser)
            browser.implicitly_wait(3)
            self.activate_mac_filtration(browser, "disable")
            browser.implicitly_wait(3)
            self.apply(browser)
            browser.implicitly_wait(60)

            # After sleep must be function calling to correct work.
            self.exit(browser)

        except Exception as ex:
            print(ex)
        browser.quit()


if __name__ == '__main__':
    obj = Sercomm_RV6699("http://IP/index.htm", "admin", "")
    obj.blocking()

# id="Menu1Txt1" Configure/настройки

# id="Menu1Txt1" Wireless/Беспроводная сеть

# <a id="Menu2Txt3" href="javascript:GoAndRemember('wireless_mac.htm','')" languagecode="MAC Filter">Фильтрация по MAC</a>

# <input type="radio" name="w_band" value="2" onclick="change_band();"> <b>2.4G</b>
# <input type="radio" name="w_band" value="5" onclick="change_band();"> <b>5G</b>

# <input type="radio" name="mac_mode_radio" value="allow"> Разрешить
# <input type="radio" name="mac_mode_radio" value="deny"> Запретить
# <input type="radio" name="mac_mode_radio" value="disable"> Отключить

# <input type="text" name="macfilterAdd" size="17" maxlength="17" value="" onkeydown="if(event.keyCode==13)return false">
# <input type="button" name="hostAdd1" value="<< Добавить" style="{width:100px;}" class="submitBtn" onclick="return checkmac();">

# <input type="button" name="relname" style="{width:100px;}" class="submitBtn" value="Удалить" onclick="macrelease(1);">

# <tr>
#     <td align="center">iPad-mini-2</td>
#     <td align="center">ac:3c:0b:55:eb:c6</td>
#     <td align="center">
#         <input type="button" name="relname" style="{width:100px;}" class="submitBtn" value="Удалить" onclick="macrelease(1);">
#     </td>
# </tr>

# <tr>
#     <td align="center">iPad-mini</td>
#     <td align="center">6c:70:9f:6c:80:b5</td>
#     <td align="center">
#         <input type="button" name="relname" style="{width:100px;}" class="submitBtn" value="Удалить" onclick="macrelease(2);">
#     </td>
# </tr>


# <tr>
# 	<td colspan="2">
# 		<table border="1" cellpadding="2" cellspacing="2" width="100%">
# 		<tbody><tr>
# 			<td align="center"><span class="thead" languagecode="wireless_mac_code_7">Имя хоста</span></td>
# 			<td align="center"><span class="thead" languagecode="wireless_mac_code_8">MAC Адрес</span></td>
# 			<td align="center"><span class="thead"></span></td>
# 		</tr>
#
# 		<tr>
# 			<td align="center"></td>
# 			<td align="center"><input type="text" name="macfilterAdd" size="17" maxlength="17" value="" onkeydown="if(event.keyCode==13)return false"></td>
# 			<td align="center"><script language="javascript" type="text/javascript">strHtml='<input type="button" name="hostAdd1" value="&lt;&lt; '+getErrorMsgByVar("wls_msg_36")+'" style="{width:100px;}" class="submitBtn" onClick="return checkmac();">';
# 		dw(strHtml);</script><input type="button" name="hostAdd1" value="<< Добавить" style="{width:100px;}" class="submitBtn" onclick="return checkmac();"></td>
# 		</tr>
#
# 		<script language="javascript" type="text/javascript">
# 		var strHtml;
# 		var strTemp;
# 		var list = "ac:3c:0b:55:eb:c6 6c:70:9f:6c:80:b5";
# 		//var list = "01:01:01:01:01:01 01:01:01:01:01:02 01:01:01:01:01:03";
# 		var token = new Array(maxMacNum + 2);
#         	var begin = 0;
#         	var next = -2;
#
# 		count = 0;
# 		while(next != -1 && list != "")
# 		{
# 		    if(next != -2)
# 		        begin = next + 1;
# 		    next = list.indexOf(' ', begin + 1);
# 		    if(next == -1)
# 		        token[count] = list.substring(begin);
# 		    else
# 		        token[count] = list.substring(begin, next);
#
# 		    count++;
# 		}
#
# 		count = 1;
# 		while(token[count - 1])
# 		{
#             		strTemp = token[count - 1];
#
# 			strHtml='<tr><td  align="center"></td><td  align="center">'+String(count)
# 				+'.</td>';
#
# 			document.writeln('<td  align="center">');
#
# 			showhostname(strTemp);
#
# 			strHtml='</td><td  align="center">'
# 				+strTemp
# 				+'</td><td  align="center">';
#
# 			strHtml =strHtml +'<input type="button" name="relname" style="{width:100px;}" class="submitBtn" value="'+getErrorMsgByVar("wls_msg_37")+'" onClick="macrelease('
# 			+String(count)
# 			+');">';
#
# 			strHtml = strHtml +'</td></tr>';
#
# 			document.writeln(strHtml);
# 			count++;
# 		} //while
# 		</script><tr><td align="center">
# iPad-mini-2
# </td><td align="center">ac:3c:0b:55:eb:c6</td><td align="center"><input type="button" name="relname" style="{width:100px;}" class="submitBtn" value="Удалить" onclick="macrelease(1);"></td></tr>
# <tr><td align="center">
# iPad-mini
# </td><td align="center">6c:70:9f:6c:80:b5</td><td align="center"><input type="button" name="relname" style="{width:100px;}" class="submitBtn" value="Удалить" onclick="macrelease(2);"></td></tr>
#
#
# 		</tbody></table>
# </td>
# </tr>

# <td align="right"><span languagecode="nav_logged_in">Вы вошли в систему как:</span>&nbsp;
#     <a href="javascript:GoToLink('mgt_end_user.htm','name=Manage User&amp;user=3')">admin</a>
#     |
#     <a href="javascript:applyAP()" languagecode="Apply">Применить</a>
#     |
#     <a href="javascript:xhelp()" languagecode="Help">Помощь</a>
#     |
#     <a href="javascript:restartAP()" languagecode="Reboot">Перезагрузка</a>
#     | <a href="javascript:log_out()" languagecode="Logout">Выход</a>
#     &nbsp; &nbsp; &nbsp;
# </td>

# <input type="button" name="save" value="Сохранить" class="stdbutton" onclick="submitF()" languagecode="Save">
# <a href="javascript:applyAP()" languagecode="Apply">Применить</a>
# <a href="javascript:restartAP()" languagecode="Reboot">Перезагрузка</a>
# <a href="javascript:log_out()" languagecode="Logout">Выход</a>