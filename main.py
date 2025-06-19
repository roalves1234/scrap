print("Inicializando...")
from ObtencaoHtml import ObtencaoHtml
from ObtencaoLinguagem import ObtencaoLinguagem
from ColetagemOpiniaoUsuario import ColetagemOpiniaoUsuario

html = ObtencaoHtml().get()
linguagens = ObtencaoLinguagem = ObtencaoLinguagem(html).get()

for linguagem in linguagens[:3]:
    print('\n\n')
    print(f"\033[1m## Linguagem: {linguagem.get('name')}  |  Percentual de participação: {linguagem.get('rating')}  |  Taxa de crescimento: {linguagem.get('change')} ##\n\033[0m")
    print(ColetagemOpiniaoUsuario(False).get(linguagem.get('name')))