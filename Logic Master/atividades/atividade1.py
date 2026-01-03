"""Calculadora de IMC"""

peso = float(input('Digite seu peso em Kg: '))
alt = float(input('Digite sua altura: '))

imc = peso / (alt ** 2)

print(f'Seu IMC e: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso!')
elif imc < 25:
    print('Peso normal!')
elif imc < 30:
    print('Sobrepeso!')
elif imc < 35:
    print('Obesidade grau 1!')
elif imc < 40:
    print('Obesidade grau 2!')
else:
    print('Obesidade mórbita!')