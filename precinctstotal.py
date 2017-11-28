#rows represent the candidates
#columns represent the precincts
votes= [[300,200,100],[400,200,100],[345,234,654],[100,324,190]]
highest=0
winner=0
for row in range (4):
   total=0
   for col in range (3):
       total += votes[row][col]
       if total>=highest:
           highest=total
           winner=row+1
   print "candidate" + str(row + 1) + " total is " + str(total)
print "The winner is canidate",winner,"with",highest,"votes"
