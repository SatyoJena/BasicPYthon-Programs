x=['SATYO','BAI','BISWA','ISWAR']
y=[96,97,85,92]
from matplotlib import pyplot as plt
#plt.barh(x,y)
#plt.show()
y,x=zip(*sorted(zip(y,x)))
plt.barh(x,y)
plt.show()
#conclusion
#horizontal bala thaki deuchanti. x,y anusare first perpendicular graph banei taku khali 90 degrees bulei dekhei deuchanti 
