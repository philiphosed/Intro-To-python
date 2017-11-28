#David Philiphose Lab 12
#part 1
fileobj=file("Movies")
line=fileobj.readline()
movies=set()
while line:
    line=line.strip()
    movies.add(line)
for movie in movies:
    print movie

#part 2
listoflists=[['4','5','2'],['9','1'],['8','4','23']]
summation=0
counter=0
for i in len(range(listoflists):
             for m in len(range(listoflists[i]):
                          summation+=int(listoflists[i][m])
                          counter+=counter+1
print "The sum is",summation,"while the average is",summation/counter
