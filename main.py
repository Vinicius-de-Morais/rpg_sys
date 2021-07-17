
class Personagem():

    atributos = {
        "cavaleiro andante":{
            'força': 3,
            'destreza': 2,
            'inteligencia': 0,
            'fe': 0,
            'sabedoria': 0,
            'resistencia': 2,
            'carisma': 2,
            'sorte': 0
        },
        "cavaleiro":{
            'força': 2,
            'destreza': 1,
            'inteligencia': 1,
            'fe': 0,
            'sabedoria': 0,
            'resistencia': 3,
            'carisma': 3,
            'sorte': 0
        },
        "alquimista":{
            'força': 0,
            'destreza': 1,
            'inteligencia': 3,
            'fe': 0,
            'sabedoria': 2,
            'resistencia': 1,
            'carisma': 3,
            'sorte': 0
        },
        "bardo":{
            'força': 0,
            'destreza': 0,
            'inteligencia': 1,
            'fe': 0,
            'sabedoria': 1,
            'resistencia': 0,
            'carisma': 5,
            'sorte': 3
        },
        "nobre":{
            'força': 1,
            'destreza': 1,
            'inteligencia': 1,
            'fe': 1,
            'sabedoria': 1,
            'resistencia': 1,
            'carisma': 1,
            'sorte': 1
        },
        "oraculo":{
            'força': 0,
            'destreza': 0,
            'inteligencia': 1,
            'fe': 5,
            'sabedoria': 3,
            'resistencia': 1,
            'carisma': 0,
            'sorte': 0
        }
    }

    def __init__(self, nome, idade, altura, peso, genero, classe):
        self.nome      = nome.title()
        self.raca      = "Desconhecida"
        self.idade     = idade
        self.altura    = altura
        self.peso      = peso
        self.genero    = genero
        self.classe    = classe
        self.atributos = Personagem.atributos[classe.lower()]

    @staticmethod
    def _consultar_classes():
        return "\n".join(Personagem.atributos.keys())

    def upar_um_level(self, atributo):
        self.atributos[atributo] += 1

    def mostrar_perfil(self):
        perfil = f''' 
        Nome: {self.nome}
        Raça: {self.raca}
        Idade: {self.idade}
        Altura: {self.altura}
        Peso: {self.peso}
        Genero: {self.genero}
        Classe: {self.classe}
        '''
        return perfil


if __name__ == "__main__":
    persona = Personagem('Jorge', 41, 1.90, '71 kg', 'Masculino', 'Oraculo')
    print( persona.mostrar_perfil() )
    print('='*50)
    
    print( persona.atributos )
    #  upar 1 level de força e 3 de inteligencia
    persona.upar_um_level('força')
    for i in range(3):
        persona.upar_um_level('inteligencia')
    # (Claro que o UP não está sendo acumulativo já que estamos instanciando a classe toda vez)
    print( persona.atributos )