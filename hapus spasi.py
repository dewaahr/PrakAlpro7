def hapus_spasi(kalimat):
    # kalimat=kalimat.split()
    # print(*kalimat,sep=" ")
    
    hasil=' '.join(kalimat.split())
    print(hasil)

kalimat=input("Masukan Kalimat:")
hapus_spasi(kalimat)
