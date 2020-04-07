a=1
b=1
c=0
ctr=0
while len(str(c)) !=1000:
    c=a+b
    a=b
    b=c
    ctr+=1

print(c)
print(ctr+2)
