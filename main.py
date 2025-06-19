print("Inicializando...")
from ObtencaoHtml import ObtencaoHtml
from ObtencaoLinguagem import ObtencaoLinguagem
from ColetagemOpiniaoUsuario import ColetagemOpiniaoUsuario

html = ObtencaoHtml().get()
linguagens = ObtencaoLinguagem = ObtencaoLinguagem(html).get()

for linguagem in linguagens[:3]:
    print('\n\n')
    print(f"*** Linguagem: {linguagem.get('name')} | Percentual de participação: {linguagem.get('rating')} | Taxa de crescimento: {linguagem.get('change')} ***")
    print(ColetagemOpiniaoUsuario().get(linguagem.get('name')))