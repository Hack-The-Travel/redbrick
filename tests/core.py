# -*- coding: utf-8 -*-
import pytest
from redbrick import ClientBrick


class TestCore:

    def test_dump(self, httpbin):
        client = ClientBrick()
        client.send('GET', httpbin.url + '/xml')
        dumps = client.dump('test', 'xml')
        with open(dumps[0]) as fd:
            assert fd.read() == (client.last_sent if client.last_sent is not None else '')
        with open(dumps[1]) as fd:
            assert fd.read() == (client.last_receive if client.last_receive is not None else '')
