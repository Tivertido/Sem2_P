# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def square(N):
    for k in range(int(N.bit_length())):
        result = 2 ** k
        if result <= N:
            print(result)

N = int(input("Введите число N: "))
print("Целые степени двойки не превосходящие N:")
square(N)