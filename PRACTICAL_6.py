"""Write a python program that accepts a string from user and perform following string 
operations- i. Calculate length of string ii. String reversal iii. Equality check of two 
strings iii. Check palindrome ii. Check substring"""

str1=input("Enter a string: ")
str2=input("Enter another string: ")
#1
length1=len(str1)
length2=len(str2)
print("The length of string is:",length1)
print("The length of string is:",length2)
#2
reverse1=str1[::-1]
reverse2=str2[::-1]
print("The reverse of the string is:",reverse1)
print("The reverse of the string is:",reverse2)
#3
if str1==str2:
    print("The strings are equal.")
else:
    print("The string are not equal")
#4
if str1==reverse1:
    print("The given string",str1.upper(),"is a palindrome")
else:
    print("The given string",str1.upper(),"is not a palindrome.")
if str2==reverse2:
    print("The given string",str2.upper(),"is a palindrome.")
else:
    print("The given string",str2.upper(),"is not a palindrome.")
#5
if str1 in str2:
    print("String ONE is a substring of string TWO")
elif str2 in str1:
    print("String TWO is a sbstring of String ONE")
else:
    print("The given strings are not substrings of one another.")                                