class Carro():
    numero_rodas = 4
    qnt_passageiros = 5

    def acelerar(self):
        print("Acelerando..")

    def frear(self):
        print("Freando...")

    def buzinar(self):
        print("Buzinando...")

class Uno(Carro):
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 2000

uno = Uno()
uno.acelerar()
print(uno.numero_rodas)