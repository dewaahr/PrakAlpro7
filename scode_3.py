def hapus_spasi(kalimat):
    kalimat=kalimat.split()
    print(*kalimat,sep=" ")

kalimat=input("Masukan Kalimat:")
hapus_spasi(kalimat)