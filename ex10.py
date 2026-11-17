# Descrição: Mostra os números ímpares de 0 até 20.
# Parâmetros de entrada: Não há. #
# Valores de saída: Todos os números ímpares da faixa. #
# Autor: Pedro Silva. #

for numero in range(0, 21):
    if numero % 2 != 0:
        print(numero)
