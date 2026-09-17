import sqlite3 as sql
from cryptography.fernet import Fernet
import hashlib
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

def master_sifre_kontrol():
    if os.path.exists("master.hash"):
        with open("master.hash", "r") as f:
            master_sifre = f.read().strip()

        deneme = 0
        while deneme < 3:
            girilen_sifre = input("Master şifrenizi girin: ")
            hash_nesnesi = hashlib.sha256(girilen_sifre.encode())
            hex_hash = hash_nesnesi.hexdigest()
            if hex_hash != master_sifre:
                print("Hatalı master şifre. Lütfen tekrar deneyin.")
                deneme += 1
            else:
                print("Master şifre doğrulandı.")
                ana_menü()
                return
        print("3 hatalı giriş yaptınız. Programdan çıkılıyor.")
    else:
        master_sifre = input("Yeni bir master şifre oluşturun: ")
        hash_nesnesi = hashlib.sha256(master_sifre.encode())
        hex_hash = hash_nesnesi.hexdigest()
        with open("master.hash", "w") as f:
            f.write(hex_hash)
        print("Master şifre başarıyla oluşturuldu.")
        ana_menü()

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

def sifre_ekle(site_adi, kullanici_adi, sifre):
    conn = sql.connect('sifre_yoneticisi.db')
    cursor = conn.cursor()
    sifre_encrypted = fernet.encrypt(sifre.encode())
    cursor.execute("INSERT INTO sifreler (site_adi, kullanici_adi, sifre) VALUES (?, ?, ?)", (site_adi, kullanici_adi, sifre_encrypted))
    conn.commit()
    conn.close()

def sifre_listele():
    conn = sql.connect('sifre_yoneticisi.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id,site_adi, kullanici_adi, sifre FROM sifreler")
    sifreler = cursor.fetchall()
    if sifreler:
        print("\nKayıtlı Şifreler:")
        for id, site_adi, kullanici_adi, sifre_encrypted in sifreler:
            sifre_decrypted = fernet.decrypt(sifre_encrypted).decode()
            print(f"İd: {id}, Site: {site_adi}, Kullanıcı Adı: {kullanici_adi}, Şifre: {sifre_decrypted}")
    else:
        print("\nKayıtlı şifre bulunamadı.")
    conn.close()

def sifre_sil(id):
    conn = sql.connect('sifre_yoneticisi.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM sifreler WHERE id = ?', (id,))
    if cursor.rowcount == 0:
        print("Belirtilen ID ile eşleşen bir şifre bulunamadı.")
    else:
        print("Şifre başarıyla silindi.")
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
            site_adi = input("Site Adı: ")
            kullanici_adi = input("Kullanıcı Adı: ")
            sifre = input("Şifre: ")
            sifre_ekle(site_adi, kullanici_adi, sifre)
            print("Şifre başarıyla eklendi.")
        elif secim == '2':
            sifre_listele()
        elif secim == '3':
            sifre_listele()
            id = input("Silmek istediğiniz şifrenin ID'si: ")
            sifre_sil(id)
        elif secim == '4':
            print("Çıkış yapılıyor...")
            sys.exit()

master_sifre_kontrol()