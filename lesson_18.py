# elements = {5,}
# print(type(elements))


# elements = {1, 2, 3, 4, 5}
# elements.add(6)
# elements.add(6)
# print(elements)
# elements.discard(7)
# print(elements)

# a = {1, 2, 3}
# b = {4, 5, 6}
# a.add(b)
# b.update(a)
# print(a)
# print(b)


# a = {1, 2, 3, 6}
# b = {2, 4, 5, 6}
# print(a.intersection(b))

# a = {1, 2, 3}
# b = {4, 5, 6}
# print(a.isdisjoint(b))

# a = {1, 2, 3}
# b = {2, 4, 5}
# print(a.difference(b))
# print(b.difference(a))


# a = {1, 2, 3}
# b = a.copy()
# a.add(6)
# print(b)

# a = {1, 2, 3, 4, 5, 6, 7}
# b = {5, 4, 1, 2, 3, 7, 6}
# print(b.issubset(a))
# print(a.issuperset(b))

# a = [1, 2, 3, 3, 2, 1, 4, 5, 5, 4, 3, 2]
# print(set(a))



# def add():
#     print(10)

# x = add()
# print(x)


# def add():
#     return 10

# x = add()
# print(x + 5)


# def multiplication_table():
#     for i in range(1, 11):
#         for j in range(1, 11):
#             print(i*j, end='\t')
#         print()

# for i in range(10):
#     multiplication_table()
#     print('-'*50)


# def add():
#     return 10

# print(add() + 5)


# def add(a, b):
#     return a + b

# print(add(198, 89))


# def add(a, b, c, d):
#     return a + b + c + d

# print(add(16, 24, d=6, c=7))



# def show(*args, b):
#     print(args)
#     print(b)

# show(1, 2, 3, 4, 5, 6, 7, 7, b=8)




# def show(**kwargs):
#     for key in kwargs:
#         print(f'{key} -> {kwargs[key]}')

# show(a=6, b=7)
# show()


# from inchvor import sqrt
# print(sqrt(25))



# x = 6

# def a(b):
#     b += 1
#     print(b)

# a(x)
# print(x) # 6


# x = 6
# b = x
# b += 1
# print(x)

# c = [1, 2, 3]

# def a(b):
#     b.append(5)
#     print(b)

# a(c)
# print(c)


# a = [1, 2, 3]
# b = a
# a.append(5)
# print(b)


# def f1(a, b):
#     b += 2 #6
#     def f2(c, d):
#         print(c + d)
#     f2(a, b)
# f1(2, 4)


# x = lambda a, b: a + b
# print(x(2, 4))


# def is_prime(a):
#     for i in range(2, a):
#         if a % i == 0:
#             return False
#     else:
#         return True

# def filter(mylist):
#     new_list = []
#     for element in mylist:
#         if is_prime(element) == True:
#             new_list.append(element)

#     return new_list


# list_ = [i for i in range(2, 100)]
# prime_elements = filter(list_)
# print(prime_elements)