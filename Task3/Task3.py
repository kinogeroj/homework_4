# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os
import random

os.system('cls')

print('Сгенерируем случайным образом ряд чисел, некоторые из которых будут повторяться.')

print()

randomlist = []

for i in range(0,20):
    
    n = random.randint(1,9)
    
    randomlist.append(n)

print(f'Получился вот такой ряд чисел: {randomlist}.')

def deleteduplicate(inputlist):

    """Функция принимает на вход список и удаляет из него повторяющиеся элементы."""

    outputlist = []

    for i in inputlist:

        if i not in outputlist:

            outputlist.append(i) 

    return outputlist

print()

print(f'Ряд чисел с удаленными повторяющимися элементами: {deleteduplicate(randomlist)}.')