#Ex. 15
# def compress(text): 
#     sequence = '' 
#     count = 1 
#     for i in range(len(text) - 1):
#         if text[i] == text[i + 1]:
#             count += 1
#         else:
#             sequence += text[i] + str(count)
#             count = 1

#     sequence += text[-1] + str(count)

#     return sequence

# print(compress('aaccdda'))

#Ex. 14
# def character_frequency(text):
#     data = {}
#     for letter in text:
#         if letter in data:
#             data[letter] += 1
#         else:
#             data[letter] = 1

#     return data
# print(character_frequency('Banana'))
    

#Ex. 16
# def is_prime(number):
#     for bajanarar in range(2, int(number**0.5) + 1):
#         if number % bajanarar == 0:
#             return False
#     return True


# def count_prime(numbers):
#     count = 0
#     for number in numbers:
#         if is_prime(number):
#             count += 1

#     return count
# print(count_prime([2, 3, 4, 5, 6, 7, 8, 9, 10]))



#Ex. 8
# def sum_numbers(n):
    ##Version 1
    # summ = 0 
    # for i in range(1, n + 1):
    #     summ += i

    ##Version 2
    # return summ
#     return n * (n + 1) // 2
# print(sum_numbers(5))


#Ex. 9
# def count_even(numbers):
#     count = 0
#     for number in numbers:
#         if number % 2 == 0:
#             count += 1
#     return count

# print(count_even([1, 2, 3, 4, 5, 6]))


