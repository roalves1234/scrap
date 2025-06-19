from Equipe import Equipe

class ColetagemOpiniaoUsuario:
    def __init__(self):
        pass
    
    def get(self, linguagem):
        return(Equipe().get(linguagem))