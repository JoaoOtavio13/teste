from main import Automóvel

class HB20(Automóvel):
    def __init__(self, ligar, desligar, potencia, motor, modelo, marca):
        Automóvel.__init__(ligar, desligar, potencia, motor)
        self.modelo=''
        self.marca=''

    def ligando(self):
        print('ta ligando')

    def getcarateristicas_do_HB20(self):
        print(f'o meu carro é modelo {self.modelo} de marca {self.marca}')