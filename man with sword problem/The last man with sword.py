""" 
if at start, there are 1000 men standing
forming a circle,and one man with a sword.
He kills his adjacent man and passes the sword to
man adjacent to his victim.
If this continues till only one man survives,
name the index of last man with sword.
"""
import math
def last_man(x):
	a= (2*x - 2**((math.floor(math.log(x,2)))+1) )+ 1
  # note that this is a self made function by me and my friend Bai (refer image)
  # after solving and analyzing the problem using algorithm
	return a

print(last_man(2))
