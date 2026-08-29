import sqlite3 as sql
from cryptography.fernet import Fernet
import os

if  os.path.exists("anahtar.key"):
    with open("anahtar.key", "rb") as key_file:
        key = key_file.read()
else:
    key = Fernet.generate_key()
    with open("anahtar.key", "wb") as key_file:
        key_file.write(key)

fernet = Fernet(key)

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