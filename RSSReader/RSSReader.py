# coding=UTF-8
'''
RSS Reader utility classes

First version: 12 Aug 2009
Upgrade to GTK3: 27 Mar 2016
'''

import feedparser


class RSSItem:
    """This is an RSS item, it contain all the RSS info like Title and Description"""

    def __init__(self, channel="", title="", description="", link=""):
        self.channel = channel
        self.title = title
        self.description = description
        self.link = link


class RSSReader:
    def __init__(self, url):
        self.url = url

    def createRSSItem(self, channel, item):
        """Create an RSS item and return it"""
        title = item.get('title', "(none)")
        description = item.get('description', "(none)")
        link = item.get('link', "(none)")
        return RSSItem(channel, title, description, link)

    def getItems(self):
        feed = feedparser.parse(self.url)

        channel = feed.channel.title

        itemsToReturn = []

        for item in feed.entries:
            rss_item = self.createRSSItem(channel, item)
            itemsToReturn.append(rss_item)

        return itemsToReturn
