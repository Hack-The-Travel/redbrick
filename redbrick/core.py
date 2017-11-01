# -*- coding: utf-8 -*-
import requests


class ClientBrick(object):

    def __init__(self):

        #: Content of the request, in unicode
        self.last_sent

        #: Content of the response, in unicode
        self.last_receive

        #: SSL Verification default
        self.verify = True

    def send(self, method, url):
        """Sends request.

        :param method: str, HTTP method to use.
        :param url: str, URL to send.
        """
        r = requests.request(method, url, verify=self.verify)
        print r.text
