# -*- coding: utf-8 -*-
import pytest
from redbrick import ClientBrick
from .utils import xstr


class TestCore:

    def test_dump(self, httpbin):
        client = ClientBrick()
        client.send('GET', httpbin.url + '/xml')
        dumps = client.dump('test', 'xml')
        with open(dumps[0]) as fd:
            assert fd.read() == xstr(client.last_sent)
        with open(dumps[1]) as fd:
            assert fd.read() == xstr(client.last_receive)
