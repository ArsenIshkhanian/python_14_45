#mytuple = (7, 8, 'Arsen', True, 7.89)
# mytuple = 7, 8, 9, 10, 'Arsen', True
# print(type(mytuple))


# mytuple = 7, 8, 9, 10, 'Arsen', True
# for value in mytuple:
#     print(value)

# mylist = [7, 'Arsen', 'OK', True, [8, 9, 10]]
# # print(type(mylist))
# print(mylist[4][0])

# mylist = [1, 2, 3, 4]
# y = mylist
# mylist.append(5)
# print(y)


# mylist = [6, 5, 1, 2, 3, 4]
# mylist.sort(reverse=True)
# print(mylist)


# mylist = ['g', 'a', 'c', 'b']
# mylist.sort(reverse=True)
# print(mylist)


# mylist = ['Arsen', 'Is', 'Hamlet', 'Nver', 'Yervand', 'Artur']
# mylist.sort(key=len)
# print(mylist[-1])

# from copy import deepcopy
# mylist = [1, 2, 3, [4, 5]]
# y = mylist[:]
# y = mylist[::]
# y = list(mylist)
# y = deepcopy(mylist)
# mylist[3][0] = 6
# print(y)


# mylist = [1, 2, 3, 4, 5]
# mylist.insert(1, 6)
# print(mylist)

# mylist = [1, 2, 3, 4, 5]
# mylist[0] = 8
# print(mylist)


# mylist = [1, 2, 3, 4, 5]
# deleted_element = mylist.pop()
# print(mylist)
# print(deleted_element)

# mylist.pop(1)
# print(mylist)

# mylist.remove(3)
# print(mylist)

# del mylist[2:]
# print(mylist)


# mylist = [1, 2, 3, 4, 5, 2, 2, 2, 3, 3, 3]
# print(mylist.pop(mylist.index(3)))
# print(mylist.remove(3))

# print(mylist.count(3))

# mylist = [1, 2, 3, 4, 5, 2, 2, 2, 3, 3, 3]
# mylist.clear()
# mylist = []
# print(mylist)

# x = [1, 2, 3]
# y = [4, 5, 6]
# x.append(y)
# x.extend(y)
# x += y
# print(x)

# text = 'a'
# print([text] * 12)

# mylist = [None]
# mylist = mylist * 12


# mylist = ['a', 'b', 'c']

# for value in range(len(mylist)):
#     print(f'{value} -> {mylist[value]}')


# for index, value in enumerate(mylist):
#     print(f'{index} -> {value}') 



# x = [19, 20, 13, 17]
# y = ['Hamlet', 'Artur', 'Nver']

# for name, grade in zip(y, x):
#     print(f'{name} -> {grade}')


# x = [1, 2, 3, 4, 5, 6, 7]
# y = []

# for i in x:
#     if i % 2 == 0:
#         y.append(i)
# print(y)

# y = [i for i in x if i % 2 == 0]
# print(y)

# y = [i for i in range(1, 11)]
# print(y)


# x = [1, 7, 9, 10, 12, 14]
# y = []

# for i in x:
#     if i % 2 == 0:
#         y.append('zuyg')
#     else:
#         y.append('kent')
# print(y)

# y = ['Zuyg' if i % 2 == 0 else 'Kent' for i in x]
# print(y)



# for i in range(17):
#     if i == 10:
#         continue
#     print(i)


# for num in range(2, -5, -1):
#     print(num, end=' ')


# for i in range(3):
#     if i == 19:
#         break
#     print(i)
# else:
#     print('loop finished')



