# Muhammad Yusuf
# 5220600048

def dekripsi():
    Alpabeth1 = "abcdefghijklmnopqrstuvwxyz"
    input_encrypted = str(input("Masukan pesan : " ))

    for key in range(len(Alpabeth1)):
        translated = ""
        for symbol in input_encrypted:
            if symbol in Alpabeth1:
                num = Alpabeth1.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(Alpabeth1)
                translated = translated + Alpabeth1[num]
            else:
                translated = translated + symbol

        print('key pesan %s: %s' % (key, translated))

def main():
    dekripsi()


if __name__ == '__main__':
    main()
