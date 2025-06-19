import sys
from ObtencaoHtml import ObtencaoHtml
from ObtencaoLinguagem import ObtencaoLinguagem
from ColetagemOpiniaoUsuario import ColetagemOpiniaoUsuario

sys.stdout = open('crewlog_.txt', 'a')
html = ObtencaoHtml().get()
linguagens = ObtencaoLinguagem = ObtencaoLinguagem(html).get()

#for linguagem in linguagens:
#    print(linguagem)
    
resultado_pesquisa = ColetagemOpiniaoUsuario().get("Python")