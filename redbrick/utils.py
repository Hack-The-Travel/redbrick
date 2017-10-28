# -*- coding: utf-8 -*-

"""
redbrick.utils
~~~~~~~~~~~~~~~~

This module provides utility functions that are used within redbrick
that are also useful for external consumption.
"""

import sys
if sys.version_info[0] < 3:
    from io import open


def dump_to_file(path_to_file, text, encoding='utf-8'):
    with open(path_to_file, mode='w', encoding=encoding) as f:
        f.write(unicode(text))
