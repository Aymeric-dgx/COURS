objet = {"A" : [13, 700], "B" : [12, 400], "C" : [8, 300], "D" : [10, 300]} # [poids, valeur]
cap = 30 # capacité du sac

def sac(obj :dict, cap :int):
    val = 0
    def aux(obj, cap):
        if obj == {} or (len(obj) == 1 and obj[0][0] > cap):
            return val
        else:
            for i in obj:
                if obj[i][0] > cap:
                    del obj[i]
                else:
                    val = val + obj[i][1]
                    cap = cap - obj[i][0]
                    del obj[i]
                    a = aux(obj, cap)
                    b = val + obj[i][1]
                    return max(a, b)
        return val
    return aux(obj, cap)

print(sac(objet, cap))






#creer encore une autre fonction et bidouiller pour stocker une valeur en dehors de cette derneiere, et 
#la comparer avec une autre valeur modifié par la nouvelle fonction

def addition(dic :dict)->int:
    val = 0
    for i in dic:
        val = val + dic[i][1]
    return val

def sac(obj :dict, cap :int)->dict:
    sac = {}
    obj = dict(sorted(obj.items(), key=lambda x: x[1][0], reverse=True))
    def aux(obj :dict, cap :int, sac :dict, tmp =0):
        if len(obj) == 0 or obj[ list(obj.keys())[0] ][0] > cap:
            return sac
        else:
            for i in obj:
                if False:
                    print(i)
                else:
                    sac[i] = obj[i]
                    cap = cap - obj[i][0]
                    tmp_dic = obj.copy()
                    del tmp_dic[i]
                    tmp2 = addition(aux(tmp_dic, cap, sac))
                    if tmp2 > tmp:
                        tmp = tmp2
                        sac = aux(tmp_dic, cap, sac, tmp)
                    else:
                        return sac



    return aux(obj, cap, sac)






def backpack(objets  :dict, cap :int)->dict:
    sac = []
    tmp_sac = []
    obj = sorted(objets.items(), key=lambda x: x[1][0], reverse=True)  #transfomre le dic en liste de tupeles -> [(nom, [poids, valeurs]), (...), ...]]
    max_val = 0
    

    def addition(dic :list)->int:
        val = 0
        for i in range(len(dic)):
            val = val + dic[i][1][1]
        return val

    
    def sub_backpack(obj :list, cap :int, sac=[], max_val=0, tmp_sac=[])->list:
        if len(obj)==0 or obj[0][1][0] > cap:
            return tmp_sac
        else:
            for i in range(len(obj)):
                if len(tmp_sac)!=0:
                    del tmp_sac[-1]
                tmp_sac.append(obj[i])
                tmp_cap = cap - obj[i][1][0]
                tmp  = sub_backpack(obj[i+1:], tmp_cap, sac, max_val, tmp_sac)
                tmp_val = addition(tmp)
                if tmp_val > max_val:
                    max_val = tmp_val
                    sac = tmp
            return sac
                
    final_sac = sub_backpack(obj, cap)
    return final_sac

c = backpack(obj, cap)
print(c)