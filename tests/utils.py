# -*- coding: utf-8 -*-
import pytest
import sys
if sys.version_info[0] < 3:
    from io import open
from redbrick.utils import dump


class TestUtils:
    @pytest.mark.parametrize(
        'text, encoding', (
            ('Lorem Ipsum is simply dummy text of the printing and typesetting industry.', None),
            (u'Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне.', None),
            (u'Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне.', 'cp1251'),
        ))
    def test_dump(self, text, encoding):
        path_to_dump = '/tmp/dump.txt'
        dump(path_to_dump, text, encoding=encoding)
        with open(path_to_dump, 'r', encoding=encoding) as fd:
            assert fd.read() == text
