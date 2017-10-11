from pyhtplac import *
import time

com = ComHtplac()

print com.teste_conexao()

start = time.time()

PERIOD_OF_TIME = 1  # 120 min

while True :
    print com.ler_entrada(1)
    if time.time() > start + PERIOD_OF_TIME: break

com.fechar_conexao()