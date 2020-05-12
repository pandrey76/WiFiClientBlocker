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

    def __init__(self):
        """

        """
        self.i = None

    def turn_off(self):
        """

        :return:
        """
        router_ip = NetworkInformer.get_connected_router_ip()
        ip_interface = ipaddress.ip_interface(router_ip)
        if ip_interface.version != 4:
            raise Exception("Wrong router ip address version")
        router_mac = NetworkInformer.get_mac_address_by_ip(router_ip).lower()

        with open("Routers.json", "r") as read_file:
            routers_meta_json = json.load(read_file)
            current_router = None
            for router_meta in routers_meta_json["routers"]:
                if (router_meta["macAddressLan"].lower() == router_mac) or \
                        (router_meta["macAddressWire"].lower() == router_mac):
                    current_router = router_meta
                    break
            if current_router is None:
                raise Exception("Current router is not registered in Routers.json.")

        url = current_router["loginInfo"]["url"].replace("IP", router_ip)
        print(url)
        login = current_router["loginInfo"]["login"]
        print(login)
        password = current_router["loginInfo"]["password"]
        print(password)

        path_to_run_script = os.path.dirname(os.path.realpath(__file__))
        path_to_run_script = os.path.join(path_to_run_script, "WebBrowser")

        realisation_file = current_router["realisation"]["file"]
        path_to_run_script = os.path.join(path_to_run_script, realisation_file)

        module = realisation_file.replace(".py", "")
        realisation_class = current_router["realisation"]["class"]

        spec = importlib.util.spec_from_file_location(module + '.' + realisation_class, path_to_run_script)
        current_router_implementation_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(current_router_implementation_module)
        print(current_router_implementation_module)
        current_router_implementation_object = current_router_implementation_module.Sercomm_RV6699(url, login, password)
        print(current_router_implementation_object)
        current_router_implementation_object.blocking()


if __name__ == '__main__':
    # looking_router_info()
    router_inspector = RoutersInspector()
    router_inspector.turn_off()