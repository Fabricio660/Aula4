"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

valor = float(input('Digite um valor '))

if valor > 0:
    print('Valor Positivo')

elif valor < 0:
    print('Valor Negativo')

else:
    print('Valor igual a zero')    