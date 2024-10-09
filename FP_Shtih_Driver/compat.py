# -*- coding: utf-8 -*-


import sys
import locale
import functools


LOCALE = locale.getpreferredencoding()

unicode = str
xrange = range
reduce = functools.reduce


# Взято из six
def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a
    # dummy metaclass for one level of class instantiation that replaces
    # itself with the actual metaclass.
    class metaclass(type):
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)

    return type.__new__(metaclass, 'temporary_class', (), {})


def str_compat(cls):

    return cls


def bool_compat(cls):

    return cls
