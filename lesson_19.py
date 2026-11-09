#Ex. 1
# def say_hello():
#     print('Say hello')

# say_hello()

#Ex. 2
# def say_hello(name):
#     print(name)

# name = input('Name: ')
# say_hello(name)

#Ex. 3
# def add(a, b):
#     return a + b

# x = int(input('X: '))
# y = int(input('Y: '))
# gumar = add(x, y)
# print(gumar)


#Ex. 4
# def even_odd(n):
#     return n % 2 == 0

# print(even_odd(7))


#Ex. 5
# def check_number(n):
#     if n < 0:
#         print('Negative')
#     elif n > 0:
#         print('Positive')
#     else:
#         print('Zero')


# x = int(input('Number: '))
# check_number(x)



#Ex. 6
# def maximum(a, b, c):
#     if a >= b and a >= c:
#         print(a)
#     elif b >= a and b >= c:
#         print(b)
#     else:
#         print(c)

# maximum(7, 7, 4)


#Ex. 7
# def count_digits(n):
#     count = 0
#     while n != 0:
#         n //= 10
#         count += 1

#     return count

# print(count_digits(1124))

#Ex. 8
# def sum_n(n):
#     #version 1
#     # return n * (n + 1) / 2

#     #version 2
#     # summ = 0
#     # for i in range(1, n + 1):
#     #     summ += i
#     # return summ

# print(sum_n(5))

#Ex. 9
# def count_even(n):
#     return len([i for i in n if i % 2 == 0])

# print(count_even([1, 5, 3, 4, 2, 1, 6, 7 ,5, 3]))

#Ex. 10
# def find_max(n):
#     n.sort()
#     return n[-1]

# print(find_max([4, 5, 2, 3, 1]))


#Ex. 11
# def average(numbers):
#     summ = 0
#     for number in numbers:
#         summ += number

#     print(summ / len(numbers))

# average([10, 20, 30, 40])


#Ex. 12
# import time
# def is_prime(n):
#     start = time.time()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             end = time.time()
#             print(end - start)
#             return False
#     end = time.time()
#     print(end - start)
#     return True

# print(is_prime(1387654377541111))