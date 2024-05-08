import time
import threading

compteur = 0


    







def f_compteur(nb, id, mutex):
    global compteur
    for i in range(nb):
        with mutex:
            tmp = compteur
            time.sleep(0.5)
            compteur = tmp + 1
            print(compteur, id)


t1 = threading.Thread(target=f_compteur, args=(8,1))
t2 = threading.Thread(target=f_compteur, args=(10,2))
t1.start()
t2.start()