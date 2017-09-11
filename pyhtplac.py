import serial


class ComHtplac:
    def __init__(self):
        self.com = serial.Serial('/dev/ttyS0', 19200, timeout=0.1)

    def ligar_rele(self, id, ligar):
        if ligar:
            self.com.write('CMD+RLY%s=1\r' % id)
            retorno = self.com.readlines()
            return retorno
        else:
            self.com.write('CMD+RLY%s=0\r' % id)
            retorno = self.com.readlines()
            return retorno
