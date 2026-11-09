# n = int(input("N: ")) # 10

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             print('^', end=' ')
#         elif j == n + 1 - i:
#             print('^', end=' ')
#         else:
#             print(' ', end=' ')
#     print()




# n = int(input("N: ")) # 6
# count = 0
# for _ in range(n):
#     number = int(input("Number: "))
#     for divisor in range(2, int(number ** 0.5) + 1):
#         if number % divisor == 0:
#             break
#     else:
#         count += 1
# print(count)




# n = int(input("N: ")) # 6
# summ = 0 # 1

# for i in range(1, n + 1):
#     summ_2 = 1
#     for j in range(1, i + 1):
#         summ_2 *= j
#     summ += summ_2
# print(summ)



# n = int(input("N: ")) # 5
# max_summ = 0 # 17
# max_number = 0
# for i in range(n): # 1
#     number = int(input("Number: ")) #  0
#     number_2 = number
#     summ = 0 #  + 4 + 7 + 6
#     while number > 0:
#         summ += number % 10
#         number //= 10
#     if summ > max_summ:
#         max_summ = summ
#         max_number = number_2

# print(max_summ, max_number)




# n = int(input("N: "))

# for i in range(1, n + 1):
#     for j in range(1, n + i):
#         if j > n - i:
#             print('#', end=' ')
#         else:
#             print(' ', end=' ')
#     print()




# n = int(input("N: "))
# k = 1
# for i in range(1, n + 1):
#     for j in range(1, n + i):
#         if j > n - i:
#             if (i + j) % 2 == 1:
#                 print(' ', end='\t')
#             else: 
#                 print(k, end='\t')
#                 k += 2
#         else:
#             print(' ', end='\t')
#     print()



# n = int(input("N: "))
# for i in range(1, n + 1): # 1
#     for j in range(1, i + 1):
#         print(n + 1 - j, end=' ')

#     for k in range(2 * n - 2 * i):
#         print('.', end=' ')

#     for t in range(1, i + 1):
#             print(n - i + t, end=' ')

#     print()




# import random
# import readchar
# # import msvcrt

# n = int(input("N: "))
# hp = 3
# scores = 0
# monkey_row = random.randint(1, n)
# monkey_column = random.randint(1, n)
# monkey_emoji = '🐵'

# bomb_row = random.randint(1, n)
# bomb_column = random.randint(1, n)
# bomb_emoji = '💣'

# banana_row = random.randint(1, n)
# banana_column = random.randint(1, n)
# banana_emoji = '🍌'

# gift_row = random.randint(1, n)
# gift_column = random.randint(1, n)
# gift_emoji = '🎁'


# while True:
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if i == monkey_row and j == monkey_column:
#                 print(monkey_emoji, end='\t')
#             elif i == banana_row and j == banana_column:
#                 print(banana_emoji, end='\t')
#             elif i == bomb_row and j == bomb_column and scores >= 3:
#                 print(bomb_emoji, end='\t')
#             elif i == gift_row and j == gift_column and hp == 1:
#                 print(gift_emoji, end='\t')
#             else:
#                 print('*', end='\t')
#         print()
#     print(hp * '❤️ ')
#     print(scores * '⭐')
    

#     ##Windows
#     # monkey_step == msvcrt.getwche()
#     ##Macos
#     monkey_step = readchar.readkey()
#     print('\n')
#     monkey_step == monkey_step.lower()
#     if monkey_step == 'q':
#         break
#     elif monkey_step == 'w':
#         monkey_row -= 1

#     if monkey_row == banana_row and monkey_column == banana_column:
#         scores += 1
#         banana_row = random.randint(1, n)
#         banana_column = random.randint(1, n)
#     elif monkey_row == gift_row and monkey_column == gift_column:
#         hp += 1