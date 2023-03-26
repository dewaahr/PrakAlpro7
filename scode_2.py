def frekuensi(kalimat,kata):
    kalimat_bersih=''
    frekuensi_kata=0

    for karakter in kalimat:
        if karakter.isalpha() or karakter.isnumeric():
            kalimat_bersih=kalimat_bersih+karakter
        if karakter.isspace():
            kalimat_bersih=kalimat_bersih+' '

    kalimat_bersih=kalimat_bersih.split()

    for kata_cek in kalimat_bersih:
        if kata_cek==kata:
            frekuensi_kata=frekuensi_kata+1
    return frekuensi_kata

kalimat=input('Masukan Kalimat:').lower()
kata=input('Masukan Kata yang ingin dicari:').lower()
jumlah_frekuensi=frekuensi(kalimat,kata)
print(f"Kata {kata} ada {jumlah_frekuensi} buah")