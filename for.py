# #1
# n = int(input())
# for i in range(1,11):
#   print(f"{n}*{i}={i*n}", end="; ")


# #2
# a = int(input())
# b = int(input())
# if a%2 == 0:
#   for i in range(a,b+1,2):
#     print(i+1, end= " ")
# else:
#   for i in range(a,b+1,2):
#     print(i, end= " ")

# #3
# n = int(input())
# for i in range(10,0, -1):
#   print(f"{i}**{n}={i**n}", end="; ")


# #4
# a = int(input())
# b = int(input())
# n = 0
# for i in range(a,b+1):
#   n = n + i**2
# print(n)

# #5
# n = int(input())
# N = 1
# for i in range(1,n+1):
#   N = N * i
# print(N)


# n = int(input())
# N = 0
# if n >= 2:
#   for i in range(2,n+1):
#     N = N + (i - 1)* i
#     if i == n:
#       print(f"{i-1}x{i}", end="=")
#     else:  
#       print(f"{i-1}x{i}", end="+")
#   print(N)
# else:
#     print("No")


# n = int(input())
# for i in range(0,n+1):
#   if i%2 == 0:
#     print(f"{i}", end=" ")
#   else:
#     print(f"-{i}", end=" ")


# n = int(input())
# for i in range(1,n+1):
#   print(i**i, end=" ")


# n = int(input())
# for i in range(1,n+1):
#   for j in range(i):
#     print("*", end=" ")
#   print()


# n = int(input())
# for i in range(n,0, -1):
#   for j in range(i):
#     print("*", end=" ")
#   print()


# n = int(input())
# for i in range(n,0, -1):
#   for _ in range(n-i):
#      print("  ",end="")
#   for _ in range(i):
#       print("*", end=" ")
#   print()


# n = int(input())
# for i in range(1,n+1):
#   for _ in range(n-i):
#     print(" ", end="")
#   for j in range(i):
#     print("*", end=" ")
#   print()
