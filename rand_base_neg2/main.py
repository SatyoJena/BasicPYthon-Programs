'''
an attempt to generate predetermined random numbers. 
by translating to -2 base from base 2 of base 10  nums, 
then retranslating it back to base 10

But got a cool fractal instead :))
'''
import matplotlib.pyplot as pl
def decimal_to_bin(a:int) -> str :
    ans =''
    while (a>=1):
        ans += str(a%2)
        a//=2 
    return ans[::-1]

def bin_to_neg2_decimal(a:str) -> int :
    ans =0
    n= len(a)
    for i in range(1,n) :
        ans += ((-2)**i)*(int(a[n-1-i]))
    return ans

x = [i for i in range(0,100000)]
y = [bin_to_neg2_decimal(decimal_to_bin(i)) for i in x]

pl.plot(x,y)
pl.show()