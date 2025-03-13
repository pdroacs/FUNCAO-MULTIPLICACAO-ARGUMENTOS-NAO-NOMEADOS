# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicacao(*args):
    total = 1
    for num in args:
        total *= num  # total = total * num -> mesma coisa
    return total


resultado = multiplicacao(1, 2, 3, 4, 5, 6)
print(f'O resultado da multiplicação é: {resultado}')
