# def get_fizzbuzz_sum(num1, num2):
#     sum = 0
#     for i in range(num1, (num2 + 1)):
#         if i % 3 == 0 and i % 5 == 0:
#             sum += i
#     return sum

#проверка:
# print(get_fizzbuzz_sum(1, 30))

#ИЛИ КОРОЧЕ:

def get_fizzbuzz_sum(num1, num2):
    a = [i for i in range(num1, (num2 + 1)) if i % 3 == 0 and i % 5 == 0]
    return sum(a)
#проверка:
print(get_fizzbuzz_sum(1000, 20000))