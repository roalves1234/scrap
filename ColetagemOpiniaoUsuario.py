from Equipe import Equipe

class ColetagemOpiniaoUsuario:
    def __init__(self, verbose: bool):
        self.verbose = verbose
    
    def get(self, linguagem):
        return(Equipe(self.verbose).get(linguagem))