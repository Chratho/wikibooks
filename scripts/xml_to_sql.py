#!/usr/bin/python3.4
import xml.etree.ElementTree as etree

import psycopg2
import os

DB_NAME = "wikibooks"
DB_USER = "ct"

XML_DATA_SRC = os.path.join("xml","enwikibooks.xml")

STEP_SIZE = 50

conn = None
try:
    conn = psycopg2.connect("dbname='{name}' user='{user}'".format(name=DB_NAME,user=DB_USER))
except:
    print("Error: Unable to connect to database.")
    sys.exit(-1);

tree = etree.parse(XML_DATA_SRC,parser=etree.XMLParser(encoding="UTF-8")).getroot()

i = 0
with conn.cursor() as cur:
    for node in tree:
        if node.tag != "doc": continue

        id = node.attrib['id']
        url = node.attrib['url']
        title = node.attrib['title']

        cur.execute("""INSERT INTO book(book_id,url,title,text) VALUES (%s,%s,%s,%s)""", (id,url,title,node.text))

        i += 1
        if (i % STEP_SIZE == 0):
            print("Inserting {amt} books.".format(amt=STEP_SIZE))
            conn.commit()

conn.commit()
