# Descrição: Apresenta os quadrados dos inteiros de 15 a 200. #
# Parâmetros de entrada: Não há. #
# Valores de saída: Quadrado de cada número entre 15 e 200. #
# Autor: Pedro Silva. #

for numero in range(15, 201):
    quadrado = numero ** 2
    print(numero, "ao quadrado é", quadrado)
