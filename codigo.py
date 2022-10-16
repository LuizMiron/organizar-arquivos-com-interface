from gc import collect
import tkinter
from tkinter.filedialog import askdirectory



# janela principal
janela = tkinter.Tk()
janela.title("main")

texto = tkinter.Label(janela, text="aqui se tem um texto")
texto.grid(column=0, row=0)

# seleciona o diretorio e printa no terminal
diretorio = askdirectory()
print(diretorio)


janela.mainloop()