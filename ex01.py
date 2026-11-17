################################################################
# Descrição: Solicita dois números e mostra qual deles é maior. #
# Parâmetros de entrada: Dois números informados pelo usuário. #
# Valores de saída: O maior número ou uma mensagem de igualdade.#
# Autor: Pedro Vileira                                        #
################################################################

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)
else:
    print("Os dois números são iguais.")
