from main import Oraculo, Nobre, Bardo, Alquimista, Cavaleiro, CavaleiroAndante, Personagem

persona = Nobre('Jorge', 41, 1.90, '71 kg', 'Masculino')
print(persona)
persona.sobe_um_level('força')
persona.sobe_um_level('força')
persona.sobe_um_level('força')
print(persona.atributos)
