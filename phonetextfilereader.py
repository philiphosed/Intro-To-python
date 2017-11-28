phonenumbers={}
fileobj=file("Phonenumbers")
line=fileobj.readline()
while line:
    alist=line.split()
    phonenumbers[alist[0]]=alist[1]
    line=fileobj.readline()
print phonenumbers["Josh"]
