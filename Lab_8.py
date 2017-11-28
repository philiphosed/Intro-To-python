a=file("numbers.txt",'r')
line=a.readline()
while line:
    linetotal=line.split()
    for i in len(linetotal):
        tot=0
        tot+=float(total[i])
    average=sum(tot)/len(linetotal)
    print average
    line=a.readline()
