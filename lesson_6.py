#If else exercise
# dog_age = int(input('Dog: '))

# if dog_age <= 2:
#     human_age = dog_age * 10.5
# else:
#     human_age = 2 * 10.5 + (dog_age - 2) * 4

# print(human_age)

#---------------------------------------------------------------------------

#If else exercise
# year = int(input('year: '))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('leap year')
# else:
#     print('not leap year')

#---------------------------------------------------------------------------

#Ex1
# import random

# count = 0
# n = int(input('N: '))

# for i in range(n):
#     person_number = random.randint(1, 10)
#     credit = int(input(f'Random: {person_number} || Enter the credid[{i + 1}]: '))
#     if credit > 0 and person_number % 2 == 0:
#         count += 1

# print(count)

#---------------------------------------------------------------------------
#Ex2
# summ = 0
# months = int(input('Enter the count of months: '))

# for i in range(months):
#     salary = float(input(f'Enter your {i + 1} salary: '))
#     summ += salary

# avg = summ / months

# print(round(avg))

#---------------------------------------------------------------------------
#Ex3
# import math
# print(math.factorial(5))


# number = int(input('Numbe: ')) # 5
# summ = 1
# for i in range(1, number + 1):
#     summ *= i
# print(summ)

#---------------------------------------------------------------------------
#Ex4
# count_3 = 0
# count_4 = 0
# count_5 = 0

# students = int(input('How many students do you have? '))#25

# for i in range(students):
#     mark = int(input(f'Enter the mark[{i + 1}]: '))
#     if mark == 3:
#         count_3 += 1
#     elif mark == 4:
#         count_4 += 1
#     elif mark == 5:
#         count_5 += 1
#     else:
#         print('Chka tenc gnahatakan')

# if count_5 >= count_4 and count_5 >= count_3:
#     print('Gerazancik dasarana')
# elif count_4 >= count_5 and count_4 >= count_3:
#     print('Lav dasarana')
# else:
#     print('Shat vat dasarana')

#---------------------------------------------------------------------------
#Ex5
# a = int(input('a: '))
# b = int(input('b: '))
# count = 0
# summ = 0

# for digit in range(a, b + 1):
#     if digit % 3 == 0:
#         count += 1
#         summ += digit

# average = summ / count
# print(average)

#---------------------------------------------------------------------------
#Ex6
# for digit in range(10, 100):
#     first = digit // 10
#     second = digit % 10
#     if first * second == digit / 3:
#         print(digit)

#---------------------------------------------------------------------------
#Ex7
# count_c = int(input('Cards: '))
# summ = count_c * (count_c + 1) / 2

# for _ in range(1, count_c):
#     current_c = int(input('What left: '))
#     summ -= current_c

# print(summ)

#---------------------------------------------------------------------------

#Ex1
# pashar = 100

# for i in range(25): #[0-24] = 25
#     pashar = pashar - 4
#     print(f'amis {i + 1}-um mnacela utelu {pashar}')


#Ex2
# a = int(input('a; ')) 
# b = int(input('b; ')) 
# c = int(input('c; ')) 
# count = 0 
# summ = 0 
# for digit in range(a, b + 1): 
#     if digit % c == 0:
#         count += 1
#         summ += digit
# print(summ / count)


# a = int(input('a: '))
# b = int(input('b: '))
# # x = int(input('X: '))
# for x in range(a, b + 1):
#     y = x ** 3 + 2 * x ** 2 - 4 * x + 1
#     print(f'{x} -> {y}')