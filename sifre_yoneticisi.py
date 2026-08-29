import sqlite3 as sql

conn = sql.connect('sifre_yoneticisi.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sifreler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_adi TEXT NOT NULL,
    kullanici_adi TEXT NOT NULL,
    sifre TEXT NOT NULL
)''')
conn.commit()
conn.close()