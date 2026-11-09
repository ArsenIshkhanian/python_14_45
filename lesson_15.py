# import time
# nums = [4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2 ,4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2, 4, 2, 3, 7, 2,4, 2, 3, 7, 2]

# start = time.time()
# for num in nums: #O(n)
#     if nums.count(num) > 1: #O(n)
#         print(num)
# end = time.time()
# version_1 = end - start

# start = time.time()
# nums.sort() # O(nlogn)
# for i in range(len(nums) - 1): #O(n)
#     if nums[i] == nums[i + 1]:
#         print(nums[i])
# end = time.time()
# version_2 = end - start

# print(version_1 - version_2)



# nums = [1, 3, 4, 6, 7, 8, 10]
# target = 45
# for i in range(len(nums)): #O(n)
#     for j in range(i + 1, len(nums)): #O(n)
#         if nums[i] + nums[j] == target:
#             print(nums[i], nums[j])
#     

# i = 0 # 4
# j = len(nums) - 1 # 4
# while i < j:
#     if nums[i] + nums[j] == target:
#         print(nums[i], nums[j])
#         break
#     elif nums[i] + nums[j] < target:
#         i += 1
#     else:
#         j -= 1
# else:
#     print(-1)


# for i in range(len(nums)):
#     print(i)

# for number in nums:
#     print(number)



# nums = [4, 8, 2, 10, 6]
# maximum = 0
# for num in nums:
#     if num > maximum:
#         maximum = num
# print(maximum)




# nums = [4, 9, 2, 9, 7]
# verj = 0 # 4, 9
# nax = 0 # 0, 4, 7

# for num in nums: # 4, 9, 2, 9, 7
#     if num > verj:
#         nax = verj
#         verj = num
#     elif num > nax and num != verj:
#         nax = num
# print(nax, verj)




# nums = [1, 3, 3, 7, 9]
# for i in range(len(nums)-1):
#     if nums[i] > nums[i+1]:
#         print(False)
#         break
# else:
#     print(True)


# print(abs(17 - 18))
# print(abs(17 - 15))