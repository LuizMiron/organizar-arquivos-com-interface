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
diretorios = tkinter.Frame(janela)
diretorios.pack()
cOrigem = tkinter.Frame(diretorios)
cOrigem.pack(side=tkinter.TOP)
cDestino = tkinter.Frame(diretorios)
cDestino.pack(side=tkinter.BOTTOM)

#2.1 ADICIONANDO A ORIGEM
# label com explicando o funcionamento
texto = tkinter.Label(cOrigem, text="adicione a origem")
texto.pack(side=tkinter.TOP)

#input de origem
vOrigem = tkinter.Entry(cOrigem, width=60)
vOrigem.pack(side=tkinter.LEFT)

#botão de origem
btnOrigem = tkinter.Button(cOrigem, text="procurar", command=obter_origem)
btnOrigem.pack(side=tkinter.RIGHT)


#2.2 ADICIONANDO O DESTINO
# label com explicando o funcionamento
texto = tkinter.Label(cDestino, text="adicione o destino")
texto.pack(side=tkinter.TOP)
# input de destino
vDestino = tkinter.Entry(cDestino, width=60)
vDestino.pack(side=tkinter.LEFT)
# botão de origem
btnOrigem = tkinter.Button(cDestino, text="procurar", command=obter_destino)
btnOrigem.pack(side=tkinter.RIGHT)

janela.mainloop()
