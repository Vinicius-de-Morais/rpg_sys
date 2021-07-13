
class Personagem():
    def __init__(self, nome, idade, altura, peso, genero, classe):
        self.nome = nome.title()
        self.raca = "Desconhecida"
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.classe = classe.title().strip()
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
 # Pretendo mudar e transformar cada classe em um objeto separado
 # Mas deixa isso pra outra hora.
        if self.classe == 'Cavaleiro Andante':
            self.atributos_base['força'] = 3
            self.atributos_base['destreza'] = 2
            self.atributos_base['resistencia'] = 2
            self.atributos_base['carisma'] = 2
        elif self.classe == 'Cavaleiro':
            self.atributos_base['força'] = 2
            self.atributos_base['destreza'] = 1
            self.atributos_base['inteligencia'] = 1
            self.atributos_base['resistencia'] = 3
            self.atributos_base['carisma'] = 3
        elif self.classe == 'Alquimista':
            self.atributos_base['destreza'] = 1
            self.atributos_base['inteligencia'] = 3
            self.atributos_base['sabedoria'] = 2
            self.atributos_base['resistencia'] = 1
            self.atributos_base['carisma'] = 3
        elif self.classe == 'Bardo':
            self.atributos_base['inteligencia'] = 1
            self.atributos_base['sabedoria'] = 1
            self.atributos_base['carisma'] = 5
            self.atributos_base['sorte'] = 3
        elif self.classe == 'Nobre':
            self.atributos_base = {x: 1 for x in self.atributos_base}
        elif self.classe == 'Oraculo':
            self.atributos_base['inteligencia'] = 1
            self.atributos_base['fe'] = 5
            self.atributos_base['sabedoria'] = 3
            self.atributos_base['resistencia'] = 1    
        return self.atributos_base
    
    @property
    def atributos(self):
        atributos = self.atributos_base.items()
        for item, coiso in atributos:
            print(item, coiso)

    def upa_lv (self):
        pass

    def __str__(self):
        atributos = self.atributos_base.items()
        for item, coiso in atributos:
            print(item, coiso)
        return f''' 
        Nome: {self.nome}
        Raça: {self.raca}
        Idade: {self.idade}
        Altura: {self.altura}
        Peso: {self.peso}
        Genero: {self.genero}
        Classe: {self.classe}
        '''
