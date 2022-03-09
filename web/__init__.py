from datetime import datetime, timezone
from flask import Flask, render_template
import sqlite3
import time

db_file = 'sqlite.db'
app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute('SELECT timestamp, office, outside FROM readings WHERE timestamp > ? ORDER BY timestamp ASC', (time.time() - 60*60*24, ))
    recs = cur.fetchall()
    data = []
    skip = 10
    count = 0
    for rec in recs:
        if count == 0:
            data.append((datetime.fromtimestamp(rec[0], timezone.utc), rec[1], rec[2]))
        count = count + 1
        if count > skip:
            count = 0
    con.close()
    #return f"<p>Timestamp: {d} ({t}) Office: {office} Outside: {outside}</p>"
    return render_template('index.html', recs=data)
