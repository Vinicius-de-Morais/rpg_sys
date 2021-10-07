from abc import ABCMeta, abstractmethod


class Mascara:
    __metaclass__ = ABCMeta

    @abstractmethod
    def modifica_atributos(self):
        pass

    @abstractmethod
    def poder_de_classe(self):
        pass
