def cek_anagram(kalimat1,kalimat2):
    kalimat1=kalimat1.lower()
    kalimat2=kalimat2.lower()
    a=sorted(kalimat1)
    b=sorted(kalimat2)
    if a==b:
            print("Anagram")
    else:
            print("Bukan")
kalimat1=input('Maasukan Kalimat 1:')
kalimat2=input('Maasukan Kalimat 2:')

cek_anagram(kalimat1,kalimat2)