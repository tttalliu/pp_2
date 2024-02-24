#task1
def my_function():
    grams = int(input())
    ounces = 28.3495231 * grams
    print(ounces)
my_function()

#task2
def temp():
    F = int(input())
    C = (5 / 9) * (F - 32)
    print(C)
temp()

#task3
def solve(numheads, numlegs):
    for rab in range(numheads):
        chick = numheads - rab
        if 4 * rab + 2 * chick == numlegs:
            return rab, chick
numheads = 35
numlegs = 94
f = solve(numheads, numlegs)
print(f[0])
print(f[1])

#task4
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def filter_primes(numbers):
    primes = []
    for n in numbers:
        if is_prime(n):
            primes.append(n)
    return primes
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_numbers = filter_primes(numbers)
print(prime_numbers)

#task5
from itertools import permutations
def print_permutations():
    my_str = input()
    for p in permutations(my_str):
        print("".join(p))
print_permutations()

#task6
def reverse_words(my_str):
    words = my_str.split()
    reversed_str = ""
    for i in range(len(words) - 1, -1, -1):
        reversed_str += words[i] + " "
    return reversed_str.strip()
my_str = input()
reversed_str = reverse_words(my_str)
print(reversed_str)

#task7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#task8
def spy_game(nums):
    count_0 = 0
    count_7 = 0
    for num in nums:
        if num == 0 and count_7 == 0:
            count_0 += 1
        elif num == 0 and count_7 == 1:
            count_0 += 1
        elif num == 7 and count_0 >= 2:
            count_7 += 1
    if count_0 >= 2 and count_7 >= 1:
        return True
    else:
        return False
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

#task9
import math
def volume():
    r = int(input())
    v = (4 / 3) * math.pi * pow(r, 3)
    print(v)
volume()

#task10
def unique_elements(first_list):
    r_list=[]
    for i in first_list:
        if i not in r_list:
            r_list.append(i)
    return r_list
first_list=[1, 2, 3, 3, 4, 5, 5, 6, 7, 7]
r_list=unique_elements(first_list)
print(r_list)   

#task11
def is_palindrome(my_str):
    reversed_str=''
    for char in my_str:
        reversed_str=char+reversed_str
    return reversed_str==my_str
print(is_palindrome("madam"))

#task12
def histogram(my_list):
    for num in my_list:
        print('*'*num)
histogram([4,9,7])

#task13
import random
def guess_the_number():
    sec_num=random.randint(1,20)
    print("Hello! What is your name?")
    name=input()
    print("Well, ",name,", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    count=0
    while True:
        n=int(input())
        count+=1
        if n<sec_num:
            print("Your guess is too low.")
            print("Take a guess.")
        elif n>sec_num:
            print("Your guess is too high.")
            print("Take a guess.")
        else:
            print("Good job, ",name,"! You guessed my number in ",count," guesses!")
guess_the_number()