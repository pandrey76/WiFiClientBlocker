import json


def looking_router_info():
    with open("Routers.json", "r") as read_file:
        data = json.load(read_file)
        # data = json.loads(read_file.read())
        print(data)
        print(type(data))
        for to in data:
            print(type(to), to)

        print(type(data["routers"][0]), data["routers"][0])
        print(type(data["routers"][0]["admin"]), data["routers"][0]["admin"])
        print(type(data["routers"][1]), data["routers"][1])
        print(type(data["routers"][1]["class"]), data["routers"][1]["class"])
        print(data["routers"][1]["macAddressWire"])


if __name__ == '__main__':
    looking_router_info()
