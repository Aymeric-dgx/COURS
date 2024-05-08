# Créé par charles.clercq, le 24/02/2023 en Python 3.7

class Cesar:
    def __init__(self):
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    def chiffre(self, msg, clef):
        ch = ''
        for l in msg:
            if l in self.alphabet :
                ch = ch + self.alphabet[(self.alphabet.index(l)+clef)%len(self.alphabet)]
            else:
                ch = ch + l
        return ch

    def dechiffre(self, ch, clef):
        msg = ''
        for l in ch:
            if l in self.alphabet:
                msg = msg + self.alphabet[(self.alphabet.index(l)+(len(self.alphabet)-clef))%len(self.alphabet)]
            else :
                msg = msg + l
        return msg

if __name__ == '__main__':
    method = Cesar()
    ch = method.chiffre('ABC', 1)
    print(ch)
    msg = method.dechiffre(ch, 1)
    print(msg)

    clef = 13
    ch = method.chiffre('DIANTRE, MAIS COMMENT A TU FAIS ? JD', clef)
    print(ch)
    msg = method.dechiffre(ch, clef)
    print(msg)

    clef = 3
    ch = method.chiffre('LE MESSAGE PRECEDENT ETAIT TROP EVIDENT ! TRICHEUR', clef)
    print(ch)
    msg = method.dechiffre(ch, clef)
    print(msg)