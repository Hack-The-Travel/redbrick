# -*- coding: utf-8 -*-
import pytest
import sys
if sys.version_info[0] < 3:
    from io import open
from redbrick.utils import dump


class TestUtils:
    @pytest.mark.parametrize('text', [
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
        u'Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне.'
    ])
    def test_dump(self, text):
        path_to_dump = '/tmp/dump.txt'
        dump(path_to_dump, text)
        with open(path_to_dump, 'r') as fd:
            assert fd.read() == text
