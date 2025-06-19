from ColetagemOpiniaoUsuario import ColetagemOpiniaoUsuario

class Work:
    def __init__(self, verbose: bool = False):
        self.coletor = ColetagemOpiniaoUsuario(verbose)
    def get(self, linguagem):
        resultado = ""
        resultado += f"## Linguagem: {linguagem.get('name')}  |  Percentual de participação: {linguagem.get('rating')}  |  Taxa de crescimento: {linguagem.get('change')} ##\n\n"
        resultado += ColetagemOpiniaoUsuario().get(linguagem.get('name'))
        resultado += '\n\n\n'
        
        return(resultado)