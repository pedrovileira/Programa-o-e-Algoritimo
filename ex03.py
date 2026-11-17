# Descrição: Identifica o sexo conforme a letra digitada.#
# Parâmetros de entrada: Uma letra (F ou M).#
# Valores de saída: Feminino, Masculino ou Sexo Inválido.#
# Autor: Pedro Silva#
letra = input("Digite F ou M: ").strip().upper()

if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")
