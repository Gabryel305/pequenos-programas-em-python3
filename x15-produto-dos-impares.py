# Escreva um programa que calcule e imprima o produto dos inteiros impares de 1 a 15
# sera necessário descobrir se um numero é ou não impar. Utilizea estrutura (for)#
produto = 1

	# contador, verificador e produto
for i in range (0,16):
	
    if i % 2 != 0:
        produto *= i
        print(f'{i} impar')

print(f'O produto dos inteiros impares de 1 a 15 é: {produto}\nFim')
