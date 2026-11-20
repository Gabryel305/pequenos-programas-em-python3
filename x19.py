def cad_notas():
	n_lista = []
	
	for i in range(5):
		nota = float(input(f'{i+1}ª Av.: '))
		n_lista.append(nota)
		
	return n_lista

def calc_media(n_todas):
	media = sum(n_todas) / len(n_todas)
	
	return media
	
def exibir_notas(notas, media):
	print('\n\n\n\nNotas: {} \nMédia: {}'.format(notas, media))

	# Programa Principal
lista = cad_notas()
result = calc_media(lista)
exibir_notas(lista, result)
