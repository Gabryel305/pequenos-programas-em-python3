import tkinter as tk
import random as r

num = r.randint(1,100)
tent = 0

	# Verificador do número
def verify():
    global tent
    tent += 1

    palp = int(campo.get())

    if palp < num:
        resultado.config(text = 'O número é MAIOR!')
    elif palp > num:
        resultado.config(text = 'O número é MENOR!')
    else:
        resultado.config(text = f'Acertou! Tentativas {tent}')

	# Interface Gráfica
janela = tk.Tk()
janela.title('Acerte o Número')
janela.geometry('600x400')

titulo = tk.Label(janela,text = 'QUE NÚMERO É?', font = ('Arial',22))
titulo.pack(pady = 20)

intrucao = tk.Label(janela, text = 'Pensei em um número entre 1 a 100.\nQual número é o seu palpite?')
intrucao.pack()

campo = tk.Entry(janela)
campo.pack(pady = 10)

botao = tk.Button(janela, text = 'Tentar', command = verify)
botao.pack()

resultado = tk.Label(janela, text = '', font = ('Arial',22))
resultado.pack(pady = 20)

janela.mainloop()
