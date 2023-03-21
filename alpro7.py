def hitung_vokal(kalimat):
    vokal="aiueoAIUEO"
    jumlah=0
    for karakter in kalimat:
        if karakter in vokal:
            jumlah=jumlah+1
    return jumlah

def hitung_blank(kalimat):
    jumlah=0
    for karakter in kalimat:
        if karakter.isspace()== True:
            jumlah=jumlah+1
    return jumlah

def hitung_angka(kalimat):
    angka='1234567890'
    jumlah=0
    for karakter in kalimat:
        if karakter in angka:
            jumlah=jumlah+1
    return jumlah

def hitung_konsonan(kalimat):
    # konsonan='qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
    vokal="aiueoAIUEO"
    jumlah=0
    for karakter in kalimat:
        # if karakter in konsonan:
        if karakter not in vokal and karakter.isalpha():
            jumlah=jumlah+1
    return jumlah

kalimat=input("Kalimat:")


jumlah_vokal=hitung_vokal(kalimat)
jumlah_blank=hitung_blank(kalimat)
jumlah_angka=hitung_angka(kalimat)
jumlah_konsonan=hitung_konsonan(kalimat)


print(f"jumlah huruf vokal : {jumlah_vokal}")
print(f"jumlah huruf konsonan : {jumlah_konsonan}")
print(f"jumlah blank : {jumlah_blank}")
print(f"jumlah angka : {jumlah_angka}")