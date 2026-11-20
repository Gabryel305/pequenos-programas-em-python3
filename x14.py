# Escreva um programa que calcule o quadrado e o cube de 10 numero inteiro fornacidos pelo usuario
# Utilize uma estrutura de retiçao (for) controlada por contador para solucionar esse problema.#

# contador usando a variavel i, conta 10 numeros
for i in range(1, 11):
    # pede e calcula o numero
    num = int(input(f'{i}º número: '))
    print(f'Quadrado de {num} é: {num ** 2}')
    print(f'Cubo de {num} é: {num ** 3}')
