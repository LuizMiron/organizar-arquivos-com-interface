# importar módulos necessarios
import tkinter
from tkinter.filedialog import askdirectory
import funcoes


def obter_origem():
    origem = askdirectory()
    vOrigem.insert(tkinter.END, origem)
    
def obter_destino():
    destino = askdirectory()
    vDestino.insert(tkinter.END, destino)


# 1.CRIANDO UMA INTERFACE
# janela principal
janela = tkinter.Tk()
janela.geometry("500x600")
janela.title("main")

#2.1 ADICIONANDO A ORIGEM
# label com explicando o funcionamento
texto = tkinter.Label(janela, text="adicione a origem")
texto.grid(column=0, row=0)

#input de origem
vOrigem = tkinter.Entry(janela, width=60)
vOrigem.grid(column=0, row=1)

#botão de origem
btnOrigem = tkinter.Button(janela, text="procurar", command=obter_origem)
btnOrigem.grid(column=1, row=1)


#2.2 ADICIONANDO O DESTINO
# label com explicando o funcionamento
texto = tkinter.Label(janela, text="adicione o destino")
texto.grid(column=0, row=3)
#input de destino
vDestino = tkinter.Entry(janela, width=60)
vDestino.grid(column=0, row=4)
#botão de origem
btnOrigem = tkinter.Button(janela, text="procurar", command=obter_destino)
btnOrigem.grid(column=1, row=4)

janela.mainloop()
