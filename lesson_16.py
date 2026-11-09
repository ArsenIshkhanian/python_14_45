nums = [10, 3, 20, 8, 15, 19]
# num = abs(nums[1] - nums[0]) #10
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         result = abs(nums[i] - nums[j])
#         if result < num:
#             num = result
#             near_numbers = nums[i], nums[j]
        
# print(near_numbers)


# nums.sort() #O(nlogn)
# print(nums)
# minimum_dif = nums[1] - nums[0]

# for i in range(len(nums) - 1): # 1
#     if nums[i + 1] - nums[i] < minimum_dif:
#         minimum_dif = nums[i + 1] - nums[i]
#         minimum_numbers = nums[i + 1], nums[i]

# print(minimum_numbers)


# a = [1, 3, 5, 7]
# b = [2, 3, 6, 7]


# for element_a in a:
#     for element_b in b:
#         if element_a == element_b:
#             print(element_a)



# a = [1, 3, 5, 7] 
# b = [2, 3, 6, 7]
# i = 0 # 1 # 2 # 3 # 4
# j = 0 # 1 # 2 # 3 # 4
# # O(n)
# while i < len(a) and j < len(b):
#     if a[i] == b[j]:
#         print(a[i])
#         i += 1
#         j += 1
#     elif a[i] > b[j]:
#         j += 1
#     else:
#         i += 1





# nums = [2, 8, 19, 21, 30, 15]
# target = 17
# closest = 0 # 2 # 8 # 19
# dublicate = -1

# for num in nums: # 2, 8, 19, 21, 30, 15
#     heravorutyun = abs(num - target) # 2
#     amenamot = abs(closest - target) # 2

#     if heravorutyun < amenamot:
#         closest = num
#     elif heravorutyun == amenamot:
#         dublicate = num
    

# print(closest, dublicate)



# nums = [1, 1, 2, 2, 2, 3, 4, 4]
# for i in range(len(nums) - 1, 0, -1):
#     if nums[i] == nums[i - 1]:
#         nums.pop(i)

# print(nums)


# nums = [1, 2, 3, 4]
# i = 0 # 3
# while i < len(nums) - 1: # 3
#     if nums[i] == nums[i + 1]:
#         nums.pop(i)
#     else:
#         i += 1
# print(nums)

# a = [1, 2, 3]
# b = a
# a.append(4)
# print(b)


# a = 5
# b = a
# a += 1
# print(b)



# data = {'a': 1, 'b': 2, 'c': 3}


# data = {
#     'b': 1,
#     'a': 4,
#     'c': 3,
#     'd': 2
# }

# print(data['b'])
# print(data.keys())
# print(data.values())
# print(data.items())

# new_data = dict([('b', 1), ('a', 4), ('c', 3), ('d', 2)])
# print(new_data)


# for key in data:
#     print(key, data[key])

# for key in data.keys():
#     print(key)

# for value in data.values():
#     print(value)


# for key, value in data.items():
#     print(key, value)


# data = {
#     'b': 1,
#     'a': 4,
#     'c': 3,
#     'd': 2,
# }


# print('c' in data)
# data['d'] = 15
# data.setdefault('f', 15)

# print(data)
# data.popitem()
# print(data)
# data.pop('b')
# print(data)

# print(data.get('d'))


# data = {
#     'b': 1,
#     'a': 4,
#     'c': 3,
#     'd': 2,
# }
# a = {
#     'f': 2,
#     'G': 4
# }

# data.update(a)
# a.update(data)
# print(a)



# data = {
#     'b': 1,
#     'a': 4,
#     'c': 3,
#     'd': 2,
# }
# print({key: data[key] for key in sorted(data, key=data.get)})

# data_sort = sorted(data, key=data.get)

# new_dict = {}

# for key in data_sort:
#     new_dict[key] = data[key]

# print(new_dict)


