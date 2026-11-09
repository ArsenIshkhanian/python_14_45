# x = ['apple', 'orange', 'strawberry']
# y = ['pinapple', 'greafruit']
# status = False
# for i in range(len(x)):
#     for j in range(len(y)):
#         if x[i] == y[j]:
#             status = True
#             print('True')
#             break
#     if status:
#         break
# else:
#     print('False')



# password = input("Password: ")
# count_digit = 0
# count_symbol = 0
# for i in password:
#     if i.isdigit():
#         count_digit += 1
#     elif not i.isalnum():
#         count_symbol += 1

# print(len(password) >= 8 and count_digit >= 2 and count_symbol >= 2)
    


# link = 'https://www.youtube.com/watch?v=RRW2aUSw5vU'
# print(link.split('=')[1])


# word = input("word: ").lower() # raceecar
# # print(word == word[::-1])
# for i in range(len(word) // 2):
#     if word[i] != word[len(word) - 1 - i]:
#         print('Trash')
#         break
# else:
#     print('Open')



# word = input("N: ")
# mylist = ['1', '2', '4', '3', '1', 'd', 'q', 'd', 'c', 'q']
# # for i in word:
# #     mylist.append(i)

# print(mylist[-1:-3:-1])



# mylist = [74, 56, 44, 66,  57, 9, 8, 12, 14, 16]
# for num in mylist[::-1]:
#     if num % 2 == 0:
#         mylist.remove(num)
# print(mylist)



# import random
# qashoxner = ['Arsen', 'Yervand', 'Artur', 'Nver']
# qashvoxner = ['Arsen', 'Yervand', 'Artur', 'Nver']
# fail_status = False

# while len(qashoxner) > 0:
#     qashox = random.choice(qashoxner)
#     qashvox = random.choice(qashvoxner)
#     while qashox == qashvox:
#         if len(qashvoxner) == 1:
#             fail_status = True
#             break
#         else:
#             qashvox = random.choice(qashvoxner)
#     if fail_status:
#         print('----Noric enq sksum----')
#         qashoxner = ['Arsen', 'Yervand', 'Artur', 'Nver']
#         qashvoxner = ['Arsen', 'Yervand', 'Artur', 'Nver']
#         fail_status = False
#     else:
#         print(f'{qashox} -> {qashvox}')
#         qashoxner.remove(qashox)
#         qashvoxner.remove(qashvox)
    

# mylist = [1, 2, 2, 3, 4, 3, 5, 1]
# for i in mylist[::-1]:
#     if mylist.count(i) > 1:
#         mylist.remove(i)

# print(mylist) 


# list_ = [1, 2, 3, 4]
# for i in list_:
#     if i == 4:
#         print(True)
#         break


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=' ')
#     print()

# import math
# print(math.log2(1000000))


# mylist = [1,8,7,5,4,6]
# # mylist.sort()
# # print(mylist)
# for i in range(len(mylist)):
#     status = True
#     for j in range(len(mylist) - 1 - i):
#         if mylist[j] > mylist[j + 1]:
#             status = False
#             mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
#     if status:
#         break

# print(mylist)


# nums = [4, 2, 7, 3, 2]

# for i in nums: # O(n)
#     if nums.count(i) > 1: # O(n)
#         print(i)
#         break

# nums.sort() # O(nlogn) [2, 3, 4, 4, 7]

# for i in range(len(nums) - 1): #O(n)
#     if nums[i + 1] == nums[i]:
#         print(nums[i])
#         break

# nums = [1, 3, 4, 6, 8, 10]
# target = 14
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == 14:
#             print(nums[i], nums[j])

