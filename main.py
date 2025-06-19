print("Inicializando...")
from ObtencaoHtml import ObtencaoHtml
from ObtencaoLinguagem import ObtencaoLinguagem
from Comum.Utils.utils import FileTool
from Work import Work

html = ObtencaoHtml().get()
linguagens = ObtencaoLinguagem = ObtencaoLinguagem(html).get()
arquivo_resultado = FileTool('resultado.md')
arquivo_resultado.save("")

print('\n')
resultado = ""

for linguagem in linguagens[:2]:
    print(f"** Linguagem: {linguagem.get('name')} **\n")
    resultado += Work().get(linguagem)
    arquivo_resultado.save(resultado) 
