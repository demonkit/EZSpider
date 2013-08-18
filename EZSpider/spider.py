#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Main entrance for EZSpider.
"""

__version__ = (0, 0, 1)


from Queue import Queue
from optparse import OptionParser
from parse.beautifulParser import BeautifulParser
from fetch.easyFetcher import Urllib2Fetcher


parser = OptionParser()
parser.add_option("-u", "--url", dest="url", default="www.baidu.com",
        help="The url which EZSpider starts with.")
parser.add_option("-d", "--depth", dest="depth", default=10,
        help="The maximum depth definition EZSpider goes into.")

queue = Queue()

def crawl(url, depth):
    global queue
    fetcher = Urllib2Fetcher()
    parser = BeautifulParser()
    html = fetcher.fetch(url)
    links = parser.parse(html)
    [queue.put(link) for link in links]


if __name__ == '__main__':
    print 'Starting EZSpider ...'
    (options, args) = parser.parse_args()
    crawl(options.url, 10)
