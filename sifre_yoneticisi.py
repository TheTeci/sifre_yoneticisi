import sqlite3 as sql
from cryptography.fernet import Fernet
import os
import sys

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

def ana_menü():
    while True:
        print("\nŞifre Yöneticisi")
        print("1. Şifre Ekle")
        print("2. Şifreleri Listele")
        print("3. Şifre Sil")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın (1-4): ")

        if secim == '1':
            print("yakında eklenecek")
        elif secim == '2':
            print("yakında eklenecek")
        elif secim == '3':
            print("yakında eklenecek")
        elif secim == '4':
            print("Çıkış yapılıyor...")
            sys.exit()

ana_menü()