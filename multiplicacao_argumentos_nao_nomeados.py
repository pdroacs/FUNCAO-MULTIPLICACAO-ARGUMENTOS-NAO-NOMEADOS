def multiplicacao(*args):
    total = 1
    for num in args:
        total *= num
    return total


resultado = multiplicacao(1, 2, 3, 4, 5, 6)
print(f'O resultado da multiplicação é: {resultado}')
