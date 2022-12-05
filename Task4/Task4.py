# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.(записать в строку)
# Пример:
# - k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# - k=3 => 2*x^3 + 4*x^2 + 4*x + 5

import os
import random

os.system('cls')

print('Создадим многочлен степени k и запишем его в файл, коэффициенты будут сгенерированы случайным образом автоматически.')

print()

k = int(input('Введите степень многочлена (k): '))

def createpoly(k, var_string = 'x') -> str:

    """Фунцкия принимает на вход степень многочлена, на выходе получаем строку с многочленом."""

    coeflist = []

    for i in range(0, k + 1):
        n = random.randint(-10, 10)
        coeflist.append(n)

    resstr = ''
    
    first_pow = len(coeflist) - 1
    
    for i, coef in enumerate(coeflist):
        power = first_pow - i

        if coef:
            
            if coef < 0:
                sign, coef = (' - ' if resstr else '-'), -coef

            elif coef > 0:
                sign = (' + ' if resstr else '')

            str_coef = '' if coef == 1 and power != 0 else str(coef)

            if power == 0:
                str_power = ''

            elif power == 1:
                str_power = var_string

            else:
                str_power = var_string + '^' + str(power)

            resstr += sign + str_coef + str_power

    return resstr

with open('file1.txt', 'w') as file:
    file.write(createpoly(k))

print()

print('Задача выполнена, ниже представлено содержимое файла file1.txt:')

with open('file1.txt', 'r') as file:
    Result = file.read()

print(Result)