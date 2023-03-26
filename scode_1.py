def cek_anagram(kata1,kata2):
    list_kata1=sorted(kata1)
    list_kata2=sorted(kata2)
    if list_kata1==list_kata2:
            print(f"{kata1} dan {kata2} adalah Anagram")
    else:
            print(f"{kata1} dan {kata2} bukanlah Anagram")
            
kata1=input('Masukan Kata 1:').lower()
kata2=input('Masukan Kata 2:').lower()

cek_anagram(kata1,kata2)