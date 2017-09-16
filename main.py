from pyhtplac import *
import time

com = ComHtplac()
cont = 0
while cont < 10:
    print com.ligar_rele(1, True)
    cont+=1
    time.sleep(1)

