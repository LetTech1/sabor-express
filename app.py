from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
restaurante_japones = Restaurante('Japa', 'Japones')

restaurante_mexicano.alternar_estado()

restaurante_japones.receber_avaliacao('Let', 2)
restaurante_japones.receber_avaliacao('Gui', 3)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()