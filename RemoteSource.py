
class RemoteSource:
    """

    """

    def __init__(self, source_path="", password="", name="", description=""):
        """

        :param source_path:
        :param password:
        :param name:
        """
        self.__SourcePath = source_path
        self.__Password = password
        self.__Name = name
        self.__Description = description

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
        self.__SourcePath = param

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
        self.__Password = param

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
        self.__Name = param

    @property
    def description(self):
        """

        :return:
        """
        return self.__Name

    @description.setter
    def description(self, param):
        """

        :param param:
        :return:
        """
        self.__Description = param
