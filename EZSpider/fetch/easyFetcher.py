# -*- coding: utf-8 -*-

"""
Using built-in python packages of request a url
to implement BaseFetcher.

"""


import urllib2

from base import BaseFetcher


class Urllib2Fetcher(BaseFetcher):
    """
    A urllib2 implemetation fetcher

    """
    def __init__(self, *args, **kwargs):
        pass

    def fetch(self, url):
        """Fetching html string"""
        url = Urllib2Fetcher._validate_scheme(url)
        net_obj = urllib2.urlopen(url)
        html = net_obj.read()
        net_obj.close()
        return html
