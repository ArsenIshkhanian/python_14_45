# scores = {
#     "Anna": 85,
#     "John": 92,
#     "David": 78,
#     "Maria": 95
# }


# max_name = sorted(scores, key=scores.get, reverse=True)[0]
# max_value = scores[max_name]
# print(max_name, max_value)

# max_value = 0
# max_name = ''

# for key in scores:
#     if scores[key] > max_value:
#         max_value = scores[key]
#         max_name = key

# print(max_name, max_value)


# text = "banana"
# letters = {}

# for letter in text:
#     if letter in letters:
#         letters[letter] += 1
#     else:
#         letters[letter] = 1

# print(letters)



# numbers = [4, 2, 4, 1, 2, 4, 3]
# new_dict = {}
# for number in numbers:
#     if number in new_dict:
#         new_dict[number] += 1
#     else:
#         new_dict[number] = 1

# max_number = sorted(new_dict, key=new_dict.get)[-1]
# max_count = new_dict[max_number]
# print(f'Most frquent number is {max_number}, which repeated {max_count} times.')



# numbers = [2, 3, 4, 5, 6, 7, 11, 15]
# target = 9
# new_dict = {} 
# for number in numbers:
#     zuyg = target - number
#     if zuyg in new_dict:
#         print(zuyg, new_dict[zuyg])
#     else:
#         new_dict[number] = zuyg

# print(new_dict)



# users = {}
# while True:
#     name = input('Enter your name: ')
#     if name.lower() == 'q':
#         break
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")
#     users[name] = {
#         'Email': email,
#         'Password': password
#     }
# for name in users:
#     print(f"{name} -> {users[name]['Email']} {users[name]['Password']}")




# import random
# new_dict = {}

# for _ in range(1000):
#     zar_1 = random.randint(1, 6)
#     zar_2 = random.randint(1, 6)
#     gumar = zar_1 + zar_2
#     if gumar not in new_dict:
#         new_dict[gumar] = 1
#     else:
#         new_dict[gumar] += 1     

# print(new_dict)



# info = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
# text = input('Enter the text: ').upper() #Hello
# summ = 0
# for letter in text:
#     for key in info:
#         if letter in info[key]:
#             summ += key
# print(summ)



# info = {
#     '1': '.,?!:',
#     '2': 'ABC',
#     '3': 'DEF',
#     '4': 'GHI',
#     '5': 'JKL',
#     '6': 'MNO',
#     '7': 'PQRS',
#     '8': 'TUV',
#     '9': 'WXYZ',
#     '0': ' '
# }

# text = input("Text: ").upper() #Hello
# sequence = ''

# for letter in text:
#     for key in info:
#         if letter in info[key]:
#             index = info[key].index(letter) + 1
#             sequence += index * key

# print(sequence)
