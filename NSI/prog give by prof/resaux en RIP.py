class Routeur :
    def __init__(self, id: int, table: dict):
        self.id = id
        self.table = table
    def emettre(self, m_adj, l_routeur):
        for i in range(len(l_routeur)):
            if m_adj[id][i] == 1:
                l_routeur[i].recept(self.id, self.table)
    def recept(self, id, table):
        for k in table:
            if k not in self.table:
                """self.table[k] = (table[k][0] + 1, id)"""

                





m_adj = [[0, 1, 0, 1, 0]
         [1, 0, 0, 1, 0]
         [0, 0, 0, 0, 1]
         [1, 1, 0, 0, 1]
         [0, 0, 1, 1, 0]]


r1 = Routeur(0,{"A" : (0,1)})
r2 = Routeur(1, {})
r3 = Routeur(3, {})
r4 = Routeur(2, {})
r5 = Routeur(4, {})

l_routeur = [r1, r2, r3, r4, r5]