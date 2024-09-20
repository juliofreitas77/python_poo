class Restaurante:
    def __init__(self, nome, categoria):  
        self.nome = nome
        self.categoria = categoria
        self.ativo= False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'


restaurante_praca = Restaurante('Praca', 'Gourmet')

# dir = Exibir atributos do objetos
#print(dir(restaurante_praca))

# vars = Exibir somento os atributos criados
#print(vars(restaurante_praca)
print(restaurante_praca)