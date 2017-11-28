from random import randint
z=raw_input('Welcome to your math tutor program. How many problems would you like to try?:')
b=int(z)
for num in range(b,0,-1):
    x=randint(1,10)
    y=randint(1,10)
    a=int(x+y)
    c=raw_input('What is the answer to this problem '+str(x)+'+'+str(y)+'?')
    if int(c)!=(a):
        print 'That is incorrect. The correct answer is',a
    else:
        print 'That is correct'
    
   
