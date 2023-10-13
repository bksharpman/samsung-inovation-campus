# x = 5
# y = 5
# b = (x * 2 > 20 or y / 2 <= 2 and not(x * x == y * 5))
# b = (x * 2 > 20 or y / 2 <= 2 and not(25 == 25))
# b = (x * 2 > 20 or y / 2 <= 2 and not(True))
# b = (10 > 20 or y / 2 <= 2 and not(True))
# b = (10 > 20 or 2.5 <= 2 and not(True))
# b = (False or 2.5 <= 2 and not(True))
# b = (False or False and not(True))
# b = (False or False and False)
# b = (False or False)
# b = (False)
# print(b)


# x = 5
# y = 5
# b = (x - 2 >= y + 4) or not(x == y * 2 or y * y <= 100) and ((x + 7 * y < 50) == (4 / x < 1))
# b = (5 - 2 >= 5 + 4) or not(5 == 5 * 2 or 5 * 5 <= 100) and ((5 + 7 * 5 < 50) == (4 / 5 < 1))
# b = (5 - 2 >= 5 + 4) or not(5 == 5 * 2 or 5 * 5 <= 100) and ((False) == (4 / 5 < 1))
# b = (5 - 2 >= 5 + 4) or not(5 == 5 * 2 or 5 * 5 <= 100) and ((False) == (True))
# b = (5 - 2 >= 5 + 4) or not(5 == 5 * 2 or 5 * 5 <= 100) and (False)
# b = (False) or not(5 == 5 * 2 or 5 * 5 <= 100) and (False)
# b = (False) or not(False or True) and (False)
# b = (False) or not(True) and (False)
# b = (False) or False and (False)
# b = False or False
# b = False
# print(b)


# x = 5
# y = 5
# b = (x - 2 > y * 0.5) and (y % 2 == 0 and x % 2 == 0) or not(x * x + y * y == 100 / (x / 2))
# b = (True) and (5 % 2 == 0 and 5 % 2 == 0) or not(5 * 5 + 5 * 5 == 100 / 2.5)
# b = (True) and (5 % 2 == 0 and 5 % 2 == 0) or not(False)
# b = (True) and (False and False) or not(False)
# b = (True) and (False) or not(False)
# b = (True) and (False) or True
# b = False or True
# b = True
# print(b)


# a = int(input())
# b = int(input())
# if a % 2 == 1 and b % 2 == 1:
#   print("Yes")
# else:
#   print("No")


# a = int(input())
# b = int(input())
# if a % 2 == 1 or b % 2 == 1:
#   print("Yes")
# else:
#   print("No")


# a = int(input())
# b = int(input())
# if a % 2 == 0 and b % 2 == 0:
#   print("NO")
# elif a % 2 == 1 and b % 2 == 1:
#   print("NO")
# else:
#   print("YES")


# a = int(input())
# b = int(input())
# if a % 2 == b % 2:
#   print("YES")
# else:
#   print("NO")


# a = 5
# b = 5
# c = 5
# x = (a and b and c) > 0
# print(x)


# a = 5
# b = -5
# c = -5
# x = (a or b or c) > 0
# print(x)


# a, b, c = -1, 2, -3

# result = (a > 0) + (b > 0) + (c > 0) == 1
# print(result)


# a, b, c = 1, 2, -3

# result = (a > 0) + (b > 0) + (c > 0) == 2
# print(result)


# a = 14
# result = (a // 10) and (a % 2 == 0)
# print(result)


# a = 142
# result = (a // 100) and (a % 2 == 1)
# print(result)


# a, b, c = 1, 2, 3

# result = (a == b) + (b == c) + (c == a) >= 1
# print(result)


# a, b, c = 1, 2, -2

# result = ((a + b) == 0) or ((b + c) == 0)  or ((c + a) == 0)
# print(result)


# abc = 234
# a = abc//100
# b = abc//10%10
# c = abc%10
# result = not(a==b) and not(b==c) and not(c==a)
# print(result)


# abc = 234
# a = abc//100
# b = abc//10%10
# c = abc%10
# result = a < b < c
# print(result)


# abc = 4334
# a = abc//1000
# b = abc//100%10
# c = abc//10%10
# d = abc%10
# result = (a==d) and (b==c)
# print(result)


# a, b, c = 1, 2, 3
# d = b*2-4*a*c
# result = (d >= 0)
# print(result)


# a, b, c = 2, 3, 1
# result = (a == b) or (b == c) or (c == a)
# print(result)


# a, b, c = 2, 2, 2
# result = not((a == b) and (b == c) and (c == a))
# print(result)


# x = 5
# y = 1
# result = ((x + y) % 2 == 0)
# print(result)


# x1 = 1
# y1 = 1
# x2 = 1
# y2 = 5
# result = (x1==x2 or y1==y2)
# print(result)


# x1 = 1
# y1 = 1
# x2 = 1
# y2 = 2
# result = abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
# print(result)


# x1 = 1
# y1 = 1
# x2 = 3
# y2 = 3
# result = (x1/x2) == (y1/y2)
# print(result)


# x1 = 1
# y1 = 1
# x2 = 2
# y2 = 3
# result = ((x1/x2) == (y1/y2)) or ((x1==x2 or y1==y2)) 
# print(result)