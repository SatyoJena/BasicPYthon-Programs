a=open('names.txt')
b=a.read()
#but first let me remove " from them
b1=''
for i in b :
    if i=='"' :
        continue
    else:
        b1+=i
        
c=b1.split(',')
c.sort()
n=len(c)
dict1={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,
      'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
sum=0
for i in range(n):
    for j in c[i] :
        sum+=(dict1[j])*(i+1)
    

print(sum)
