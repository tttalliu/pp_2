# task1
def square_num(N):
    for i in range(1, N + 1):
        yield i**2


N = 4
a = square_num(N)
for j in a:
    print(j)


# task2
def even(n):
    for i in range(0, n + 1, 2):
        yield i


n = int(input())
nums = even(n)
print(",".join(map(str, nums)))


# task3
def div_3_4(n):
    for i in range(0, n + 1):
        i_str = str(i)
        dig = sum(map(int, i_str))
        last_dig = int(i_str[-2:])
        if (dig % 3 == 0) and (last_dig % 4 == 0) and (i != 0):
            yield i


n = int(input())
for j in div_3_4(n):
    print(j)


# task4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


a = int(input())
b = int(input())
for j in squares(a, b):
    print(j)

# task5
def squares(a):
    for i in range(a,-1,-1):
        yield i
a=int(input())
for j in squares(a):
    print(j)