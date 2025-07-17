"""
Faça um Programa que peça dois números e imprima o maior deles."""

numero1 = float(input('Didite o primeiro numero'))
numero2 = float(input('Digite o segundo numero'))

if numero1 > numero2:
    print('O maior número e',numero1)

elif numero2 > numero1:
    print('O maior número e',numero2)

else:
    print('Os doi números são iguais')    

