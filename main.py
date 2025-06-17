from ObtencaoHtml import ObtencaoHtml
from ObtencaoLinguagem import ObtencaoLinguagem

html = ObtencaoHtml().get()

linguagens = ObtencaoLinguagem = ObtencaoLinguagem(html).get()
print('Linguagens encontradas:', linguagens)