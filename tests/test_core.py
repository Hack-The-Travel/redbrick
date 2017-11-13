# -*- coding: utf-8 -*-
import pytest
import json
from redbrick import ClientBrick
from .utils import xstr


class TestCore:

    def test_dump(self, httpbin):
        client = ClientBrick()
        client.request('GET', httpbin.url + '/xml')
        dumps = client.dump('test', 'xml')
        with open(dumps[0]) as fd:
            assert fd.read() == xstr(client.last_sent)
        with open(dumps[1]) as fd:
            assert fd.read() == xstr(client.last_receive)

    def test_request_basic_auth(self, httpbin):
        auth = ('user', 'password')
        url = httpbin.url + '/basic-auth/user/password'
        client = ClientBrick()
        with pytest.raises(IOError):
            client.request('GET', url)
        client.request('GET', url, auth=auth)
        response = json.loads(client.last_receive)
        assert response['authenticated']
