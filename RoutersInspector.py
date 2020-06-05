import os
import json
import ipaddress
from NetworkPerformance import NetworkInformer
import importlib.util


def looking_router_info():
    with open("Routers.json", "r") as read_file:
        data = json.load(read_file)
        # data = json.loads(read_file.read())
        print(data)
        print(type(data))
        for to in data:
            print(type(to), to)

        print(type(data["routers"][0]), data["routers"][0])
        print(type(data["routers"][0]["loginInfo"]), data["routers"][0]["loginInfo"])
        print(type(data["routers"][1]), data["routers"][1])
        print(type(data["routers"][1]["realisation"]), data["routers"][1]["realisation"])
        print(data["routers"][1]["macAddressWire"])


class RoutersInspector:
    """

    """

    def __init__(self, response_body):
        """

        """
        self.__CurrentRouterImplementation_object = None
        self.__ResponseBody = response_body
        self.__Action = None
        self.__Data = None
        self.parse()

    response_body = property(lambda self: self.__ResponseBody)
    """
    """

    def geting_current_router_implementation(self):
        """
        """
        # print("Entering turn_off")
        router_ip = NetworkInformer.get_connected_router_ip()
        # print(router_ip)
        ip_interface = ipaddress.ip_interface(router_ip)
        if ip_interface.version != 4:
            raise Exception("Wrong router ip address version")
        router_mac = NetworkInformer.get_mac_address_by_ip(router_ip).lower()
        # print(router_mac)

        path_to_script_dir = os.path.dirname(os.path.realpath(__file__))
        path_to_json_file = os.path.join(path_to_script_dir, "Routers.json")

        with open(path_to_json_file, "r") as read_file:
            routers_meta_json = json.load(read_file)
            current_router = None
            for router_meta in routers_meta_json["routers"]:
                if (router_meta["macAddressLan"].lower() == router_mac) or \
                        (router_meta["macAddressWire"].lower() == router_mac):
                    current_router = router_meta
                    break
            if current_router is None:
                raise Exception("Current router is not registered in Routers.json (MacAddress of router is " + router_mac + ").")

        url = current_router["loginInfo"]["url"].replace("IP", router_ip)
        # print(url)
        login = current_router["loginInfo"]["login"]
        # print(login)
        password = current_router["loginInfo"]["password"]
        # print(password)

        path_to_run_script = os.path.join(path_to_script_dir, "WebBrowser")

        module_file = current_router["realisation"]["file"]
        path_to_run_script = os.path.join(path_to_run_script, module_file)

        module_name = module_file.replace(".py", "")
        class_name = current_router["realisation"]["class"]

        spec = importlib.util.spec_from_file_location(module_name, path_to_run_script)
        current_router_implementation_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(current_router_implementation_module)
        # print(current_router_implementation_module)

        realisation_class = getattr(current_router_implementation_module, class_name)
        self.__CurrentRouterImplementation_object = realisation_class(url, login, password)
        # print(current_router_implementation_object)

    # def turn_on(self):
    #     """
    #
    #     :return:
    #     """
    #     self.__CurrentRouterImplementation_object = None
    #     self.geting_current_router_implementation()
    #     self.__CurrentRouterImplementation_object.unblocking()
    #
    # def turn_off(self):
    #     """
    #
    #     :return:
    #     """
    #     self.__CurrentRouterImplementation_object = None
    #     self.geting_current_router_implementation()
    #     self.__CurrentRouterImplementation_object.blocking()

    def parse(self):
        """

        :return:
        """
        return None

    def process(self):
        """

        :return:
        """
        if self.__Action == "block_devices":
            self.__CurrentRouterImplementation_object.block_devices()
        elif self.__Action == "recover_devices":
            self.__CurrentRouterImplementation_object.recover_devices()
        elif self.__Action == "change_wifi_password":
            self.__CurrentRouterImplementation_object.change_wifi_password()
        else:
            raise Exception("Wrong support method")


if __name__ == '__main__':
    # looking_router_info()
    # print("RoutersInspector start!!")
    # import webbrowser
    # webbrowser.open_new("http://localhost")
    try:
        router_inspector = RoutersInspector()
        router_inspector.turn_off()
        #router_inspector.recover_devices()
        
    except Exception as er:
        print(er)
        print(er.args)
