def metin_sifreleme():
    print("Lütfen sadece harf kullanınız.")
    metin = input("Şifrelenecek metni giriniz: ").upper()

    anahtar = 13
    sifrelenmis_metin = ""

    for i in range(len(metin)):
        temp = ord(metin[i]) + anahtar
        if ord(metin[i]) == 32:
            sifrelenmis_metin += " "
        elif temp > 90:
            temp -= 26
            sifrelenmis_metin += chr(temp)
        else:
            sifrelenmis_metin += chr(temp)

    print("Şifreli metin: {}".format(sifrelenmis_metin))

def sifre_cözme():
    print("Lütfen sadece harf kullanınız.")
    metin = input("Çözülecek şifreyi giriniz: ").upper()

    anahtar = 13
    cozulmus_sifre = ""

    for i in range(len(metin)):
        temp = ord(metin[i]) - anahtar
        if ord(metin[i]) == 32:
            cozulmus_sifre += " "
        elif temp < 65:
            temp += 26
            cozulmus_sifre += chr(temp)
        else:
            cozulmus_sifre += chr(temp)

    print("Şifrenin Çözülmüş Hali: {}".format(cozulmus_sifre))


def secenekler():
    secim = int(input("1. Şifreleme\n2. Şifre Çözme\nSeçiniz(1,2): "))
    if secim == 1:
        print("---Şifreleme---")
        metin_sifreleme()

    elif secim == 2:
        print("---Şifre Çözme---")
        sifre_cözme()

    else:
        print("Geçersiz Seçim")


if __name__ == "__main__":
    secenekler()