# name = input('Enter the username: ')
# not_alloed = 'bot' not in name and 'admin' not in name
# print(not_alloed)
# print('bot' not in name and 'admin' not in name)
# print('bot' != name and 'admin' != name)


# age = int(input('Enter age: '))
# passport_status = input('Do you have a passport(yes/no)? ').lower()
# destination = input('Country: ')
# print(age >= 18 and passport_status == 'yes' and destination != 'North Korea')


# import random
# zar_1 = random.randint(1, 6)
# print(zar_1 == 1 or zar_1 == 6)
# round(4.6)
# abs(-4)


# import random
# import time
# loading_time = random.randint(1, 10)
# print(loading_time)
# print('Loading...')
# time.sleep(loading_time)
# print(loading_time <= 5)



# x = int(input('X: '))
# y = int(input('Y: '))
# if x > y:
#     print('x is max')
# elif x == y:
#     print('x == y')    
# else:
#     print('y is max')

# print('out of block')



# x = int(input('X: '))
# y = int(input('Y: '))
# if x > y:
#     print('x is max')
#     if x < 10:
#         print('y poqra 10-ic')
#     else:
#         print('x metsa 10-ic')
# elif x == y:
#     print('x = y')
#     if x < 500:
#         print('x-n u y-y poqr en 500-ic')
#     elif x < 1000:
#         print('x-n u y-y poqr en 1000-ic')
# else:
#     print('y is max')



# exanak = input("Exanak(arev/xyamat/andzrev): ").lower()
# if exanak == 'andzrev':
#     print('Mna tany python ara')
# elif exanak == 'arev':
#     bassein = input('Karoxa gnas basein? ').lower()
#     if bassein == 'ayo':
#         tex = input('Ba ures uzum gnas(Dvin/Akvatek/Reebok)? ').lower()
#         if tex == 'dvin':
#             print('Ari im hetevic')
#         elif tex == 'reebok':
#             print('Lavel dzvats es')
#         else:
#             print('De qez lav or')
#     else:
#         avto_lval = input('Karoxa avton lvas? ').lower()
#         if avto_lval == 'ayo':
#             print('tuyn')
#         else:
#             print('Inch anhvaes lakot durs ekar:')
# elif exanak == 'xyamat':
#     print('Taq hagvni nor durs ari')
# else:
#     print('Es tenc exanak chgitem')



# import random
# import time
# name = input('Enter your name: ').capitalize()
# user_status = input(f'{name} jan are you ready(yes/no)? ').lower()
# if user_status == 'yes':
#     time.sleep(0.7)
#     print(3)
#     time.sleep(0.7)
#     print(2)
#     time.sleep(0.7)
#     print(1)
#     time.sleep(0.7)
#     print("Let's Go")
#     user_score = 0
#     comp_score = 0
#     comp_number = random.randint(1, 5)
#     user_number = int(input('Guess the number(1-5)? '))
#     if user_number == comp_number: # es-1 comp-0
#         user_score += 1
#         print(f'{name} WIN this round!!!')
#         print(f'comp -> {comp_number} | {name} -> {user_number} SCORES: {user_score}/{comp_score}')
#         comp_number = random.randint(1, 5)
#         user_number = int(input('Guess the number(1-5)? '))
#         if user_number == comp_number: # es-2 comp-0
#             user_score += 1
#             print(f'{name} WIN this round!!!')
#             print(f'comp -> {comp_number} | {name} -> {user_number} SCORES: {user_score}/{comp_score}')
#             print(f'END GAME:::{name} WIN!!!')
#         else: # es-1 comp-1
#             comp_score += 1
#             print(f'Comp WIN this round!!!')
#             print(f'comp -> {comp_number} | {name} -> {user_number} SCORES: {user_score}/{comp_score}')
#             print(f'END GAME:::DRAW!!!')
#     else: # es-0 comp-1
#         comp_score += 1
#         print(f'Comp WIN this round!!!')
#         print(f'comp -> {comp_number} | {name} -> {user_number} SCORES: {user_score}/{comp_score}')
#         comp_number = random.randint(1, 5)
#         user_number = int(input('Guess the number(1-5)? '))
#         if user_number == comp_number: # es-1 comp-1
#             user_score += 1
#             print(f'{name} WIN this round!!!')
#             print(f'comp -> {comp_number} | {name} -> {user_number} SCORES: {user_score}/{comp_score}')
#             print(f'END GAME:::DRAW!!!')
#         else: #es-0 comp-2
#             comp_score += 1
#             print(f'Comp WIN this round!!!')
#             print(f'comp -> {comp_number} | {name} -> {user_number} SCORES: {user_score}/{comp_score}')
#             print(f'END GAME:::Comp WIN!!!')
# else:
#     print('De du gites!')


# x = int(input('X: '))
# y = int(input('Y: '))
# if x > y:
#     print('x metsa y-ic')
# elif x == y:
#     print('x havasar e y-i')
# elif x < y:
#     print('x poqra y-ic')

# letter = input('Letter: ')
# print(letter)

# if x > y:
#     print('x meysa y-ic')
# else:
#     print('If-ic durs')

# if 10 > 6:
#     print('mi ban')

# print()


# print('p' in 'python')

# dzaynavor = 'aeiou'
# baghadzayn = 'qwrtypsdfghjklzxcvbnm'
# tar = input('Tar: ').lower()
# if tar in dzaynavor:
#     print(f'{tar}-n dzaynavor e')
# elif tar in baghadzayn:
#     print(f'{tar}-y baghadzayn e')
# else:
#     print(f'{tar} tar chi')



# tar = input('Tar: ').lower()
# print(tar.isalpha())
# print(tar.isdigit())
# print(not tar.isalnum())
# if tar.isalpha():
#     if tar in 'aeiou':
#         print(f'{tar} dzaynavor e')
#     else:
#         print(f'{tar} baghadzayn e')
# elif tar.isdigit():
#     print(f'{tar} tvi poxaren nermutseq tar')
# else: 
#     print(f'{tar} tar chi')

# age = int(input('Age: '))
# if age < 2:
#     print('noratsin')
# elif age < 14:
#     print('derahas')
# elif age < 18:
#     print('patani')
# elif age < 63:
#     print('mec mard')
# else:
#     print('toshakaru')