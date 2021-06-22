import random    # Random modülünü kullanacağımız için sisteme import ediyoruz.

print(" ")
print("---RRE ALGORİTMASI---")
print("RRE : Random Reversible Encryption (Rastgele Geri Dönüşümlü Şifreleme)")
print(" ")
# Yukarıdaki kısım programımın giriş ve kendini tanıtma kısmıydı.

isim = input("Lütfen isminizi yazınız: ")   # Burası programımın kullanıcıya hitap etmesi için isim aldığı yer.
print("UYARI!: Şifrelenecek Metni Lütfen Büyük Harflerle Girmeyiniz. Çünkü Kırılması Kolaylaşacaktır.") # Büyük harf uyarısı.

sifrelenecek_metin = input("Merhaba"+" "+ isim + "," +" "+"lütfen şifrelenecek metni gir: ")
# Yukarıdaki satırda ismimizle hitap ederek şifrelenecek metin isteniyor ve böylece "sifrelenecek_metin" değişkenini tanımlıyoruz.

alfabe = ["a","b","c","ç","d","e","f","g","ğ","h","i","ı","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
sifrelenmis_metin = ""
anahtar = []           # Alfabe, Şifrelenmiş Metin, Anahtar dizisi ve Çözülmüş Metni de sisteme tanımlıyoruz.
cozulmus_metin = ""

for i in sifrelenecek_metin:
    sifrelenmis_metin += i
    rastgele_sayı = random.randint(1,5)      # Rastegele olarak 1 ile 5 arasında rakamlar üretmeye yarar.
    anahtar.append(rastgele_sayı)            # Üretilen sayıları append diyerek anahtar dizisinin içerisine yazar.

    for x in range(rastgele_sayı):
        harf = random.choice(alfabe)         # Girdiğimiz metnin arasındaki random harfler burada üretiliyor.
        sifrelenmis_metin += harf

for i in range(len(anahtar)):                # Anahtardaki random sayılarının uzunluğunu alır.
    index = 0                   # Şifrelenmiş metindeki karakterleri çözerken 0.indexten başlanmasını sağlar.

    for x in anahtar:
        if  len(cozulmus_metin) <= len(anahtar)-1 :    # Eğer çözülmüş metnin uzunluğu anahtarın uzunluğundan 1 eksikse
            cozulmus_metin += sifrelenmis_metin[index] # Çözülmüş metin = çözülmüşmetin+şifrelenmiş metin(index)
        else:                                          # Değilse
            break
                                                       # index = index+x+1 şeklinde yap.
        index += x + 1

print("-------------------------------------------------------------------------------------------------------------------")
print("Şifrelemek İstediğin Metin: ",sifrelenecek_metin)
print("Girdiğin Metnin Şifrelenmiş Hali: ",sifrelenmis_metin)  # Bu alan elde etmek istediğimiz verileri ekrana yazdırma kısmı.
print("Şifrelenmiş Metni Çözmek İçin Anahtar:",anahtar)
print("Şifrelenmiş Metnin Anahtar İle Çözülmüş Hâli: ",cozulmus_metin)
print("-------------------------------------------------------------------------------------------------------------------")
print(isim + ","+" "+"şifrelenmiş olan metninizi çözüp kullanabilmek için lütfen verilen şifrelenmiş metni ve anahtarı saklayınız.")
print("Şifrelenmiş Metin: ",sifrelenmis_metin)
print("Anahtar: ",anahtar)  # Bu alan ise ismimizle hitap ederek bize şifrelenmiş metnin ve anahtarın saklanmasının uyarısını yapıyor.
print("-------------------------------------------------------------------------------------------------------------------")
print("Şifreleme İşlemi Başarıyla Tamamlandı") # Bu alan son alanımız. Kullanıcıya işlemin tamamlandığının bilgisini veriyor
print("Görüşmek Üzere"+" "+isim+"...")      # Ve ismimizle hitap ederek kullanıcıya vedasını ediyor.