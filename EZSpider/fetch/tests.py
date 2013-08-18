# -*- coding: utf-8 -*-


from easyFetcher import Urllib2Fetcher


fetcher = Urllib2Fetcher()
print len(fetcher.fetch("http://www.google.com"))


print len(fetcher.fetch("www.google.com"))
