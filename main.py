import json
from raças import DefineRaca
from verificadores import RealizaVerificacao


class Personagem:
    def __init__(self, nome, raca, idade, altura, peso, genero, classe):
        if RealizaVerificacao(raca, altura):
            self._nome = nome.title()
            self._classe = classe.title()
            self._idade = idade
            self.altura = altura
            self.peso = peso
            self.genero = genero
            self._atributos = Atributos().define_atributos(classe)
            self.poder_de_raca = None
            self._raca = DefineRaca(raca).define(self)
            self.bencao = self._atributos['Benção']
            self.treinado = ', '.join(self._atributos['Treinado'])
            self.itens = self._atributos['Itens']
            self.atributos_lista = list(self._atributos.items())[:8]

    @property
    def atributos(self):
        atributos = f'''Força: {self._atributos["Força"]}
Destreza: {self._atributos["Destreza"]}
Inteligência: {self._atributos["Inteligência"]}
Fé: {self._atributos["Fé"]}
Sabedoria: {self._atributos["Sabedoria"]}
Resistência: {self._atributos["Resistência"]}
Carisma: {self._atributos["Carisma"]}
Sorte: {self._atributos["Sorte"]} '''
        return atributos

    def sobe_um_level(self, atributo):
        self._atributos[atributo] += 1

    def __str__(self):
        personagem = f''' 
Nome: {self._nome}
Raça: {self._raca}
Classe: {self._classe}
Idade: {self._idade}
Altura: {self.altura}
Peso: {self.peso}
Genero: {self.genero}
**Poder de Raça**
{self.poder_de_raca}'''
        return personagem

    def salva_ficha(self):

        caminho = f'{self._nome}.txt'
        with open(caminho, 'w', encoding='UTF-8') as arquivo:
            arquivo.write('*******************')
            arquivo.write(self.__str__())
            arquivo.write('\n*******************\n')
            arquivo.write(self.atributos)
            arquivo.write('\n*******************')


class Atributos:

    @staticmethod
    def define_atributos(classe):
        try:
            caminho = 'classes.json'
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                file = json.load(arquivo)

                for classes in range(len(file)):
                    if classe in file[classes]:
                        index_classe = classes

            classe_escolhida = file[index_classe].values()
            for atributo in classe_escolhida:
                return atributo
        except:
            raise TypeError('Classe Invalida')

    @staticmethod
    def retorna_classes():
        caminho = 'classes.json'
        with open(caminho, 'r', encoding='UTF-8') as arquivo:
            arquivo = json.load(arquivo)
            classes = [item for classe in arquivo for item in list(classe.keys())]
        return classes
