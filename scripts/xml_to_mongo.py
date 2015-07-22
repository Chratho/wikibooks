#!/usr/bin/python3.4
import xml.etree.ElementTree as etree

import os
from pymongo import MongoClient

XML_DATA_SRC = os.path.join("xml","enwikibooks.xml")

STEP_SIZE = 50

conn = None
try:
    conn = MongoClient()
except:
    print("Error: Unable to connect to database.")
    sys.exit(-1);
col = conn.wikibooks.book

tree = etree.parse(XML_DATA_SRC,parser=etree.XMLParser(encoding="UTF-8")).getroot()

i = 0
dicts = []
for node in tree:
    if node.tag != "doc": continue

    book_id = node.attrib['id']
    url = node.attrib['url']
    title = node.attrib['title']

    dicts.append({ "book_id": book_id, "url": url, "title": title, "text": node.text })

    i += 1
    if (i % STEP_SIZE == 0):
        col.insert_many(dicts)
        dicts = []
