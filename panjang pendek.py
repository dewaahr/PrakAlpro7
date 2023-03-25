def terpendek_terpanjang(kalimat):
    kalimat=kalimat.lower()
    kalimat=kalimat.replace('.','')
    kalimat=kalimat.replace(',','')
    kalimat=kalimat.split(' ')
    kalimat.sort()
    terpanjang=kalimat[0]
    terpendek=kalimat[-1]
    print(f"Terpendek : {terpendek}\nTerpanjang : {terpanjang}")
    print(terpanjang)

kalimat=input("Masukan Kalimat:")
terpendek_terpanjang(kalimat)
