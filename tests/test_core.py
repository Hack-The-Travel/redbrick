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
            assert fd.read() == xstr(client.last_received)

    def test_request_basic_auth(self, httpbin):
        auth = ('user', 'password')
        url = httpbin.url + '/basic-auth/user/password'
        client_without_auth = ClientBrick()
        with pytest.raises(IOError):
            client_without_auth.request('GET', url)
        client_with_auth = ClientBrick(auth=auth)
        client_with_auth.request('GET', url)
        response = json.loads(client_with_auth.last_received)
        assert response['authenticated']
