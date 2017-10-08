from pyhtplac import *
import time

com = ComHtplac()

print com.teste_conexao()

time.sleep(1)

print com.ligar_saida(1, True)

time.sleep(5)

print com.ligar_saida(1, False)

com.fechar_conexao()
