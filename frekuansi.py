def frekuensi(kalimat,kata):
    kalimat=kalimat.lower()
    kalimat=kalimat.replace('.','')
    kalimat=kalimat.replace(',','')
    kalimat=kalimat.split(' ')
    kata=kata.lower()
    frekuensi_kata=0
    for kata_cek in kalimat:
        if kata_cek==kata:
            frekuensi_kata=frekuensi_kata+1
    return frekuensi_kata


kalimat=input('Masukan Kalimat:')
kata=input('Masukan Kata yang ingin dicari:')
jumlah_frekuensi=frekuensi(kalimat,kata)
print(jumlah_frekuensi)