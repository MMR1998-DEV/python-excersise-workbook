#insert from text file to database2 file

import sqlite3
import pandas

data = pandas.read_csv("ten_more_countries.txt")

conn = sqlite3.connect("database2.db")
cur = conn.cursor()
for index, row in data.iterrows():
    print(row["Country"], row["Area"])
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row["Country"], row["Area"]))

conn.commit()
conn.close()