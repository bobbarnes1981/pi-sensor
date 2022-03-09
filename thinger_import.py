import sqlite3
import csv

db_file = 'sqlite.db'
csv_file = 'data.csv'

con = sqlite3.connect(db_file)
cur = con.cursor()

with open(csv_file) as f:
    reader = csv.reader(f, delimiter=';')
    next(reader) # discard header
    for row in reader:
        if len(row) != 3:
            continue
        data = [
            row[0],
            row[1],
            row[2]
        ]
        cur.execute('INSERT INTO readings (timestamp, office, outside) VALUES (?, ?, ?)', data)
        con.commit()
        print(f"{data[0]}, {data[1]}, {data[2]}")

con.close()

