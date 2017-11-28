code=raw_input('Your classification code:') #this starts the program with the classification code
while code!=Q:
    if code==Q:#this is to display a stop or invalid code
        days=0
        bod=0
        eod=0
        miles=0
        price=0
        print 'Summary:'+"\t"+'code:'+"\t"+'days rented:'+"\t"+'Odometer at start and end'+"\t"+'Number of miles driven and price billed',
        print '        '+"\t"+code+"\t"+days+"\t"+bod+','+eod+"\t"+miles+','+price,
    else:
        while code==b: #sets up the budget program
            days=raw_input('Number of days rented:')
            bod=raw_input('Odometer at start of rental(to the tenth mile):')
            eod=raw_input('Odometer at end of rental(to the tenth mile):')
            miles=int(eod)-int(bod)#to find miles driven in time period
            baseC=40
            mileageC=0.25
            price=((int(baseC)*int(days))+(miles*mileageC))
        if code==d: #this sets up daily charge
            days=raw_input('Number of days rented:')
            bod=raw_input('Odometer at start of rental(to the tenth mile):')
            eod=raw_input('Odometer at end of rental(to the tenth mile):')
            miles=int(eod)-int(bod)
            baseC=60
            avg=miles/int(days)
            if avg>(int(days)*100):
                cost=(avg-(int(days)*100))
                mileageC=0.25
                price=((int(baseC)*int(days))+(cost*mileageC))
            else:
                price=((int(baseC)*int(days))
        else code==w: #this sets up weekly charge
            days=raw_input('Number of days rented:')
            bod=raw_input('Odometer at start of rental(to the tenth mile):')
            eod=raw_input('Odometer at end of rental(to the tenth mile):')
            miles=int(eod)-int(bod)
            baseC=190
            weeks=int(days)/7
            weekslarge=int(days)//7
            weekmiles=int(miles)/weeks
            mileageC=0
            if 1500>weekmiles>900: #weekly for between 1500 and 900 miles
                mileageC=mileageC+(100*weekslarge)
                price=mileageC+(baseC*weeks)
            elif weekmiles>1500:
                mileageC=mileageC+(200*weekslarge)
                price=mileageC+((miles-1500)*0.25)  
            else:
                price=baseC*weeks
print 'Summary:'+"\t"+'code:'+"\t"+'days rented:'+"\t"+'Odometer at start and end'+"\t"+'Number of miles driven and price billed',
print '        '+"\t"+code+"\t"+days+"\t"+bod','eod+"\t"+miles','price, #this displays output
