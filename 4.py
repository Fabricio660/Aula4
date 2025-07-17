"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante
"""
Letra = input('Digite uma Letra').lower()

if len(Letra) !=1 or not Letra.isalpha():
 print('Entrada invalida.Digite apenas uma letra do alfabeto')

elif letra in 'aeiou':
 print('vogal')
else:
 print('Consoantes')