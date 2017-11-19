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


def dump_to_file(path_to_file, text, encoding=None):
    """Dumps text to file.

    :param path_to_file: str, combination of a directory path and a filename to dump
    :param text: str, text to dump, unicode is supported
    :param encoding: str, encoding of dump file, default value is 'utf-8'
    """
    if encoding is None:
        encoding = 'utf-8'
    if text is None:
        text = ''
    if isinstance(text, str):
        text = text.decode(encoding)
    with open(path_to_file, mode='w', encoding=encoding) as f:
        f.write(text)
