from main import Personagem
persona = Personagem('Jorge', 41, 1.90, '71 kg', 'Masculino', 'Cavaleiro Andante')
print(persona)
print(persona.atributos)
print('****************')
persona.sobe_um_level('Força')
persona.sobe_um_level('Força')
persona.sobe_um_level('Força')
print(persona.atributos)