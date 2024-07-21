class Automóvel:
    def __init__(self,ligar,_desligar,__potencia,motor):
        self.ligar=''
        self._desligar=''
        self.__potencia=''
        self.motor=''

    def ligando(self):
        print(self.ligar)
    
    def desligando(self):
        print(self.desligando)

    def caracaterísticas(self):
        print(f'seu  carro tem {self.potencia} e {self.motor} de potência do motor')