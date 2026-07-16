## String practice

# str1 = "Yash is a software engineer"
# for i in range(len(str1) - 1, -1, -1):
#     print(str1[i], end="")

## Palindrome check
# str1 = "ababa"
# str2 = ""
# for i in range(len(str1) - 1, -1, -1):
#     str2 += str1[i]
# print(str2)
# if str1 == str2:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

## Count characters, digits and symbols in a string
# str1 = "P@#yn26at^&i5ve"
# print(type(str1))
# char = 0
# digits = 0
# symbol = 0
# for i in str1:
#     if i.isalpha():
#         char += 1
#     elif i.isdigit():
#         digits += 1
#     else:
#         symbol += 1
# print("Characters: ", char, "Digits: ", digits, "Symbols: ", symbol)

# count_char = 0
# count_digit = 0
# count_symbol = 0
# for ch in str1:
#     if ("A" <= ch <= "Z" or "a" <= ch <= "z"):
#         print(ch, "is a character")
#         count_char += 1
#     elif "0" <= ch <= "9":
#         print(ch, "is a digit")
#         count_digit += 1
#     else:
#         print(ch, "is a symbol")
#         count_symbol += 1
# print("Characters: ", count_char, "Digits: ", count_digit, "Symbols: ", count_symbol)