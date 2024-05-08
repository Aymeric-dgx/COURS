g = {"a": ["e","b"], "b" : ["a", "c", "d"], "c" : ["b", "d"], "d" : ["b", "c"],"e": ["a"]}


def parcours(graph, debut):
    mem = []
    def sub_parcours(graph,debut, mem):
        for i in graph[debut]:
            if not i in mem:
                mem.append(i)
                sub_parcours(graph, i, mem )
    sub_parcours(graph, debut, mem)

def rech_chemin(graph, debut, fin):
    mem = []
    chemin = []
    def sub_rech_chemin(graph, debut, fin, mem):
        for i in graph[debut]:
            if not i in mem:
                mem.append(i)
                if i == fin:
                    chemin.append(i)
                    sub_rech_chemin(graph,    )
                else:
                    sub_rech_chemin(graph, i, fin, mem)
        print(chemin)
    sub_rech_chemin(graph, debut, fin, mem)


"""def rech_chemin(graph, debut, fin, mem):
    mem = []
    chemin = []"""




rech_chemin(g, "b", "d")

