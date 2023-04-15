x=[]
y=[]
for i in range (100,1000):
    for j in range(100,1000):
        x.append(str(i*j))

for i in x :
    if i == i[::-1] :
        y.append(i)
                     
print(max(y))
#here i got 99999
#obviously,project nayuki is correct but i wanna know where's my mistake



#lets try out the solution from project nayuki,
#simply copy paste,lets see what happens
'''def compute():
	ans = max(i * j
		for i in range(100, 1000)
		for j in range(100, 1000)
		if str(i * j) == str(i * j)[ : : -1])
	return str(ans)
print (compute())'''
#i got  906609
#AND THAT'S RIGHT .WOW.     I WONDER HOW WITHOUT NESTING, HE DID IT?
#PROBABLY TO BE LEARNT IN CLASS XII.

#MAGICALLY , I LEARNT IT IN CLASS XII AFTER ALL.
#Its list comprehension.

