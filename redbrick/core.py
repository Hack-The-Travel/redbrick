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

    def dump(self, service, message_format, encoding='utf-8'):
        """Dumps text of last request and response.

        :param service: str, name of called service, part of dumped files name.
        :param message_format: str, format of request/response text, extension of dumped files.
        :param encoding: (optional) str, encoding of dump file.
        """
        dumps = list()
        for text, action in [(self.last_sent, 'RQ'), (self.last_receive, 'RS')]:
            now = datetime.now().strftime('%Y-%m-%dT%H%M%S.%f')
            path_to_file = os.path.join(
                self.log_dir,
                '{dt}_{srv}_{act}.{fmt}'.format(dt=now, srv=service, act=action, fmt=message_format)
            )
            try:
                dump_to_file(path_to_file, text, encoding=encoding)
                dumps.append(path_to_file)
            except IOError as e:
                log.error('Dump error: {}'.format(e), exc_info=True)
        return dumps

    def send(self, method, url,
            headers=None, data=None, service_name=None):
        """Sends request.

        :param method: str, HTTP method to use.
        :param url: str, URL to send.
        """
        service_name = '' if service_name is None else service_name

        r = requests.request(method, url, data=data, headers=headers, verify=self.verify)
        self.last_sent = data
        self.last_receive = r.text
        # TODO: provided format, now used constant 'xml'
        self.dump(service_name, 'xml')
        r.raise_for_status()
