import json

class Personagem:
    def __init__(self, nome, idade, altura, peso, genero, classe):
        self._nome = nome.title()
        self._classe = classe.title()
        self._raca = "Desconhecida"
        self._idade = idade
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self._atributos = Atributos().define_atributos(classe)
        # self.poder_de_raca = #DEFINIR DEPOIS
    
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
Classe: {self._classe}
Raça: {self._raca}
Idade: {self._idade}
Altura: {self.altura}
Peso: {self.peso}
Genero: {self.genero}'''
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