# print("Hello Yash!")

## variables
# sher="harsh bhaiya"

## Data Types
# a=12
# b=12.5
# c=12/5
# d="Hello Yash"
# e=34j
# f=True

# print(type(a)) #int
# print(type(b)) #float
# print(type(c)) #float
# print(type(d)) #str
# print(type(e)) #complex
# print(type(f)) #bool

## Doc String where paragrpah needed
# """hello this is multilinee"""

## Naming Conventions

# YashSharma="yash" #Pascal Case
# yashSharma="yash" #Camel Case
# yash_sharma="yash" #Snake Case

# a="A"
# print(ord(a)) #ASCII value of A
# A=65
# print(chr(A)) #Character of ASCII value 65

# # String Slicing

# a="Yash"
# print(a[0:4])

# print(a[0:4:2]) #Yh
## start:end:step
# Character:  Y   a   s   h
# Index:      0   1   2   3

# print(a[::]) #Yash


## Data Type Conversion impicit

# a="12"
# a= int(a)
# print(type(a))

# a="12"
# b=int(a)
# print(type(b)) #<class 'str'>


# a=0
# print(bool(a)) #False

## Data Type Conversion explicit

# a=12
# print(12/3) #4.0

## Input Function 

# name= "Yash"
# Age ="21"

# print("Hello my name is", name, "and my age is", Age) #Hello my name is Yash and my age is 21

# input("Hello what is your age") # Garbage value will be stored in variable but not used

# age= int(input("Hello what is your age")) 
# print(type(age)) #str

## Operators

# a=10
# b=20

# print(a+b) #30
# print(a-b) #-10
# print(a*b) #200
# print(a/b) #0.5
# print(b/a) #2.0
# print(b//a) #2 floor division it will replace all decimal values with integer value 
# print(a**b) #100000000000000000000
# print(b%a) #0


## Logical Operators
# print(12!=12 or 12==12 or 10>5) #True
# print (12!=12 and 12==12) #False


## If else statement
# a=12
# if a>10:
#     print("A is greater than 10")   
# else:
#     print("A is less than 10")


# money=int(input("Enter your money: "))

# if money==10:
#     print("You have 10 rupees")
# elif money==20:
#     print("You have 20 rupees")
# elif money==30:
#     print("You have 30 rupees")
# else:
#     print("You have more than 30 rupees")

# a= int(input("Enter first number: "))
# b=int(input("Enter second number: "))

# if(a>b):
#     print("a is greater than b")
# elif(a<b):
#     print("b is greater than a")
# else:
#     print("a is equal to b")

## Range Function 
# (start, end, step) = 1, 10, 2 ## sss
# range(1, 10, 2) #1, 3, 5, 7, 9

## For Loop
# a= range(1, 10, 2)
# for i in a:
#     print(i) #1, 3, 5, 7, 9

# for i in range(1, 10, 1):
#     print(i) #1, 2, 3, 4, 5, 6, 7, 8, 9

# for i in range(16,1,-1):
#     print(i) #16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2

# for i in range(-5,-15,-1):
#     print(i) #-5, -6, -7, -8, -9, -10, -11, -12, -13, -14


# for i in range(5,50,5):
#     print(i)

# a="Yash Sharma is a software engineer"
# print(len(a)) #35
# for i in range(len(a)):
#     print(a[i]) #Y, a, s, h,  , S, h, a, r, m, a

# a= "Yash Sharma is a software engineer"
# for i in a:
#     print(i) 

## Accept an integer value from user and print hello that a times
# a=int(input("Give me your integer value: "))
# for i in range(a):
#     print("hello")

## Print numbers from 1 to n
# n=int(input("enter your integer value: "))
# for i in range(1,n+1):
#     print(i)

## Reverse numbers from n to 1
# n=int(input("enter your integer value: "))
# for i in range(n,0,-1):
#     print(i)

# number=int(input("Enter your number: "))
# for i in range(1,11,1):
#     print(number, "x", i, "=", number*i)

## Print sum of n numbers
# n=int(input(" Enter the number sum upto n: "))
# sum =0
# for i in range(1,n+1,1):
#     sum+=i
# print(sum)   

# n=int(input(" Enter the factorial number: "))
# fact=1
# for i in range(1,n+1):
#     fact *=i
# print(fact)

# n= int(input("enter your number : "))
# sum_even=0;sum_odd=0
# for i in range(1,n+1):
#     if(i%2==0):
#         sum_even+=i
#     else:
#         sum_odd+=i
# print("sum of even numbers is: ", sum_even, "sum of odd numbers is: ", sum_odd)

# ## Print all factors of a number
# n=int(input("Enter your number: "))
# factor=0
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i ,ends=" ")

# number=int(input("Enter your number: "))
# sum=0
# for i in range(1,number):
#     if(number%i == 0 ):
#         print(i)
#         sum+=i
# if(sum==number):
#         print("Perfect number")
# else:
#         print("Not a perfect number")

## Check prime number
# n=int(input("Enter your number: "))
# if(n<=1):
#     print("Not a prime number")
# else:
#     for i in range(2,n):
#         if(n%i==0):
#             print("Not a prime number")
#             break
#     else:
#             print("Prime number")