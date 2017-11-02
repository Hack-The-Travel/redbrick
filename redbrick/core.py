# -*- coding: utf-8 -*-
import os
from datetime import datetime
import logging
import requests
from .utils import dump_to_file

log = logging.getLogger(__name__)


class ClientBrick(object):

    def __init__(self):

        #: Content of the request, in unicode
        self.last_sent = None

        #: Content of the response, in unicode
        self.last_receive = None

        #: SSL Verification default
        self.verify = True

        #: Path to log files
        self.log_dir = '/tmp'

    def dump(self, service, fmt, encoding='utf-8'):
        """Dumps content of last request and response.

        :param encoding: (optional) str, encoding of dump file.
        """
        for text, action in [(self.last_sent, 'RQ'), (self.last_receive, 'RS')]:
            now = datetime.now().strftime('%Y-%m-%dT%H%M%S.%f')
            path_to_file = os.path.join(
                self.log_dir,
                '{dt}_{srv}_{act}.{fmt}'.format(dt=now, srv=service, act=action, fmt=fmt)
            )
            try:
                dump_to_file(path_to_file, text, encoding=encoding)
            except Exception as e:
                log.error('Dump error - {}'.format(path_to_file), exc_info=True)

    def send(self, method, url):
        """Sends request.

        :param method: str, HTTP method to use.
        :param url: str, URL to send.
        """
        r = requests.request(method, url, verify=self.verify)
        print r.text
