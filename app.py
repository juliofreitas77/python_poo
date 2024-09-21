from modelos.retaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Julio', 10)
restaurante_praca.receber_avaliacao('Jose', 4)
restaurante_praca.receber_avaliacao('Ana', 5)
#restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
#restaurante_japones = Restaurante('Japa', 'Japonesa')

#restaurante_japones.alternar_estado()


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()