from ObtencaoHtml import ObtencaoHtml
from ObtencaoLinguagem import ObtencaoLinguagem
from ColetagemOpiniaoUsuario import ColetagemOpiniaoUsuario

html = ObtencaoHtml().get()
linguagens = ObtencaoLinguagem = ObtencaoLinguagem(html).get()

#for linguagem in linguagens:
#    print(linguagem) 

resultado_pesquisa = ColetagemOpiniaoUsuario().get("Python")
print(resultado_pesquisa)