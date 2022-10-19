from tkinter.filedialog import askdirectory
import os
from genericpath import isfile
from typing import Dict
from csv import DictReader


#criando caminho do arquivo para salvar
def salvar(origem, destino):
    with open(os.path.join("itens", "diretorios.csv"), 'w') as diretorio:
        diretorio.write('origem,destino\n')
        diretorio.write(f'{origem},{destino}\n')


def executar():
    with open(os.path.join("itens", "diretorios.csv")) as dcsv:
        reader = DictReader(dcsv)
        for linha in reader:
            orig = linha['origem']
            dist = linha['destino']
            # faz a copia
            print(orig)
            print(dist)
    organizar(dist, orig)

# lista dos diretorios das pastas
dicionario = dict()

# lista de extensões de cada tipo
audios_ext = ['.mp3', '.wav']
imagens_ext = ['.img', '.jpg', '.jpeg', '.png']
documentos_ext = ['.txt', '.doc', '.docx', '.pdf', '.log']
videos_ext = ['.mp4', '.mov', '.avi']

# 1. Criar pastas: imagens, audios e documentos obs: pasta "outros" já existe
def criar_pastas(diretorio):
    global dicionario
    dicionario.update({'audios': os.path.join(diretorio, 'audios')})
    dicionario.update({'imagens': os.path.join(diretorio, 'imagens')})
    dicionario.update({'docs': os.path.join(diretorio, 'documentos')})
    dicionario.update({'videos': os.path.join(diretorio, 'videos')})
    dicionario.update({'outros': os.path.join(diretorio, 'outros')})

    for pasta in dicionario.values():
        if not os.path.isdir(pasta):
            os.mkdir(pasta)


# Função para pegar a extensão do arquivo
def ext_arquivos(nome):
    index = nome.rfind('.')
    return nome[index:]


# 2. Pegar o nome dos arquivos
def organizar(diretorioDist, diretorioOrig):
    criar_pastas(diretorioDist)
    arquivos = os.listdir(diretorioOrig)

    for arq in arquivos:
        if os.path.isfile(os.path.join(diretorioOrig, arq)):
            # 3. Pegar sua extensão para deternimar o seu tipo
            extensao = str(ext_arquivos(arq)).lower()
            print(arq, extensao)

            # 4. Mover determinado arquivo nas pastas, baseado no seu tipo
            nova_pasta = str()
            if extensao in audios_ext:
                nova_pasta = dicionario['audios']
            elif extensao in imagens_ext:
                nova_pasta = dicionario['imagens']
            elif extensao in documentos_ext:
                nova_pasta = dicionario['docs']
            elif extensao in videos_ext:
                nova_pasta = dicionario['videos']
            else:
                nova_pasta = dicionario['outros']

            velho = os.path.join(diretorioOrig, arq)
            novo = os.path.join(nova_pasta, arq)
            os.rename(velho, novo)
            print(f'Moveu: {velho} -> {novo}')
