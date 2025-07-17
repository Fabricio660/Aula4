#modulo
print(12 %4 == 0)

n = int(input('Digite um valor numerico'))

if(n % 2 == 0):  #mod se o resto e 0 e divivivel por 2 (par)
   #print (f' o {n} digitado e par')
    print('O número =>',n,'digitado e par')


elif(n % 2 == 1):
    #print(f'0 {n} digitado é impar')
    print('O número => ',n,'digitado e ímpar' )

else:
    print('Número digitado invalido')