try:
    source = file("accounntstuff.txt")
    numlines = numwords = numchars = 0
    line = source.readline()
    total=0
    while line: #read one line at a time. (non-null line is True)
            linelist=line.split()
            total+=float(linelist[2])
            line=source.readline()
    print total
    source.close()
except IOError:
    print "file cannot be opened"
