from pyhtplac import *
import time

com = ComHtplac()

print com.teste_conexao()

print com.ligar_rele(1, True)

time.sleep(1)

print com.ligar_rele(1, False)
