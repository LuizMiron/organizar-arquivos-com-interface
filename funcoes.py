from tkinter.filedialog import askdirectory
import os

# seleciona a origem e o destino escolhido


#criando caminho do arquivo para salvar
def salvar(origem, destino):
    with open(os.path.join("itens", "diretorios.csv"), 'w') as diretorio:
        diretorio.write('origem,destino\n')
        diretorio.write(f'{origem},{destino}\n')
    