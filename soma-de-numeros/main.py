import funcao as f

print('Informe 10 números!')
numeros = f.cadastrar_num()
pares = f.num_par(numeros)
impares = f.num_impar(numeros)
total = f.calc_soma(numeros)

print(f'\n\n\n\n\nNúmeros Pare: {pares}\nNúmeros Impares: {impares}\nResultado da Soma: {total}')
