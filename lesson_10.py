# n = int(input("N: "))

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j > n + 1 - i:
#             print('.', end=' ')
#         else:
#             print('#', end=' ')
#     print()



# k = int(input("K: "))
# for i in range(k):
#     number = int(input("N: "))
#     count = 0
#     for j in range(1, number + 1):
#         if number % j == 0:
#             count += 1
#     print(f'{number} -> {count} divisors')



# n = int(input("Range: "))
# for digit in range(2, n + 1):
#     summ = 0
#     for divisor in range(1, digit):
#         if digit % divisor == 0:
#             summ += divisor
#     if summ == digit:
#         print(digit)



# a = int(input("a: "))
# b = int(input("b: "))
# if a < b:
#     for i in range(1, a + 1):
#         if a % i == 0 and b % i == 0:
#             print(i, end=' ')
# else:
#     for i in range(1, b + 1):
#         if a % i == 0 and b % i == 0:
#             print(i, end=' ')



# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == 1 or i == n:
#             print('*', end='')
#         elif j == 1 or j == n:
#             print('*', end='')
#         elif i == j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# N = int(input("Enter N: ")) # 5
# for a in range(1, N): #
#     for b in range(1, N): # 
#         if a + b == N:
#             print(f"{a} + {b} = {N}")



# N = int(input("N: ")) # 5
# for a in range(1, N): # 1, 2, 3, 4
#     b = N - a # 1
#     print(a, "+", b, "=", N)



# n = int(input("N: "))

# for i in range(n):
#     for j in range(n):
#         print(f'{2 * j + i:<3}', end=' ')
#     print()


# n = int(input("N: "))

# for i in range(1, n + 1):
#     for j in range(0, i):
#         print(i, end=' ')
    # print()


# a = int(input("a: "))
# b = int(input("b: "))
# for i in range(1, a + 1):
#     for j in range(1, b + 1):
#         if j == 1 or j == b:
#             print('|', end=' ')
#         elif i == 1 or i == a:
#             print('-', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

