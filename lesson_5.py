# import random
# import time
# name = input('Prove your name: ').capitalize()
# user_status = input(f'{name} are you ready? (yes/no)').lower()
# if user_status == 'yes':
#     time.sleep(0.5)
#     print(3)
#     time.sleep(0.5)
#     print(2)
#     time.sleep(0.5)
#     print(1)
#     time.sleep(0.5)
#     print('FINISH HIM!!!')

#     user_score = 0
#     pc_score = 0
#     pc_number = random.randint(1, 5)
#     user_number = int(input('Guess the number? (1-5): '))
#     if user_number == pc_number: #es 1 pc 0
#         user_score += 1
#         print(f'{name} WIN this round!!!')
#         print(f'pc -> {pc_number} | {name} -> {user_number} SCORES: {user_score}/{pc_score}')
#         pc_number = random.randint(1, 5)
#         user_number = int(input('Guess the number? (1-5): '))
#         if user_number == pc_number: # 2 0
#             user_score += 1
#             print(f'{name} WIN this round!!!')
#             print(f'pc -> {pc_number} | {name} -> {user_number} SCORES: {user_score}/{pc_score}')
#             print(f'END GAME::: {name} WIN!!!')
#         else: # 1 1
#             pc_score += 1
#             print(f'PC WIN this round!!!')
#             print(f'pc -> {pc_number} | {name} -> {user_number} SCORES: {user_score}/{pc_score}')
#             user_number = int(input('Guess the number? (1-5): '))
#             print(f'END GAME::: DRAW!!!')
#     else: # 0 1
#         pc_score += 1
#         print(f'PC WIN this round!!!')
#         print(f'pc -> {pc_number} | {name} -> {user_number} SCORES: {user_score}/{pc_score}')
#         pc_number = random.randint(1, 5)
#         user_number = int(input('Guess the number? (1-5): '))
#         if user_number == pc_number: # 1 1
#             user_score += 1
#             print(f'{name} WIN this round!!!')
#             print(f'pc -> {pc_number} | {name} -> {user_number} SCORES: {user_score}/{pc_score}')
#             print(f'END GAME ::: {name} DRAW!!!')
#         else: # 0 2
#             pc_score += 1
#             print(f'PC WIN this round!!!')
#             print(f'pc -> {pc_number} | {name} -> {user_number} SCORES: {user_score}/{pc_score}')
#             print(f'END GAME::: PC WIN!!!')
# else:
#     print('de kpi gorcerit')



# import time

# print('3')
# time.sleep(1)
# print('2')
# time.sleep(1)
# print('1')
# time.sleep(1)
# print("LET'S GO!!!!!")

# player = int(input('Number: '))
# import random
# comp = random.randint(0, 5)
# comp_point = 0
# player_point = 0
# if player == comp:
#     print('es haxteci')
#     player_point += 1
#     print (f'comp {comp_point}:{player_point} player')
#     int(input('Number: '))
#     comp = random.randint(0, 5)
#     if player == comp:
#         print('es haxteci')
#         player_point += 1
#         print (f'comp {comp_point}:{player_point} player')
#     elif player != comp:
#         print('compy haxxtec')
#         comp_point += 1
#         print(f'comp {comp_point}:{player_point} player')
#         int(input('Number: '))
#         comp = random.randint(0, 5)
#         if player != comp:
#             print('compy haxtec')
#             comp_point += 1
#             print(f'comp {comp_point}:{player_point} player')
# elif player != comp:
#     print('compy haxtec')
#     comp_point += 1
#     print(f'comp {comp_point}:{player_point} player')
#     int(input('Number: '))
#     comp = random.randint(0, 5)
#     if player != comp:
#         print('compy haxtec')
#         comp_point += 1
#         print(f'comp {comp_point}:{player_point} player')
#     elif player == comp:
#         print('es haxteci')
#         player_point += 1
#         print(f'comp {comp_point}:{player_point} player')
#         int(input('Number: '))
#         comp = random.randint(0, 5)
#         if player == comp:
#             print('es haxteci')
#             player_point += 1
#             print(f'comp {comp_point}:{player_point} player')
#         else:
#             print('compy haxtec')
#             comp_point += 1
#             print(f'comp {comp_point}:{player_point} player')
# else:
#     print('a')


# import datetime
# tday = datetime.datetime.now()
# print(tday.hour >= 9 and tday.hour < 18)
# print(tday.year)
# print(tday.month)
# print(tday.day)
# print(datetime.time(19, 23, 32, 1076))




# summ = 0
# summ += 1
# summ += 2
# summ += 3
# summ += 4
# summ += 5
# print(summ)

# for i in range(6, 25, 6):
#      summ += i
# print(summ)

# text = 'python'
# print(text[0])
# for _ in text:
#     print(_, end='')

# print(len(text))
# for i in range(len(text)): # 0, 1, 2, 3, 4, 5
#     print(f'tar {i + 1} - {text[i]}')


# text = 'Hello world'

# for i in range(len(text)): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#     print(f'tar[{i + 1}] = {text[i]}')


# summ = 0
# for tiv in range(1, 6):
#     summ += tiv
# print(summ)

# print(15 * 16 / 2)


# summ = 0
# summ += 1
# summ += 2
# summ += 3
# summ += 4
# summ += 5
# for i in range(6):
#     summ += i

# print(summ)


# tiv = 16
# print(tiv % 2)

# summ = 0
# for i in range(100):
#     if i % 2 == 0:
#         summ += i

# print(summ)

# summ = 0
# for i in range(2, 101, 2):
#     summ += i

# print(summ)


# for i in range(1, 21):
#     if i == 17:
#         continue
#     print(i)

# count = 0
# for i in range(100, 200):
#     if i % 17 == 0:
#         print(i)
#         count += 1
#         if count == 2:
#             break


# count = 0
# for i in range(120, 135):
#     if i % 17 == 0:
#         print(i)
#         break
# else:
#     print('Chka tenc tiv')

# text = 'python'
# for i in range(1, len(text)):
    # print(f'{text[i]} - {text[i + 1]}')
    # print(f'{text[i]} - {text[i - 1]}')


# import math
# tiv = int(input('TIV: '))
# for i in range(2, int(math.sqrt(tiv)) + 1):
#     if tiv % i == 0:
#         print('parz chi')
#         break
# else:
#     print('parza')

