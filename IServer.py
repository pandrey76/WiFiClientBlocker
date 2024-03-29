import os
import json
import imaplib
import email
import re

from Response import Response


class IServer:
    """

    """
    def __init__(self):
        """

        """
        path_to_script_dir = os.path.dirname(os.path.realpath(__file__))
        path_to_json_file = os.path.join(path_to_script_dir, "RemoteSources.json")

        with open(path_to_json_file, "r") as read_file:
            servers_meta_json = json.load(read_file)
            self.__TrustedServers = []
            for current_sever in servers_meta_json["trusted_source"]:
                self.__TrustedServers.append(current_sever)

            self.__SourcePath = servers_meta_json["remote_sources"][0]["source_path"]
            self.__Password = servers_meta_json["remote_sources"][0]["password"]
            self.__Name = servers_meta_json["remote_sources"][0]["name"]

    def request(self):
        """

        :return:
        """
        pass

    def get_response(self):
        """

        :return:
        """
        host = "imap.gmail.com"
        port = 993
        user = self.__SourcePath
        password = self.__Password
        # sender = self.__Name

        connection = imaplib.IMAP4_SSL(host=host, port=port)
        connection.login(user=user, password=password)

        status, msgs = connection.select('INBOX')
        assert status == 'OK'

        typ, data = connection.search(None, '(UNSEEN)') # , 'FROM', '"%s"' % sender)
        try:
            for num in data[0].split():
                typ, message_data = connection.fetch(num, '(RFC822)')
                mail = email.message_from_bytes(message_data[0][1])
                for part in mail.walk():
                    # sender = None
                    # for attr in self.__TrustedServers:
                    #     if attr == part["From"]:
                    #         sender = part["From"]
                    #         break
                    # if sender is None:
                    #     raise Exception("Response from not trusted server" )
                    # body_obj = part.get_payload(decode=True)
                    email_body = re.findall(r"<div>(.*)<\/div>", str(part.get_payload(decode=True)))
                    # print(type(email_body))
                    response = Response(author="", title=part["Subject"], body=email_body[0], ext_data="")
                    return response

        finally:
            try:
                connection.close()
            except:
                pass
            connection.logout()
        return None


if __name__ == '__main__':
    server = IServer()
    response = server.get_response()
    # import re
    # response = re.findall(r"<div>(.*)<\/div>", '<div>good</div>')
    # response = HTMLParser.feed(data='<div>good</div>')
    # from lxml.html import fromstring
    print("Author: ", response.author, "Title: ", response.title, "Body: ", response.body, "Ext.Data: ", response.ext_data)