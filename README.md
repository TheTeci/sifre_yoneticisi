# Şifre Yöneticisi

## 1. Proje Ne Yapıyor?
- Bu proje basit bir şifre yöneticisi projesidir.
- ilk olarak sizden programa giriş yapmak için bir master şifre ister. Şifre 3 kez yanlış girilirse uygulama kapanır.
- Uygulamaya doğru master şifre ile giriş yaparsanız önünüze menü seçenekleri gelir.
- Menüde şifre ekleme, şifre silme, şifreleri listeleme ve uygulamadan çıkış yapma seçenekleri vardır. 
- Eklediğiniz şifreyi başkaları göremesin diye cryptography ile şifreler. Başkaları şifrenize erişir ise rastgele karakterler görür.
- Şifreleri silmek için ekranda çıkan, silmek istediğiniz id'ye denk gelen sayıyı yazıp silebilirsiniz.
- istediğinizde mevcut şifrelerinizi listeleyerek görebilirsiniz.

## 2. Nasıl Kurulur?
- Python 3.11.0 sürümü kullanılmıştır.

- Aşağıdaki requirements.txt dosyasını çalıştırın
```
pip install -r requirements.txt
```

## 3. Kullanılan Kütüphaneler

- sqlite3 (Python ile hazır gelir, kurman gerekmez)
- cryptography (Fernet)
- hashlib (Python ile hazır gelir, kurman gerekmez)
- os (Python ile hazır gelir, kurman gerekmez)
- sys (Python ile hazır gelir, kurman gerekmez)

## 4. Nasıl Kullanılır?

- Programı çalıştır
- İlk çalıştırmada master şifre oluşturmanız istenir
- Sonraki çalıştırmalarınızda sadece master şifreyi girmeniz istenir
- Ekrana çıkan numaraları seçerek şifre ekle , sil veya listele
- Şifre eklemek için site adı, kullanıcı adı ve şifrenizi girmeniz gerekli.
- Şifreleri silmek için ekranda çıkan, silmek istediğiniz id'ye denk gelen sayıyı yazıp silebilirsiniz.
- Şifreleri listele seçeneği ile mevcut şifrelerinizi görebilirsiniz.
- Çıkış yap


