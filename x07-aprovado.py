# crie um programa que receba duas notas de um aluno, calcule a media dessa notas
# se a media for maior ou igual a sete o aluno esta aprovado, senao reprovado #
nota1 = int ( input ( 'nota 1: ' ) )
nota2 = int ( input ( 'nota 2: ' ) )
media = (nota1 + nota2) / 2
print(f'media = {media}')
if media >= 7:
    print ('APROVADO')
else:
    print ('REPROVADO')