dinheiro = True
senha = False


if dinheiro == True and senha == True:
    print('Sacar')

elif dinheiro == True and senha == False:
    print('Senha Invalida!')

elif dinheiro == False and senha == True:
    print('Saldo Insuficiente')
elif dinheiro ==   False and senha == False:
    print('Dados incorretos')




