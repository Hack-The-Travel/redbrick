# -*- coding: utf-8 -*-
import pytest
import json
from datetime import datetime, timedelta
from redbrick import ClientBrick
from .utils import xstr

DATETIME_FORMAT = '%Y%m%dT%H%M%S.%f'


class TestCore:
    def test_dump(self, httpbin):
        client = ClientBrick()
        for req in ['/xml', '/encoding/utf8']:
            client.request('GET', httpbin.url + req)
            dumps = client.dump('test', 'xml')
            with open(dumps[0]) as fd:
                assert fd.read() == xstr(client.last_sent)
            with open(dumps[1]) as fd:
                assert fd.read() == xstr(client.last_received)

    def test_dump_timezone(self, httpbin):
        """Checks timezone applying for dumping."""
        dt_utc = datetime.utcnow()
        client_paris = ClientBrick(timezone='Europe/Paris', datetime_format=DATETIME_FORMAT)  # UTC+1
        url = httpbin.url + '/get'
        client_paris.request('GET', url)
        dumps_paris = client_paris.dump('timezone', 'json')
        fmt = '/'.join([client_paris.dumps_dir, DATETIME_FORMAT])
        cut = len('_timezone_RQ.json')
        dt_paris = datetime.strptime(dumps_paris[0][:-cut], fmt)
        delta = dt_paris - dt_utc
        assert int(round(delta.total_seconds()/60/60)) == 1

    def test_dump_datetime(self, httpbin):
        """Checks that RQ and RS dumps have the same timestamp."""
        client = ClientBrick(datetime_format=DATETIME_FORMAT)
        url = httpbin.url + '/get'
        client.request('GET', url)
        dumps = client.dump('datetime', 'json')
        fmt = '/'.join([client.dumps_dir, DATETIME_FORMAT])
        cut = len('_datetime_RQ.json')
        assert datetime.strptime(dumps[0][:-cut], fmt) == datetime.strptime(dumps[1][:-cut], fmt)

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
