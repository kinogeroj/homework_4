# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Пример:
# - В file1.txt :
# 2*x**2 + 4*x + 5
# - В file2.txt:
# 4*x**2 + 1*x + 4
# - Результирующий файл:
# 6*x**2 + 5*x + 9

import os
import sympy
from createpolynom import createpoly

os.system('cls')

print('Сгенерируем два многочлена, запишем их в файлы и произведем их суммирование!')

print()

k = input('Введите коэффициенты многочленов через пробел: ').split()

k = [int(i) for i in k]

with open('file1.txt', 'w') as file:
    
    file.write(createpoly(k[0]))

with open('file2.txt', 'w') as file:
    
    file.write(createpoly(k[1]))

x = sympy.Symbol('x')

with open('file1.txt', 'r') as file:

    a = file.read()

with open('file2.txt', 'r') as file:
    
    b = file.read()

c = str(sympy.simplify(sympy.simplify(a) + sympy.simplify(b)))

with open('result.txt', 'w') as file:
    file.write(c)

print()

print(f'При сложении многочленов "{a}" и "{b}" получился такой многочлен: "{c}", он записан в файл result.txt.')