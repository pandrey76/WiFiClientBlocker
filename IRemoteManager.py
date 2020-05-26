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
        if response.title == "router":
            return True
        else:
            return False

    def process(self):
        """

        :return:
        """
        response = self.__IServer.get_response()
        if self.is_my(response):
            imp = self.__RouterInspector.getting_current_router_implementation()
            if str(response.body).lower().find("block"):
                imp.turn_off()
            elif str(response.body).lower().find("recover"):
                imp.turn_on()


if __name__ == "__main__":
    remote_manager = IRemoteManager()
    remote_manager.process()
