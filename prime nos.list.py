#prime numbers list
import time
l=[2]
import math 
a=time.clock()
for i in range(3,1000000):#a million 
    flag=1
    for j in range(math.floor(len(l)**.5)) :
        flag=flag*(i%l[j])
    if flag :
        l.append(i)
b=time.clock()
print(b-a)
