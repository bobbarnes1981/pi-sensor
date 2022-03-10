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
    for rec in recs:
        data.append((datetime.fromtimestamp(rec[0], timezone.utc).strftime('%Y-%m-%d %H:%M:%S'), rec[1], rec[2]))
    con.close()
    #return f"<p>Timestamp: {d} ({t}) Office: {office} Outside: {outside}</p>"
    return render_template('index.html', recs=data)
