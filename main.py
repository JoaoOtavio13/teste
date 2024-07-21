class Automóvel:
    def __init__(self,ligar,desligar,potencia,motor):
        self.ligar=''
        self.desligar=''
        self.potencia=''
        self.motor=''

    def ligando(self):
        print(self.ligar)
    
    def desligando(self):
        print(self.desligando)

    def caracaterísticas(self):
        print(f'seu  carro tem {self.potencia} e {self.motor} de potência do motor')