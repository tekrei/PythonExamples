#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
import urllib3

running_path = os.path.dirname(os.path.realpath(__file__))

# read file
request = urllib3.PoolManager().request(
    "GET", "https://www.w3schools.com/xml/cd_catalog.xml")
contents = request.data.decode('utf-8')
# to open a local file use open('example.xml, 'r').read()
# parse contents
root = ET.fromstring(contents)
print('root %s %s' % (root.tag, root.attrib))
print('-----------------------------------------')
# find all doc elements in the documents
for atype in root:
    print('child %s %s --> %s' % (atype.tag, atype.attrib, atype.text))
    # traverse all children of
    for child in atype:
        print('\tchild %s %s --> %s' % (child.tag, child.attrib, child.text))
    print('-----------------------------------------')
