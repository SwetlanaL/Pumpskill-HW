# def plural_form(num, *args):
#     first_digit = num % 10
#     second_digit = int(num / 10) % 10
#     if second_digit != 1:
#         if first_digit == 1:
#             return str(num) + ' ' + args[0]
#         elif first_digit >= 2 and first_digit <= 4:
#             return str(num)+ ' ' + args[1]
#     return str(num)+ ' ' + args[2]
            
# print(plural_form(1, 'яблоко', 'яблока', 'яблок'))
# print(plural_form(2, 'яблоко', 'яблока', 'яблок')) 
# print(plural_form(11, 'студент', 'студента', 'студентов')) 
# print(plural_form(15, 'студент', 'студента', 'студентов')) 
# print(plural_form(3, 'студент', 'студента', 'студентов')) 

#OR:

def plural_form(value, form1, form2, form3):
    #abs() - возвращает положительное число
    n = abs(value) % 100
    n1 = n % 10
    result_form = form3
    if 10 < n < 20 or n == 0:
        result_form = form3
    elif  1 < n1 < 5:
        result_form = form2
    elif n1 == 1:
        result_form = form1
    return f'{value} {result_form}'

print(plural_form(0, 'яблоко', 'яблока', 'яблок'))
print(plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(plural_form(2, 'яблоко', 'яблока', 'яблок')) 
print(plural_form(11, 'студент', 'студента', 'студентов')) 
print(plural_form(15, 'студент', 'студента', 'студентов')) 
print(plural_form(3, 'студент', 'студента', 'студентов')) 