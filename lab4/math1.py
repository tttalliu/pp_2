#task1
import math
deg=int(input())
rad=(deg/180)*math.pi
print ("{0:.6f}".format(rad))

#task2
h=5
b1=5
b2=6
a=((b1+b2)/2)*h
print(a)

#task3
import math
sides=4
leng=25
a=(math.pow(leng,2)*sides)/(4*math.tan(math.pi/sides))
print(round(a))

#task4
base=5
h=6
a=h*base
print(a)
