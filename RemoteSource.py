

class RemoteSource:
    """

    """

    def __init__(self, source_path="", password="", name=""):
        """

        :param source_path:
        :param password:
        :param name:
        """
        self.__SourcePath = source_path
        self.__Password = password
        self.__Name = name

    @property
    def source_path(self):
        """

        :return:
        """
        return self.__SourcePath

    @source_path.setter
    def source_path(self, param):
        """

        :param param:
        :return:
        """
        self.__SourcePath = source_path

    @property
    def password(self):
        """

        :return:
        """
        return self.__Password

    @password.setter
    def password(self, param):
        """

        :param param:
        :return:
        """
        self.__Password = password

    @property
    def name(self):
        """

        :return:
        """
        return self.__Name

    @name.setter
    def name(self, param):
        """

        :param param:
        :return:
        """
        self.__Name = name