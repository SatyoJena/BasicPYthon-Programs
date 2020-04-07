result='y'
while (result=='y'):
    x= input('choose operator +-*/ ___')
    a=int(input ('enter first arguemnt___'))
    b=int (input ('enter second arguement___'))
    if (x=='+'):
        print ('ur result is', a+b)
    elif (x=='-'):
        print ('ur result is', a-b)
    elif (x=="*"):
        print('ur result is', a*b)
    elif (x=='/'):
        print ('dont enter 2nd arguement 0')
        print ('ur quotient is', a/b,'and remainder is',a%b)
    
    else:
        print ('unsupported operation')
    result=input ('continue?... y/n___')
    
        
