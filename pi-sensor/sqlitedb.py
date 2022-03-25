
import logging
import sqlite3
import json
import os.path
import time

class SqliteDb(object):
    def __init__(self, db_file):
        self.db_file = db_file
        if not os.path.exists(self.db_file):
            con = sqlite3.connect(self.db_file)
            cur = con.cursor()
            cur.execute('CREATE TABLE readings (timestamp INTEGER UNIQUE NOT NULL, office REAL, outside REAL, garage REAL)')
            con.commit()
            con.close()
    def store(self, payload):
        try:
            for name in ['office', 'outside', 'garage']:
                logging.info("Stored: {0} {1}".format(name, payload[name]))
            con = sqlite3.connect(self.db_file)
            cur = con.cursor()
            cur.execute('INSERT INTO readings (timestamp, office, outside, garage) VALUES (?, ?, ?, ?)', (time.time(), payload['office'], payload['outside'], payload['garage']))
            con.commit()
            con.close()
        except Exception as e:
            logging.error(e)

