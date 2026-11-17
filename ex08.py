# Descrição: Calcula a soma dos cem primeiros números naturais.#
# Parâmetros de entrada: Não há.                                #
# Valores de saída: Soma dos números de 1 até 100.              #
# Autor: Pedro Silva. #
soma = 0

for numero in range(1, 101):
    soma += numero

print("A soma dos cem primeiros números naturais é:", soma)
