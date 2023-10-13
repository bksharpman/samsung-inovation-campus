# a,b = int(input())
# if a > b:
#   print(a)
# else:
#   print(b)


# a = int(input())
# if a > 0:
#   print("+")
# else:
#   print("-")


# a = int(input())
# b = int(input())
# if a > b:
#   a = a*3
#   b = b*2
#   print(a,b)
# else:
#   b = b*3
#   a = a*2
#   print(a,b)


# abc = 254
# a = abc//100
# b = abc//10%10
# c = abc%10

# if a > b and a > c :
#   print(a)
# elif b > a and b > c :
#   print(b)
# elif c > b and c > a :
#   print(c)
# else:
#   print("wtf")


# m = 20
# n = 4
# if m%n == 0:
#   print(m//n)
# else:
#   print("not completely divisible")


# n = 20
# a = 7
# na = n%10 + n//10
# #a
# if n // 10 > 0:
#   print("YES")
# else:
#   print("NO")
# #b
# if na > a:
#   print("YES")
# else:
#   print("NO")


# abc = 254
# a = abc//100
# b = abc//10%10
# c = abc%10
# ab = a + b
# bc = b + c
# if ab > bc:
#   print(f"{bc}{ab}")
# else:
#   print(f"{ab}{bc}")


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# abcd = a+b+c+d
# abcd_mid = (5*a + 4*b + 3*c + 2*d)/abcd
# if 3 >= abcd_mid:
#   print(a + b + c)
# elif 4 >= abcd_mid:
#   print(a + b)
# else:
#   print(a)


# minutes = int(input())
# h = minutes//60
# m =minutes%60

# if h < 10 and m < 10:
#   print(f"0{h}:0{m}", end="")
# elif h < 10 and m >= 10:
#   print(f"0{h}:{m}", end="")
# elif h >= 10 and m < 10:
#   print(f"{h}:0{m}", end="")
# else:
#   print(f"{h}:{m}", end="")

# if minutes >= 540 and minutes < 1080:
#   print(" - working time")
# else:
#   print(" - free time")


# day = int(input())
# month = int(input())
# year = int(input())

# if year % 4 == 0:
#   if month == 2:
#     a = day <=29
#     print(a)
#   elif month == 4 or 6 or 9 or 11:
#     a = day <=30
#     print(a)
#   else:
#     a = day <= 31
#     print(a)
# else:
#   if month == 2:
#     a = day <=28
#     print(a)
#   elif month == 4 or 6 or 9 or 11:
#     a = day <=30
#     print(a)
#   else:
#     a = day <= 31
#     print(a)


# day = int(input())
# month = int(input())
# year = int(input())
# seconds = int(input())

# day_seconds = seconds//86400
# if day < 10 and month < 10:
#   print(f"0{day + day_seconds}.0{month}.{year}", end="")
# elif day < 10 and month >= 10:
#   print(f"0{day + day_seconds}.{month}.{year}", end="")
# elif day >= 10 and month < 10:
#   print(f"{day + day_seconds}.0{month}.{year}", end="")
# else:
#   print(f"{day + day_seconds}.{month}.{year}", end="")


# day=10; month=1; year=2020
# flag = True

# if day < 1 or day > 31 or month < 1 or month > 12 or year < 1:
#   flag = False

# if day == 31 and (month == 2 or month == 4 or month == 6):
#   flag = False

# if day == 30 and month == 2:
#   flag = False

# if day == 29 and month == 2 and year % 4 != 0:
#   flag = False

# print(flag)

