def translate_alay(kalimat):
    huruf_normal="aAiIeEoOjJgGbrRsSB"
    huruf_alay="441133007799622558"
    hasil=""
    for karakter in kalimat:
        if karakter in huruf_normal:
            posisi=huruf_normal.index(karakter)
            hasil=hasil+huruf_alay[posisi]
        else: hasil=hasil+karakter
    return hasil


kalimat=input("Kalimat:")

hasil= translate_alay(kalimat)

print(hasil)