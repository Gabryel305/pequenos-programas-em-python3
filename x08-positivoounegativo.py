# faca um programa que peca um valor e mostre na tela se o valor é positivo ou negativo
numero = int ( input( 'Informe um Valor: ' ) )
if numero < 0:
    print ( f' {numero} É um numero negativo' )
elif numero == 0:
    print ( 'Valor zero' )
else:
    print ( f'{numero} É um numero positivo' )