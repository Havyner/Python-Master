"""Calculadora de Lucros em Carros"""

valor_Pago = float(input('Valor da compra do carro: '))
valor_Manutencao = float(input('Valor investido em manutenções: '))
valor_Venda = float(input('Valor da venda do carro: '))

custo = valor_Pago + valor_Manutencao
lucro = valor_Venda - custo

print(f'Valor total gasto no carro: {custo:.2f}')

if lucro < 0:
    print(f'Você teve um prejuízo de: {lucro:.2f}')
elif lucro == 0:
    print(f'Você ficou no 0x0: {lucro:.2f}')
else:
    print(f'Você teve um lucro de: {lucro:.2f}')