# text = 'python'

# for letter in text:
#     print(letter)

# n = len(text)
# for i in range(n):
#     print(f'{i + 1} -> {text[i]}')

# for i in range(15):
#     print(i)

# for i in range(len(text) - 1): # 5
#     print(f'{text[i]} -> {text[i + 1]}')


# summ = 0
# for i in range(1, 6):
#     summ += i

# print(summ)

# summ = 5 * 6 / 2
# print(int(summ))


# grechka = 100
# amisner = int(grechka / 4)

# for i in range(amisner):
#     print(f'amis {i + 1}')
#     grechka = grechka - 4
#     print(f'Dzez mnac utelu {grechka}')
# print('Dzez bari baxt')


# n = int(input('N: '))
# summ = 0
# for i in range(5, n + 1, 5):
#     debt = float(input(f'Debt[{i}]: '))
#     summ += debt
# print(f'${summ}')




# import time
# timer = int(input('Timer: ')) # 10
# for second in range(timer, -1, -1):
#     # print(second)
#     time.sleep(1)
#     status = input(f"Kuzes hanes {second}rd vayrkyanum uteliqd(yes/no)? ").lower()
#     if status == 'yes':
#         print(f'Dzer uteliqy patrast exav {timer - second} vayrkyanum!!')
#         break
# else:
#     print('Dzer uteliqy patrast e!')



# a = int(input('a: '))# 10
# b = int(input('b: '))# 15
# c = int(input('c: '))# 3

# summ = 0 # + 12 + 15
# count = 0 # + 1 + 1
# for i in range(a, b + 1):
#     if i % c == 0:
#         summ += i
#         count += 1

# avg = summ / count
# print(avg)


# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# for x in range(b, a, c):
#     y = x ** 3 + 2 * x ** 2 - 4 * x + 1
#     print(f'{x} -> {y}')


# a = int(input('koxm: ')) # 65 -> 32 -> 16 -> 8 
# count = 0
# for i in range(100):
#     if a > 12:
#         a /= 2
#         count += 2
#     else:
#         print(count)
#         break


# toshak = float(input("Toshak: ")) # 90
# tsaxs = float(input("Tsaxs: ")) # 100

# paderjka = 0

# for i in range(10):
#     paderjka += tsaxs - toshak
#     print(f'amis {i + 1} -> tsaxs = ${round(tsaxs, 2)}')
#     tsaxs *= 1.03

# print(f'Tati jan uxarki ${round(paderjka, 2)} pox')
    


# n = int(input("N: "))
# s = 0

# for i in range(n):
#     s += (-1)**i * (1/(2**i))
#     print(f'{i} -> {s}')

# print(s)


# x = float(input("X: "))
# hamarich = 1
# haytarar = 1
# for i in range(1, 7):
#     hamarich *= (x - ((2**i) - 1))
#     haytarar *= (x - 2**i)

# res = hamarich / haytarar
# print(res)


# x = float(input('x: '))
# hamarich = (x - 1)*(x - 3)*(x - 7)*(x - 15)*(x - 31)*(x - 63)
# haytarar = (x - 2)*(x - 4)*(x - 8)*(x - 16)*(x - 32)*(x - 64)
# print(hamarich / haytarar)


# G = int(input("Girls: "))
# B = int(input("Boys: "))

# if B > 2 * G or G > 2 * B:
#     print('Dzev chka')
# elif B > G:
#     n = B - G
#     skizb = "BGB" * n
#     verj = "BG" * (G - n)
#     print(f'{skizb}{verj}')
# elif B < G:
#     n = G - B
#     skizb = "GBG" * n
#     verj = "GB" * (B - n)
#     print(f'{skizb}{verj}')
# else:
#     print('GB' * B)

