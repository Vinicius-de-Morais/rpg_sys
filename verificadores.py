from abc import ABCMeta, abstractmethod


class Mascara:
    __metaclass__ = ABCMeta

    @abstractmethod
    def verifica(self):
        pass


class RealizaVerificacao:
    def __init__(self, raca, altura):
        self._raca = raca
        self.altura = altura

        self.verifica()

    def verifica(self):
        verificadores = [VerificaAltura, VerificaRaca]

        for verificador in verificadores:
            verificador.verifica(self)


class VerificaAltura(Mascara):

    def verifica(self):
        if type(self.altura) != float:
            raise ValueError('Altura deve ser declarada como um float. EX: 1.70')

        elif self.altura < 1.60 and self._raca == 'Gigante' or self.altura < 1.60 and self._raca == 'Anão':
            raise Exception('Um Gigante ou Anão não pode ter menos de 1.60 de altura')


class VerificaRaca(Mascara):

    def verifica(self):
        pass
