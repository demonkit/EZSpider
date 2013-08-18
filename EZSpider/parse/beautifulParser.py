# -*- coding: utf-8 -*-


from BeautifulSoup import BeautifulSoup


class BeautifulParser(object):
    """
    An HTML parser, which parses the given static html string
    to a banch of urls.

    """

    def parse(self, html, *args, **kwargs):
        """
        Input a readable html object, parse the object, returns 
        an iterable object contained urls.

        """
        soup = BeautifulSoup(html)
        wrapped_links = soup.findAll('a')
        links = []
        for item in wrapped_links:
            if 'href' in item.attrs[0]:
                links.append(item.get("href"))
        return links
