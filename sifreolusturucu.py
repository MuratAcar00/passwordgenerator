import random
import string

def sifre_olustur(uzunluk=12, buyuk_harf=True, kucuk_harf=True, sayi=True, ozel_karakter=True):
    karakter_havuzu = ""
    if buyuk_harf:
        karakter_havuzu += string.ascii_uppercase
    if kucuk_harf:
        karakter_havuzu += string.ascii_lowercase
    if sayi:
        karakter_havuzu += string.digits
    if ozel_karakter:
        karakter_havuzu += string.punctuation

    if not karakter_havuzu:
        raise ValueError("En az bir karakter türü seçmelisiniz!")

    sifre = ''.join(random.choice(karakter_havuzu) for _ in range(uzunluk))
    return sifre

# Kullanıcıdan bilgileri alma kısmı
try:
    uzunluk = int(input("Şifre uzunluğunu girin (varsayılan 12): ") or 12)
    buyuk_harf = input("Büyük harfler eklensin mi? (E/h): ").lower() != 'h'
    kucuk_harf = input("Küçük harfler eklensin mi? (E/h): ").lower() != 'h'
    sayi = input("Sayılar eklensin mi? (E/h): ").lower() != 'h'
    ozel_karakter = input("Özel karakterler eklensin mi? (E/h): ").lower() != 'h'

    sifre = sifre_olustur(uzunluk, buyuk_harf, kucuk_harf, sayi, ozel_karakter)
    print(f"Oluşturulan şifre: {sifre}")

except ValueError as e:
    print(f"Hata: {e}")
