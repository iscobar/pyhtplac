# -*- coding: utf-8 -*-
import serial


class ComHtplac:
    def __init__(self):
        # No Raspberry Pi 3 a porta mini UART (a que é pelo GPIO) é mapeada por padrão na /dev/ttyS0
        self.com = serial.Serial('/dev/ttyS0', 19200, timeout=0.1)

    # A função ligar_rele recebe o ID do Rele (1~8) e se ele deve ser ligado ou não
    def ligar_rele(self, id, ligar):
        if ligar:
            self.com.write('CMD+RLY%s=1\r' % id)
            retorno = self.com.readlines()
            return retorno
        else:
            self.com.write('CMD+RLY%s=0\r' % id)
            retorno = self.com.readlines()
            return retorno

    # A função ligar_saida recebe o ID da porta digital (1~4) e se ela deve ser ligado ou não
    def ligar_saida(self, id, ligar):
        if ligar:
            self.com.write('CMD+OUT%s=1\r' % id)
            retorno = self.com.readlines()
            return retorno
        else:
            self.com.write('CMD+OUT%s=0\r' % id)
            retorno = self.com.readlines()
            return retorno

    # A função ler_entradaa recebe o ID da porta digital (1~12)
    def ler_entrada(self, id):
        self.com.write('CMD+IN%s\r' % id)
        retorno = self.com.readlines()
        return retorno