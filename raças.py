from abc import ABCMeta, abstractmethod


class Mascara:
    __metaclass__ = ABCMeta

    def __init__(self, personagem):
        self._atributos = personagem._atributos
        personagem.poder_de_raca = self.define_poder_de_raca()

    @abstractmethod
    def modifica_atributos(self):
        pass

    @abstractmethod
    def define_poder_de_raca(self):
        pass


class DefineRaca:
    def __init__(self, raca):

        racas = [Humano, Lohikaarme, Gigante, Anão, Felnari, Khevari]

        for raca_definida in racas:
            nome_da_raca = raca_definida.__name__

            if raca == nome_da_raca:
                self.raca_definida = raca_definida

    def define(self, objeto):
        try:
            self.raca_definida(objeto).modifica_atributos()
        except:
            raise ValueError('Raça Inválida')


class Humano(Mascara):

    def modifica_atributos(self):
        self._atributos['Carisma'] += 1
        self._atributos['Inteligência'] += 1

    def define_poder_de_raca(self):
        return '''Compaixão de Narcissus: Cura feridas letais de aliados. Só
pode ser usado uma vez a cada 5 dias'''


class Lohikaarme(Mascara):

    def modifica_atributos(self):
        self._atributos['Resistência'] += 1
        self._atributos['Inteligência'] += 2

    def define_poder_de_raca(self):
        return '''Maldição de Athrelion: Intimida qualquer inimigo. Só pode ser 
        usado uma vez por dia.'''


class Gigante(Mascara):

    def modifica_atributos(self):
        self._atributos['Força'] += 2
        self._atributos['Resistência'] += 1

    def define_poder_de_raca(self):
        return '''Consciência das eras: Consegue sentir as vibrações do
solo e localizar inimigos através delas.'''


class Anão(Mascara):

    def modifica_atributos(self):
        self._atributos['Sabedoria'] += 2
        self._atributos['Resistência'] += 1

    def define_poder_de_raca(self):
        return '''Beber até cair: Quase imune a qualquer bebida ou droga
produzida por alguém que não seja um anão.'''


class Felnari(Mascara):

    def modifica_atributos(self):
        self._atributos['Destreza'] += 2
        self._atributos['Sabedoria'] += 1

    def define_poder_de_raca(self):
        return '''Tempestade de Pharo: Usando a força do vento dá um
avanço que tem um alcance de até 20 metros, aparecendo
atrás de um inimigo. Só pode ser usada a cada 3 turnos.'''


class Khevari(Mascara):

    def modifica_atributos(self):
        self._atributos['Sabedoria'] += 1
        self._atributos['Fé'] += 3

    def define_poder_de_raca(self):
        return '''Filho do Inverno: Cria uma crosta gélida que reduz todo
dano direcionado pela metade, por dois turnos. Enquanto
nesse modo, o jogador não pode infringir dano a inimigos.'''
