import json
class Personagem:
    def __init__(self, nome, idade, altura, peso, genero, classe):
        self.nome = nome.title()
        self.raca = "Desconhecida"
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.atributos_base = self.define_classe(classe)
    
    @property
    def atributos(self):
        atributos = self.atributos_base.items()
        for item, coiso in atributos:
            print(item, coiso)

    def sobe_um_level(self, atributo):
        self.atributos_base[atributo] += 1

    def __str__(self):
        personagem = f''' 
Nome: {self.nome}
Raça: {self.raca}
Idade: {self.idade}
Altura: {self.altura}
Peso: {self.peso}
Genero: {self.genero}'''
        return personagem

    def define_classe(self, classe):
        caminho = 'json.json'
        with open(caminho, 'r', encoding='UTF-8') as arquivo:
            x = json.load(arquivo)
            for classes in range(len(x)):
                if classe in x[classes]:
                    index_classe = classes
        classe_escolhida = x[index_classe].values()
        for x in classe_escolhida:
            self.atributos_base = x
        return self.atributos_base
