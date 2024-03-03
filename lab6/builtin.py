#task1
import math
my_list=[1,2,3,4,5]
m=math.prod(my_list)
print(m)

#task2
str="This is the 2ND ex"
upper=0
lower=0
for c in str:
    if c.isupper():
        upper+=1
    if c.islower():
        lower+=1
print(upper,lower)

#task3
def is_palindrome(str):
    reversed_str= "".join(reversed(str))
    if str==reversed_str:
        print("its palindrome")
s="meem"
is_palindrome(s)

#task4
import math
import time

n = int(input())
ms = int(input())
s = ms / 1000
time.sleep(s)
r = math.sqrt(n)
print(f"Square root of {n} after {ms} milliseconds is {r}")

#task5
def all_true(n):
    return all(n)
my_tuple=(1,2,3,4,5)
print(all_true(my_tuple))
