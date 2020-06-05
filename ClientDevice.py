

class ClientDevice:
    """

    """

    def __init__(self, name, mac, long_name, priority, ip):
        """

        :param name:
        :param mac:
        :param long_name:
        :param priority:
        :param ip:
        :return:
        """
        self.__Name = name
        self.__Mac = mac
        self.__LongName = long_name
        self.__Priority = priority
        self.__IP = ip

    name = property(lambda self: self.__Name)
    """
    """

    mac = property(lambda self: self.__Mac)
    """
    """

    long_name = property(lambda self: self.__LongName)
    """
    """

    priority = property(lambda self: self.__Priority)
    """
        Priority of connected devices, can be equal  0 to 3.
        0 - Higher priority (Device of administrator).
        
    """

    ip = property(lambda self: self.__IP)
    """
    """

    @classmethod
    def get_json(cls, client_device):
        """

        :param client_device:
        :return:
        """
        return None

    @classmethod
    def set_json(cls, json):
        """

        :param json:
        :return:
        """
        return ClientDevice("", "", "", "")
