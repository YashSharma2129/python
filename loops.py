## Range function
# (start, end, step) = 1, 10, 2
# range(1, 10, 2) # 1, 3, 5, 7, 9

## For loop
# a = range(1, 10, 2)
# for i in a:
#     print(i) # 1, 3, 5, 7, 9

# for i in range(1, 10, 1):
#     print(i) # 1, 2, 3, 4, 5, 6, 7, 8, 9

# for i in range(16, 1, -1):
#     print(i) # 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2

# for i in range(-5, -15, -1):
#     print(i) # -5, -6, -7, -8, -9, -10, -11, -12, -13, -14

# for i in range(5, 50, 5):
#     print(i)

# a = "Yash Sharma is a software engineer"
# print(len(a)) # 35
# for i in range(len(a)):
#     print(a[i]) # Y, a, s, h,  , S, h, a, r, m, a

# a = "Yash Sharma is a software engineer"
# for i in a:
#     print(i)

## Accept an integer value from user and print hello that a times
# a = int(input("Give me your integer value: "))
# for i in range(a):
#     print("hello")

## Print numbers from 1 to n
# n = int(input("enter your integer value: "))
# for i in range(1, n + 1):
#     print(i)

## Reverse numbers from n to 1
# n = int(input("enter your integer value: "))
# for i in range(n, 0, -1):
#     print(i)

# number = int(input("Enter your number: "))
# for i in range(1, 11, 1):
#     print(number, "x", i, "=", number * i)

## Print sum of n numbers
# n = int(input(" Enter the number sum upto n: "))
# sum = 0
# for i in range(1, n + 1, 1):
#     sum += i
# print(sum)

# n = int(input(" Enter the factorial number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)

# n = int(input("enter your number : "))
# sum_even = 0
# sum_odd = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sum_even += i
#     else:
#         sum_odd += i
# print("sum of even numbers is: ", sum_even, "sum of odd numbers is: ", sum_odd)

## Print all factors of a number
# n = int(input("Enter your number: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=" ")

# number = int(input("Enter your number: "))
# sum = 0
# for i in range(1, number):
#     if number % i == 0:
#         print(i)
#         sum += i
# if sum == number:
#     print("Perfect number")
# else:
#     print("Not a perfect number")

## Check prime number
# n = int(input("Enter your number: "))
# if n <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")

# for i in range(10, 0, -1):
#     print(i)