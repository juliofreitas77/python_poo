# 1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
# Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro_c3 = Carro('C3','Branco', 2015)    

 #Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. 
 # Instancie um restaurante e atribua valores aos seus atributos.     
class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):  
        self.nome = nome
        self.categoria = categoria
        self.ativo= False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print (f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praca', 'Gourmet')
estaurante_praca = Restaurante('Pizzaria Express', 'Italiana')
Restaurante.listar_restaurantes()


#Crie uma classe chamada Cliente e pense em 4 atributos. 
#Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')