def palindrome(kalimat):
    kalimat=kalimat.lower()
    kalimat_bersih_1=""
    for karakter in kalimat:
        if  karakter.isalpha():
            kalimat_bersih_1=kalimat_bersih_1+karakter
    kalimat_bersih_2=kalimat_bersih_1[::-1]
    if kalimat_bersih_1==kalimat_bersih_2:
        return True
    else: return False
kalimat=input('Masukan Kalimat:')
hasil=palindrome(kalimat)
print(hasil)
