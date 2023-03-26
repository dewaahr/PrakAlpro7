def terpendek_terpanjang(kalimat):

    kalimat_bersih=''
    for karakter in kalimat:
        if karakter.isalpha() and karakter.isnumeric():
            kalimat_bersih=kalimat_bersih+karakter
        if karakter.isspace():
            kalimat_bersih=kalimat_bersih+' '

    kalimat=kalimat.split()
    terpanjang=max(kalimat,key=len)
    terpendek=min(kalimat,key=len)
    print(f"Kata terpendek  : {terpendek}\nKata terpanjang : {terpanjang}")

kalimat=input("Masukan Kalimat:").lower()
terpendek_terpanjang(kalimat)