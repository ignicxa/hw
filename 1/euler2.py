#!/usr/bin/python3

from functools import reduce

# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Какова разность между суммой квадратов и квадратом суммы?
# Сумма квадратов первых десяти натуральных чисел
# 1**2 + 2**2 + ... + 10**2 = 385
# Квадрат суммы первых десяти натуральных чисел
# (1 + 2 + ... + 10)**2 = 55**2 = 3025
# Следовательно, разность между суммой квадратов и квадратом суммы первых
# десяти натуральных чисел составляет 3025 - 385 = 2640.
# Найдите разность между суммой квадратов и квадратом суммы первых 
# ста натуральных чисел.
# Решите задачу двумя способами: с помощью map и lambda 
# и с помощью генератора списка. 
def diff():
    map_result = sum(range(101))**2 - sum(list(map(lambda i: i**2, range(101))))
    generator_result = sum(range(101))**2 - sum(i*i for i in range(101))
    return map_result if map_result == generator_result else ''


# B. Найдите наибольшее произведение пяти последовательных цифр в 
# 1000-значном числе.
"""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

def max_five():
    num = list('7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450')
    num, counter, max = list(map(int, num)), 0, 0
    while counter != 996:
        temp = num[counter:counter+5]
        if 0 not in temp:
            if sum(temp) > max:
                max, result = sum(temp), 1
                for i in num[counter:counter+5]:
                    result *= i
        counter += 1
    return result


# C. Какова сумма цифр числа 2**1000
# 2**15 = 32768, сумма цифр 3 + 2 + 7 + 6 + 8 = 26.
# Какова сумма цифр числа 2**1000?
def summm():
    return sum(list(map(int, str(2**1000))))


# D. Найдите сумму цифр в числе 100!
# n! означает n * (n-1) * ... * 3 * 2 * 1
# Найдите сумму цифр в числе 100!.
def factorial():
    temp = 1
    for i in range(1, 101):
        temp *= i
    return sum(list(map(int, str(temp))))


# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает фунции выше с тестовыми параметрами.
def main():
    print('A. Разность между суммой квадратов и квадратом суммы?')
    test(diff(), 25164150)

    print()
    print('B. Наибольшее произведение пяти последовательных цифр')
    test(max_five(), 40824)

    print()
    print('C. Сумма цифр числа 2**1000')
    test(summm(), 1366)

    print()
    print('D. Сумма цифр в числе 100!')
    test(factorial(), 648)

if __name__ == '__main__':
    main()