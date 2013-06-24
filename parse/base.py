# -*- coding: utf-8 -*-


"""
Base HTML parser class definition.
"""


class BaseParser(object):
    """
    An HTML parser, which defines each parser's basic functions.

    """

    def parse(self, html, *args, **kwargs):
        """Subclass must implement this method"""
        raise NotImplementedError
