################################################################
# Descrição: Mostra uma saudação conforme o turno de estudo.   #
# Parâmetros de entrada: M, V ou N, informados pelo usuário.   #
# Valores de saída: Saudação correspondente ou Valor Inválido. #
# Autor: Pedro Vileira                                        #
################################################################

turno = input("Digite M - Matutino, V - Vespertino ou N - Noturno: ")
turno = turno.strip().upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
