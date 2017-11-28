def reverseDatabase(database):
    reverse={}
    for key,value in database.items():
        reverse[value]=key
    return reverse

if __name__=="__main__":
    phonenumbers={}
    fileobj=file("Phonenumbers")
    line=fileobj.readline()
    while line:
        alist=line.split()
        phonenumbers[alist[0]]=alist[1]
        line=fileobj.readline()
    reversephone=reverseDatabase(phonenumbers)
        
