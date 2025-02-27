import math

#1

numbers = input("Enter the list : ").split()
nlist = [int(n) for n in numbers] 
print(math.prod(nlist)) 


#2

s = input("Enter a string : ")
def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return f"Uppers : {upper_count}, Lowers : {lower_count}"
print(count_case(s))

#3

s = input("Enter a string : ")
def isPalindrome(s):
    return s == s[::-1]
if isPalindrome(s):
    print("It is Palindrome!")
else: 
    print("It is not Palindrome.")

#4

import time

def delayed_sqrt(number, miliseconds):
    time.sleep(miliseconds/1000)
    print(f"Square root of {number} after {miliseconds} miliseconds is {math.sqrt(number)}")

num = int(input("Enter the number : "))
ms = int(input("Enter the miliseconds : "))
delayed_sqrt(num, ms)

#5 

def all_true(t):
    return all(t)

n = tuple(input("Enter the tuple: ").split(" ")) 
print(all_true(n))
