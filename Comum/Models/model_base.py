from abc import ABC, abstractmethod

class ILLM_Model(ABC): 
    @abstractmethod
    def set_prompt(self, prompt: str):
        pass

    @abstractmethod
    def get(self) -> str:
        pass

    @property
    def nome(self) -> str:
        resultado = self.__class__.__name__
        return resultado