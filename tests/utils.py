# -*- coding: utf-8 -*-
def xstr(s):
    """Converts None to empty string.

    :param s: None, str or unicode, input string.
    :return: empty string instead of None or a given string.
    :rtype: basestring
    """
    if s is None:
        return ''
    if not isinstance(s, basestring):
        raise TypeError('Input parameter should be None, str or unicode')
    return s
