def romanNumber(number):
    numbers=[0,1,2,3,4,5,6,7,8,9]
    numerals=[' ','I','II','III','IV','V','VI','VII','VIII','IX']
    for i in range(len((numerals))):
        if number==-1:
            print ''
        elif number==numerals[i]:
            print numerals[i]
            number=raw_input('Enter another integer or enter -1 to terminate:')            
    return numerals[i]        
    
    
