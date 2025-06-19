print("Inicializando...")
from ObtencaoHtml import ObtencaoHtml
from ObtencaoLinguagem import ObtencaoLinguagem
from Work import WorkLinguagem, WorkFile

work_file = WorkFile()
work_linguagem = WorkLinguagem()
html = ObtencaoHtml().get()
linguagens = ObtencaoLinguagem = ObtencaoLinguagem(html).get()
quantidade = 2

work_file.clear()
work_file.add("# LINGUAGENS MAIS USADAS\n\n")
work_file.add(work_linguagem.get_lista(linguagens))

work_file.add("\n\n")
work_file.add(f"# COMENTÁRIOS SOBRE AS {quantidade} PRIMEIRAS LINGUAGENS\n\n")
for linguagem in linguagens[:quantidade]:
    work_file.add(work_linguagem.get_comentarios(linguagem))
