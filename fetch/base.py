# -*- coding: utf-8 -*-


import urlparse


HTTP_SCHEME = ['http', 'https']

class BaseFetcher(object):
    """
    The base fetcher is defined here.
    All subclass must implemet the functions here.

    """
    def fetch(self, url, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def _validate_scheme(cls, url):
        """
        Validate the given url contains scheme,
        if not, add a default value: http:// to the head of the url

        """
        result = urlparse.urlparse(url)
        if result.scheme not in HTTP_SCHEME:
            url = 'http://' + url
        return url
