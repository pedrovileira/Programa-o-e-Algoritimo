################################################################
# Descrição: Exibe a tabuada de um número informado.            #
# Parâmetros de entrada: Um número informado pelo usuário.     #
# Valores de saída: Resultados da multiplicação de 1 a 10.     #
# Autor: Pedro Vileira                                         #
################################################################

numero = int(input("Digite um número para ver sua tabuada: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
