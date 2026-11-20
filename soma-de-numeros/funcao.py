def cadastrar_num():
	lista_num = []
	
	for i in range(10):
		num = int(input(f'{i + 1}º Número: '))
		lista_num.append(num)
	
	return lista_num
	
def num_par(lista):
	par = []
	
	for num in lista:
		if num % 2 == 0:
			par.append(num)
			
	return par

def num_impar(lista):
	impar = []
	
	for num in lista:
		if num % 2 != 0:
			impar.append(num)
	
	return impar
			
def calc_soma(lista):
	soma = sum(lista)
	
	return soma
