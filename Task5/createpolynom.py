# Special function to create polynom by Dmitrii Mironov

import random

def createpoly(k, var_string = 'x') -> str:

    """Фунцкия принимает на вход степень многочлена, на выходе получаем строку с многочленом."""

    coeflist = []

    for i in range(0, k + 1):
        
        n = random.randint(0, 10)
        
        coeflist.append(n)

    resstr = ''
    
    first_pow = len(coeflist) - 1
    
    for i, coef in enumerate(coeflist):
        
        power = first_pow - i

        if coef:
            
            if coef < 0:

                sign, coef = (' - ' if resstr else ' - '), -coef

            elif coef > 0:

                sign = (' + ' if resstr else '')

            str_coef = '1' if coef == 1 and power != 0 else str(coef)

            if power == 0:

                str_power = ''

            elif power == 1:

                str_power = var_string

            else:

                str_power = var_string + '**' + str(power)

            resstr += sign + str_coef + '*' + str_power

    return resstr[:-1]