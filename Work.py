from Comum.Utils.utils import FileTool
from ColetagemOpiniaoUsuario import ColetagemOpiniaoUsuario

class WorkLinguagem:
    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def get_comentarios(self, linguagem):
        print(f"** Linguagem: {linguagem.get('name')} **\n")
        resultado = ""
        resultado += f"## Linguagem: {linguagem.get('name')}  |  Percentual de participação: {linguagem.get('rating')}  |  Taxa de crescimento: {linguagem.get('change')} ##\n\n"
        resultado += ColetagemOpiniaoUsuario(self.verbose).get(linguagem.get('name'))

        resultado += '\n\n\n'

        return(resultado)
    
    def get_lista(self, linguagens):
        resultado = ""
        resultado += f"| {'LINGUAGEM DE PROGRAMAÇÃO':<25} | {'% PARTICIPA':>11} | {'CRESCIMENTO':>11} |\n"
        for linguagem in linguagens:
            resultado += f"| {linguagem.get('name'):<25} | {linguagem.get('rating'):>11} | {linguagem.get('change'):>11} |\n"
        
        return(resultado)
    
class WorkFile:
    def __init__(self):
        self.texto = ""
        self.arquivo_resultado = FileTool('resultado.md')
    
    def add(self, conteudo: str):
        self.texto += conteudo
        self.arquivo_resultado.save(self.texto)
    
    def clear(self):
        self.arquivo_resultado.save("")
    