from datetime import datetime, timezone
from flask import Flask
import sqlite3

db_file = 'sqlite.db'
app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute('SELECT timestamp, office, outside FROM readings ORDER BY timestamp DESC limit 1')
    rec = cur.fetchone()
    t = rec[0]
    d = datetime.fromtimestamp(t, timezone.utc)
    office = rec[1]
    outside = rec[2]
    con.close()
    return f"<p>Timestamp: {d} ({t}) Office: {office} Outside: {outside}</p>"
