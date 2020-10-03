from functools import lru_cache

@lru_cache(maxsize = 10000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return (fibonacci(n-1) + fibonacci(n-2))
    
n = 1
even_numbers = []
while fibonacci(n) < 10000000:
    if fibonacci(n) % 2 == 0:
        even_numbers.append(fibonacci(n))
        sum_even_numbers = sum(even_numbers)
    n += 1
print(f'Количество элементов в последовательности: {n}')
print(f'Сумма всех четных элементов: {sum_even_numbers}')
print(f'Четные элементы последовательности: {even_numbers}')
print(f'{fibonacci(n-2)}  - предпоследнее число последовательности')
