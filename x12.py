# Desenvolva um programa que leia um nome de usuário e a sua senha
# e não aceite a senha igual ao nome do usuário
# mostrando uma mensagem de erro e voltando a pedir as informações#
while True:
    user = input('Usuário: ')
    passkey = input('Senha: ')
    if user == passkey:
        print('error (01)')
    else:
        print('Usuário e senha definidos!')
        break;