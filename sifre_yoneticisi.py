import sqlite3 as sql

conn = sql.connect('sifre_yoneticisi.db')

cursor = conn.cursor()

conn.commit()
conn.close()