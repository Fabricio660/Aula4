"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido"""

Letra = input('Digite o sexo (F ou M)').upper() #converter

if Letra == "F":
    print('F - Feminino')

elif Letra == "M":
    print('M - Masculino')

else:
    print('Sexo Invalido')



