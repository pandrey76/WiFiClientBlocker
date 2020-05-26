
class Response:
    """

    """

    def __init__(self, author="", title="", body="", ext_data="" ):
        """

        """
        self.__Author = author
        self.__Title = title
        self.__Body = body
        self.__ExtData = ext_data

    @property
    def author(self):
        """

        :return:
        """
        return self.__Author

    @author.setter
    def author(self, param):
        """

        :param param:
        :return:
        """
        self.__Author = author

    @property
    def title(self):
        """

        :return:
        """
        return self.__Title

    @title.setter
    def title(self, param):
        """

        :param param:
        :return:
        """
        self.__Title = title

    @property
    def body(self):
        """

        :return:
        """
        return self.__Body

    @body.setter
    def body(self, param):
        """

        :param param:
        :return:
        """
        self.__Body = body

    @property
    def ext_data(self):
        """

        :return:
        """
        return self.__ExtData

    @ext_data.setter
    def ext_data(self, param):
        """

        :param param:
        :return:
        """
        self.__ExtData = ext_data

