from AutoPolicy import AutoPolicy
from InsuranceExpense import InsuranceExpense
b=300.00
a=[]
for i in range(1):
    c=AutoPolicy("My Car",011100,b,207415)
    d=Insurance("My Life",4/7/16,b,994102)
    a.append(c)
    a.append(d)
    b+=100.00
for i len(a):
    print a[i] #This illistrates polymorphism in that it is a taking two distinct classes with different attributes and methods, and putting them in practical use with one another and using the same command on them.
