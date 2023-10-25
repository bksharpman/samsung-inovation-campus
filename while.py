# i = 0
# m = int(input())
# while i <= 100:
#   if i % m == 0:
#     print(i)
#   i += 1


# i = 0
# s = 0
# m = int(input())
# while i <= m:
#   s = s+i
#   i+=1
# print(s)  


# i = 0
# m = int(input())
# while m != 0:
#   m //= 10
#   i += 1
# print(i)


# m = int(input())
# s = 0
# while m > 0:
#   s = s + m%10
#   m = m//10
# print(s)


# m = int(input())
# mmax = 0
# mmin = 9
# while m > 0:
#   digit = m % 10
#   mmax = max(digit,mmax)
#   mmin = min(digit,mmin)
#   m = m // 10
# print(f"maximum:{mmax}")
# print(f"minimum:{mmin}")


# n = int(input())
# k = int(input())

# total = 0
# while n > 0:
#   if n%10 == k:
#     total = total + 1
#   else:
#     total = total
#   n = n//10
# print(total)


# n = int(input())
# n_reverse = 0
# m = 0
# while n > 0:
#   m = n%10
#   n_reverse = n_reverse*10 + m
#   n = n//10
# print(n_reverse)


# n = int(input())
# i = 1
# while i <= n:
#   print(i**2)
#   i+=1

# x = float(input())
# y = float(input())
# d = 1

# while x <= y:
#   x += (x + x*0.1)
#   d += 1
# print(d)


# x = int(input("Введите начальный вклад (в тенге): "))
# p = int(input("Введите процент увеличения (в процентах): "))
# y = int(input("Введите целевую сумму (в тенге): "))
# d = 1
# p = p / 100
# while x <= y:
#   d += 1
#   x = x + x*p
#   print(x)

# print(f"Через {d} лет вклад составит не менее {y} тенге.")

# 10. Вклад в банке составляет x тенге. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается. Определите, через сколько лет вклад составит не менее y тенге