import string
abjad = string.printable

def deskrip (chiper) :
    global abjad
    key = int(input('key:'))
    pesan = ''

    for i in chiper:
        if i in abjad:
            k=abjad.find(i)
            k=(k-key)%100
            pesan = pesan+abjad[k]
        else:
            pesan = pesan + i
    return pesan

if __name__=='__main__':
    cipher = input ('pesan:')
    print(deskrip(cipher))
