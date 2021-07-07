from abc import ABCMeta


class Personagem(metaclass=ABCMeta):
    def __init__(self, nome, idade, altura, peso, genero, classe):
        self.nome = nome.title()
        self.raca = ""
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.classe = classe
        self.vida = ""
        self.atributos_base = {
            'força': 0,
            'destreza': 0,
            'inteligencia': 0,
            'fe': 0,
            'sabedoria': 0,
            'resistencia': 0,
            'carisma': 0,
            'sorte': 0
        }


    def set_classe(self):
        
        if self.classe == 'Cavaleiro Andante':
            self.atributos_base['força'] = 3
            self.atributos_base['destreza'] = 2
            self.atributos_base['resistencia'] = 2
            self.atributos_base['carisma'] = 2
            
        return self.atributos_base
    
    def __str__(self):
        print(f''' 
        Nome: {self.nome}
        Raça: {self.raca}
        Idade: {self.idade}
        Altura: {self.altura}
        Peso: {self.peso}
        Genero: {self.genero}
        Classe: {self.classe}
        ''')

persona = Personagem('Jorge', 41, 1.90, '71 kg', 'Masculino', 'Cavaleiro Andante')
persona.set_classe()
# print(persona.atributos_base)
atributos = persona.atributos_base.items()
for linha in atributos:
    print(linha)
