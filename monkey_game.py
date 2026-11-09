# import random
#Mac version
# import readchar
#Windows version
#import msvcrt

# n = int(input('N: '))
# hp = 3
# scores = 0

# monkey_row = random.randint(1, n)
# monkey_column = random.randint(1, n)
# monkey_emoji = '🐵'

# zombi_row = random.randint(1, n)
# zombi_column = random.randint(1, n)
# zombi_emoji = '🧟'

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
#                 print(monkey_emoji, end='\t' )
#             elif i == banana_row and j == banana_column:
#                 print(banana_emoji, end='\t')
#             elif i == bomb_row and j == bomb_column and  scores >= 3:
#                 print(bomb_emoji, end='\t')        
#             elif i == gift_row and j == gift_column and hp == 1:
#                 print(gift_emoji, end='\t')
#             elif i == zombi_row and j == zombi_column and scores >= 5:
#                 print(zombi_emoji, end='\t')
#             else:
#                 print('*', end='\t')
#         print()
#     print('❤️ ' * hp)
#     print('⭐ ' * scores)
#     print(f'{monkey_emoji} -> {monkey_row} | {monkey_column}')
#     print(f'{bomb_emoji} -> {bomb_row} | {bomb_column}')
#     print(f'{zombi_emoji} -> {zombi_row} | {zombi_column}')

#     Mac Version
#     monkey_step = readchar.readkey()
#     Windows version
#     monkey_step = msvcrt.getwche()
#     print('\n')
#     monkey_step = monkey_step.lower()
#     if monkey_step == 'q':
#         break
#     elif monkey_step =='w':
#         if monkey_row == 1:
#             monkey_row = n
#         else:
#             monkey_row -= 1
#     elif monkey_step == 's':
#         if monkey_row == n:
#             monkey_row = 1
#         else:
#             monkey_row += 1
#     elif monkey_step == 'd':
#         if monkey_column == n:
#             monkey_column = 1
#         else:
#             monkey_column += 1
#     elif monkey_step == 'a':
#         if monkey_column == 1:
#             monkey_column = n
#         else:
#             monkey_column -= 1
#     else:
#         break

#     if monkey_row == banana_row and monkey_column == banana_column:
#         scores += 1    
#         banana_row = random.randint(1, n)
#         banana_column = random.randint(1, n)
#     elif monkey_row == bomb_row and monkey_column == bomb_column and scores >= 3:
#         hp -= 1
#         bomb_row = random.randint(1, n)
#         bomb_column = random.randint(1, n)
#     elif monkey_row == gift_row and monkey_column == gift_column and hp == 1:
#         hp += 1
#         gift_row = random.randint(1, n)
#         gift_column = random.randint(1, n)
#     elif monkey_row == zombi_row and monkey_column == zombi_column and scores >= 5:
#         hp -= 1
#         zombi_row = random.randint(1, n)
#         zombi_column = random.randint(1, n)

#     zombi_step = random.choice('wasd')
#     if zombi_step == 'q':
#             break
#     elif zombi_step =='w':
#         if zombi_row == 1:
#             zombi_row = n
#         else:
#             zombi_row -= 1
#     elif zombi_step == 's':
#         if zombi_row == n:
#             zombi_row = 1
#         else:
#             zombi_row += 1
#     elif zombi_step == 'd':
#         if zombi_column == n:
#             zombi_column = 1
#         else:
#             zombi_column += 1
#     elif zombi_step == 'a':
#         if zombi_column == 1:
#             zombi_column = n
#         else:
#             zombi_column -= 1
#     else:
#         break

#     if monkey_row == zombi_row and monkey_column == zombi_column and scores >= 5:
#         hp -= 1
#         zombi_row = random.randint(1, n)
#         zombi_column = random.randint(1, n)

#     if hp == 0:
#         print('GAME OVER')
#         break


