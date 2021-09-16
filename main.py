import json

class Personagem:
    def __init__(self, nome, idade, altura, peso, genero, classe):
        self._nome = nome.title()
        self._raca = "Desconhecida"
        self._idade = idade
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self._atributos = self.define_classe(classe)
        self.poder_de_raca = #DEFINIR DEPOIS
    
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
Idade: {self._idade}
Altura: {self.altura}
Peso: {self.peso}
Genero: {self.genero}'''
        return personagem

    def define_classe(self, classe):
        caminho = 'json.json'
        with open(caminho, 'r', encoding='UTF-8') as arquivo:
            file = json.load(arquivo)
            for classes in range(len(file)):
                if classe in file[classes]:
                    index_classe = classes
        classe_escolhida = file[index_classe].values()
        for atributo in classe_escolhida:
            self._atributos = atributo
        return self._atributos
