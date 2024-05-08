class Vigenere:
    def __init__(self,  mess, key : list):
        self.mess = mess
        self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = key

    def crypter(self):
        cryp = ""
        x = -1
        for i in self.mess:
            if i == " ":
                cryp = cryp + " "
            else:
                x = x+1
                c = self.alpha[   (self.alpha.index(i) + self.key[x%len(self.key)])   %26]
                cryp = cryp + c
        return cryp

    def decrypter(self, cryp):
        decrypt = ""
        x = -1
        for i in cryp:
            if i == " ":
                decrypt = decrypt + " "
            else:
                x = x+1
                d = self.alpha[  (self.alpha.index(i) - self.key[x%len(self.key)])   %26]
                decrypt = decrypt + d
        return decrypt


clé = [5, 7, 4, 145, 52, 47]
mess = Vigenere("BONJOUR CA VA TOI", clé)
c = mess.crypter()
print(c)
d = mess.decrypter(c)
print(d)