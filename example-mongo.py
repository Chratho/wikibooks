#!/usr/bin/python3.4
import pymongo

conn = None
try:
    conn = pymongo.MongoClient()
except:
    print("Error: Unable to connect to database.")
    sys.exit(-1);
col = conn.wikibooks.book

searchterm = "haskell"


# db.book.find({ $text: { $search: "haskell" }},{ score: {$meta: "textScore"}, text:0, _id:0, url:0, book_id:0}).sort({'score':{'$meta': 'textScore'}}).limit(10)

res = col.find(filter={ "$text": { "$search": searchterm} },
               projection={ "score": {"$meta": "textScore"}, "text":0, "_id":0, "url":0, "book_id":0 },
               limit = 10)
print(list(res))

