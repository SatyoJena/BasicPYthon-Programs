n = 4000000  # 4 million
a = 0
b = 1
s = 0
c = 1
while(c<n):
	c = a+b
	a=b
	b=c
	if c%2==0:
		s += c
	print(c,"\t",s)
