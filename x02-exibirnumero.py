# Faça um programa que peça um numero e entao mostre o a mensagem: "Numero informado foi [numero]"
numero = input('Digite um numero: ')
print(f'Foi informado o numero {numero}')
# Adicionei uma compração que mostra DUAS mensagens diferentes
if numero == '67': print(f'que número lindo cara!')
else : print(f'É um número comum.')