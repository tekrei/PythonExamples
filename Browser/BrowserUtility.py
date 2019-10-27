# coding=UTF-8
'''
Browser utility classes and functions
Sites and categories are stored in sites sqlite3 database

First version: 12 Aug 2009
Upgrade to GTK3: 27 Mar 2016
Fixes for Python v3: 27 Oct 2019
'''

import sys
import sqlite3


class Site:
    def __init__(self, name="", url=""):
        self.name = name
        self.url = url


class Utility:

    def __init__(self, running_path=""):
        self.connection = sqlite3.connect(running_path+"/sites")

    def removeSite(self, url):
        cur = self.connection.cursor()
        sorgu = "DELETE FROM sites WHERE url='"+url+"'"
        try:
            cur.execute(sorgu)
        except e:
            print("An error occurred:%s" % e)

    def addSite(self, name, url, category):
        cur = self.connection.cursor()
        query = "INSERT INTO sites VALUES ('"+str(name) + \
            "','"+str(url)+"',"+str(category)+")"
        rowid = -1
        try:
            cur.execute(query)
            self.connection.commit()
            rowid = cur.lastrowid
        except sqlite3.IntegrityError:
            print("%s added before!" % url)
        cur.close()
        return rowid

    def getSites(self, category):
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM sites WHERE category="+str(category))
        result = cur.fetchall()
        siteler = []
        for record in result:
            siteler.append(Site(record[0], record[1]))
        return siteler

    def getCategory(self):
        cur = self.connection.cursor()
        cur.execute("SELECT category FROM category")
        return cur.fetchall()
