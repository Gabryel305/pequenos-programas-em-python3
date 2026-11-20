# faca um programa que peca dois numero e mostre o maior deles#
numero1 = int ( input ( '1° Valor: ' ) )
numero2 = int ( input ( '2° Valor: ' ) )
if numero1 > numero2:
    print ( f'{numero1} É maior que {numero2}' )
elif numero1 < numero2:
    print ( f'{numero2} É maior que {numero1}' )
else:
    print ( f'Os numeros são iguais' )