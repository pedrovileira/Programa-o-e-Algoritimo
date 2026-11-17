# Descrição: Calcula a média de duas notas e informa o resultado. #
# Parâmetros de entrada: Duas notas parciais do aluno. #
# Valores de saída: Média e situação final do aluno. #
# Autor: Pedro Silva. #

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Média:", media)

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
