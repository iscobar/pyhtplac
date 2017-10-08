from pyhtplac import *
import time

start = time.time()

com = ComHtplac()

PERIOD_OF_TIME = 7200  # 120 min

while True :
    print com.ligar_rele(1, True)
    time.sleep(5)
    print com.ligar_rele(1, False)

    if time.time() > start + PERIOD_OF_TIME : break
