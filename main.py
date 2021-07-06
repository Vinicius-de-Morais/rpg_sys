class Personagem:
    def __init__(self, nome, idade, altura, peso, genero):
        self.nome = nome.title()
        self.raca = ""
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.classe = ""
        self.vida = ""

    def set_classe(self, classe):
        
        return self.classe
    
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

persona = Personagem('Jorge', 41, 1.90, '71 kg', 'Masculino')

print(persona)