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
import logging

log = logging.getLogger(__name__)


def dump_to_file(path_to_file, text, encoding='utf-8'):
    f = None
    try:
        f = open(path_to_file, 'w', encoding=encoding)
        f.write(unicode(text))
    except:
        log.error('Dump failed - {}'.format(path_to_file), exc_info=True)
    finally:
        if f is not None:
            f.close()
