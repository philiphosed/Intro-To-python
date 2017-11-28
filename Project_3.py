# -*- coding: utf-8 -*-
#David Philiphose
#Program #3
#Judy Etchison
#CSCI 1300
#2/26/16
def getData(URL):
    import urllib
    address = URL
    connection = urllib.urlopen(address)  # opens a connection to the above URL
    pageStr = connection.read() #reads the entire file and returns data as a string
    connection.close()  #closes connection
    print "This is the contents of the page"
    print pageStr
    return pageStr
def annualGrowthRate(gdpList,year,quarter)#function that calculates the annual growth rate
    for i in range(0,len(gdplist),2):
        try:
            datelist=gdp[i].split('-') #seperates string into massive list
            if datelist[0]==year: #finds year and quarter for gdplist and 
                try:
                    if quarter==1:
                        gdp1=gdplist[i+1]
                        annualgrowthrate = (gdp1[i] –  gdp1[i-8])/gdp1[i-8]
                    elif quarter==2:
                        gdp1=gdplist[i+3]
                        annualgrowthrate = (gdp1[i] –  gdp1[i-8])/gdp1[i-8]                
                    elif quarter==3:   
                        gdp1=gdplist[i+5]
                        annualgrowthrate = (gdp1[i] –  gdp1[i-8])/gdp1[i-8]
                    else quarter==4:
                        gdp1=gdplist[i+7]
                        annualgrowthrate = (gdp1[i] –  gdp1[i-8])/gdp1[i-8]
                except ValueError:
                    print 'Invalid Quarter'
        except ValueError:
            print 'Invalid Year'
    print 'For',year,', the annual growth rate for quarter',quarter,'was',annualgrowthrate
           

            
                
                    
URL=raw_input('Enter URL for the file you want to open:') 
data=getData(URL)#uses functions
datalist=data.split()
info=raw_input('Enter a year/quarter to analyze separated by spaces:')
infolist=info.split()
aGR=annualGrowthRate(datalist,infolist[0],infolist[1])#uses function
print 'The years in which there was a recession are'
for i in range(0,len(gdplist),3):
    recesslist=[]
    if gdplist[i-8]>gdplist[i]:
        recesslist.append(gpdlist[i])
    print 'Years in recession are','\n',recesslist
        











    



