print("""
***************************
Kullanıcı Girişi
***************************
""")

sys_kullanici_adi = "tinki"
sys_parola = "12345"

kullanici_adi = input("Kullanıcı Adı: ")
parola = input("Parola:")
if kullanici_adi == sys_kullanici_adi and parola!= sys_parola:
    print("Parola Hatalı!")
elif kullanici_adi != sys_kullanici_adi and parola == sys_parola:
    print("Kullanıcı Adı Hatalı!")
elif kullanici_adi != sys_kullanici_adi and parola != sys_parola:
    print("Kullanıcı Adı ve Parola Hatalı!")
else:
    print("Sisteme Başarıyla Giriş Yapıldı!")