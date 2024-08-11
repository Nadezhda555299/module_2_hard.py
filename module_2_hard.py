from random import randint

def numbers(n):
    unique = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                unique += str(i) + str(j)
    return f'{n} - {unique}\nКак жаль, что они поняли это поздно! '

# n = 3 - 20
n = int(input("Введите число: "))

the_ancient_cipher = numbers(n)
print(the_ancient_cipher)