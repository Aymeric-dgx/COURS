class XOR:
    def __init__(self, mess, key : list):
        self.mess = mess
        self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = key

    def crypter(self):
        binaire = ""
        crypt = ""
        for i in self.mess:
            tmp = bin(ord(i))[2:]
            while len(tmp) < 8:
                tmp = "0" + tmp
            for j in range(8):
                c = int(tmp[j])^self.key[j]
                binaire = binaire + str(c)

        for i in range(len(binaire)//8):
            tmp = binaire[i*8:i*8+8]
            c = chr(int(tmp, 2))
            crypt = crypt + c
        return crypt

    def decrypter(self):
        tmp = self.crypter()
        self.mess = tmp
        return self.crypter()

test = XOR("HELLO", [1, 0, 1, 0, 1, 0, 1, 0])
c = test.crypter()
print(c)
d= test.decrypter()
print(d)