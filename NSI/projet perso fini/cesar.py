#tester les set_key

class Cesar:
    def __init__(self, key, mess):
        self.key = key
        self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.mess = mess

    def set_key(self, key ):
        self.key = key
    def crypter(self):
        crypt = ""
        for i in self.mess:
            c = self.alpha[(self.alpha.index(i) + self.key)%26]
            crypt = crypt + c
        return crypt
    def decrypter(self, crypt):
        decrypt = ""
        for i in crypt:
            d = self.alpha[(self.alpha.index(i)-self.key)%26]
            decrypt = decrypt + d
        return decrypt


mess = Cesar(154, "BONJOUR")

c = mess.crypter()
print(c)
d = mess.decrypter(c)
print(d)