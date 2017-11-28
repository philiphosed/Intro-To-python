class DessertItem:
    def __init__(self,name,amount):
        self._name=name
        self._amount=amount
    def getName(self):
        return self._name
    def getCost(self):
        return self._total
    def __str__(self):
        print "The name of the item is a",self._name". The amount bought is",self._amount
class Cookie(DessertItem):
    def __init__(self,name,amount):
    def calculateCost(self):
        totalcookie=round(int(self._amount)*(3.99)/12)
        return totalcookie
    def __str__(self):
        display=DessertItem.__str__(self)
        display+="The price per dozen is"
        display+=str(399),"cents"
        return display
class Candy(DessertItem):
    def __init__(self,name,amount):
    def calculateCost(self):
        totalcandy=round(float(self._amount)*89)
        return totalcandy
    def __str__(self):
        display=DessertItem.__str__(self)
        display+="The price per cookie is"
        display+=str(self._pp),"cents"
        return display
class Checkout(Candy,Cookie):
    def __init__(self):
        self._alist=[]
    def readlist(self,dessertlist):
        fileobj=file(dessertlist)
        line=fileobj.readline()
        while line:
            linelist=line.split()
            if linelist[0]==1:
                acookie=Cookie(linelist[1],linelist[2])
                self._alist.append(acookie)
            else:
                acandy=Candy(linelist[1],float(linelist[2]))
                self._alist.append(acandy)
    def displayReceipt(self):
        for i in range(len(self._alist)):
            areceipt=[]
            areceipt.append(self._alist[i].calculateCost)
            print self._alist[i]
        print "Your total cost is:",sum(areceipt),"cents"
    
    
