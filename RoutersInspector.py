import json

if __name__ == '__main__':
    with open("Routers.json", "r") as read_file:
        data = json.load(read_file)
        # data = json.loads(read_file.read())
        print(data)
        print(type(data))
        for to in data:
            print(type(to), to)

        print(type(data["routers"][0]), data["routers"][0])
        print(type(data["routers"][0]["admin"]), data["routers"][0]["admin"])
