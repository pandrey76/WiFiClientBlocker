from IServer import IServer
from RoutersInspector import RoutersInspector


class IRemoteManager:
    """

    """

    def __init__(self):
        """

        """
        self.__IServer = IServer()
        self.__RouterInspector = RoutersInspector()

    def is_my(self, response):
        """

        :param response:
        :return:
        """
        if response is not None:
            if response.title.lower() == "router":
                return True
            else:
                return False
        else:
            return False

    def process(self):
        """

        :return:
        """
        response = self.__IServer.get_response()
        if self.is_my(response):
            # body_str = str(response.body)
            # body_str = body_str.lower()
            router_inspector = RoutersInspector(response.body)
            router_inspector.process()


if __name__ == "__main__":
    remote_manager = IRemoteManager()
    remote_manager.process()
