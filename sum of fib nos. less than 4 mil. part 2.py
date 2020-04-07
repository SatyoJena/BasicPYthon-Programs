def compute ():
    ans=0
    a=1
    b=2
    while a<4000000:
        if (a%2==0):
            ans+=a
        a,b=b,a+b
    return (ans)
print(compute())

#I GOT ANSWER 4613732.
