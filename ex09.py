# Descrição: Soma os números pares existentes de 1 até 500. #
# Parâmetros de entrada: Não há. #
# Valores de saída: Soma de todos os números pares da faixa. #
# Autor: Pedro Silva. #

soma = 0

for numero in range(1, 501):
    if numero % 2 == 0:
        soma += numero

print("A soma dos números pares de 1 até 500 é:", soma)
