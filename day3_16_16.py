try:
    a=file("mydata",'r')
    b=file("newdata",'w')
    source=a.readline()
    while source:
        for character in line:
            if character!="":
                b.write(character)
        source=a.readline()         
    a.close()
    b.close()
except IOError:
    print "File did not open"
