# n = int(input('N: '))
# n = str(n)
# print(len(n))


# n = int(input('N: ')) # 0
# count = 0 # 1 + 1 + 1 + 1
# summ = 0 # 5 + 6 + 3 + 4
# while n > 0:
#     summ += n % 10
#     n //= 10
#     count += 1

# print(count)
# print(summ)


# n = int(input("Enter the number: ")) #103
# lav = 0
# vat = 0
# while n != 0:
#     while n > 100 or n < -100 or n == 0:
#         print("Invalid Value: ")
#         n = int(input("Enter the number: "))
#     if n > 0:
#         lav += 1
#     else:
#         vat += 1
#     n = int(input("Enter the number: "))
    


# hours = 8
# current = 1
# tasks = 0
# shop_status = False

# while current <= hours:
#     task = int(input(f"How many tasks did you solve for {current}? "))
#     tasks += task
#     wife_call = input("You wife is calling, answer(y/n)? ").lower()
#     if wife_call == 'y':
#         shop_status = True
#     current += 1

# if shop_status:
#     print('Pti mtnes xanut, chmoranas!!!')
#     print(tasks)
# else:
#     print(tasks)


# money = int(input("Money$: ")) # 100
# percent = float(input("Percent%: ")) # 9
# desire = int(input("Desire: ")) # 1000
# year = 0

# while money < desire:
#     money *= (1 + percent / 100)
#     year += 1

# print(year)




# user_number = int(input("Enter the number between (1-100): "))
# start = 1
# end = 100
# steps = 0
# while True:
#     guess_number = (start + end) // 2
#     user_status = input(f"Qo tivy {guess_number}-in havasar e?, mets e?, poqr e?(h,m,p) ").lower()
#     steps += 1
#     if user_status == 'h':
#         print(f'Gta qo tivy {steps} qaylov')
#         break
#     elif user_status == 'm':
#         start = guess_number + 1
#     else:
#         end = guess_number - 1


# for i in range(2):
#     for j in 'ab':
#         print(i, j, end=' | ')
#     print()

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end='\t')
#     print()

# for i in range(1, 9):
#     for j in range(1, 9):
#         if i == 2 and j == 4:
#             print('Q', end=' ')
#         elif i == 6 and j == 2:
#             print('N', end=' ')
#         else:
#             print('*', end=' ')
#     print()


# n = int(input("N: ")) # 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print("#", end=' ')
#     print()