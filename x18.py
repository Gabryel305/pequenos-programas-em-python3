def cadastrar():
	print('Informe o nome de 5 pessoas.')
	nomes = []
	
	for i in range(5):
		nome = input(f'{i+1}º Nome: ')
		nomes.append(nome)
		
	return nomes
	
def exibir(lista):
	print('\n\n\n\nPessoas Cadastradas:')
	for nomes in lista:
		print(nomes)
		
# Programa Principal
n_lista = cadastrar()
exibir(n_lista)
