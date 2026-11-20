# desenvolva um programa, utilizando while, que permite ao usuário realizar operações de
# adição repetidamente, enquanto ainda quiser#

quant = int(input('Vezes de repetição: '))
plus = 0
i = 0

while i < quant:
	i += 1
	
	num = int(input(f'{i}º número: '))
	plus += num
	
	print(f'Total: {plus}')
