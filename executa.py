from main import Automóvel

carro=Automóvel('','','','')
carro.ligar='ligar'
carro._desligar='desligar'
carro.__potencia='200 cavalos'
carro.motor='150'
carro.ligando()
carro.caracaterísticas()
carro.desligando()
print()

from HB20 import HB20

carro2=HB20('','','','','','')
carro2.ligar='ligar'
carro2._desligar='desligar'
carro2.__potencia='350 cavalos'
carro2.motor='350'
carro2.modelo='HB20'
carro2.marca='Hyundai'
carro2.ligando()
carro2.caracaterísticas()
carro2.desligando()
print()