# from functools import lru_cache

# @lru_cache(maxsize = 10000)
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n > 2:
#         return (fibonacci(n-1) + fibonacci(n-2))
    
# n = 1
# even_numbers = []
# while fibonacci(n) < 10000000:
#     if fibonacci(n) % 2 == 0:
#         even_numbers.append(fibonacci(n))
#         sum_even_numbers = sum(even_numbers)
#     n += 1
# print(f'Количество элементов в последовательности: {n}')
# print(f'Сумма всех четных элементов: {sum_even_numbers}')
# print(f'Четные элементы последовательности: {even_numbers}')
# print(f'{fibonacci(n-2)}  - предпоследнее число последовательности')

#OR (через создание списка из чисел фибоначчи):
# threshold - порог
def fibonacci(zero_step, first_step, threshold):
    next_step = 0
    list_of_numbers = [zero_step, first_step]
    while next_step < threshold:
        next_step = zero_step + first_step
        zero_step = first_step
        first_step = next_step
        if next_step < threshold:
            list_of_numbers.append(next_step)
    return list_of_numbers
fibonacci_list = fibonacci(1, 1, 10000000)

even_list = []
for number in fibonacci_list:
    if number % 2 == 0:
        even_list.append(number)

print(f'Количество элементов в последовательности: {len(fibonacci_list)}')
print(f'Сумма всех четных элементов: {sum(even_list)}')
print(f'Четные элементы последовательности: {even_list}')
print(f'{fibonacci_list[- 2]}  - предпоследнее число последовательности')

