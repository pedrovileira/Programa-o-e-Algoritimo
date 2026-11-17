# Descrição: Verifica se um valor é positivo ou negativo.      #
# Parâmetros de entrada: Um número informado pelo usuário.     #
# Valores de saída: Mensagem indicando o sinal do número.     #
# Autor: Pedro Silva                                        #

valor = float(input("Digite um valor: "))

if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")
