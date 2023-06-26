from ledLines import *
    
def lOnePrinter(n, last): 
    line = lineOne(n)
    ledList = [" "," "," "]
    for i in range(3):
        if i in line:
            ledList[i] = "#"
    if not last: print(f"{ledList[0]}{ledList[1]}{ledList[2]}", end = '  ')
    else: print(f"{ledList[0]}{ledList[1]}{ledList[2]}")
     
    
def lTwoPrinter(n, last):
    
    line = lineTwo(n)
    ledList = [" "," "," "]
    for i in range(3):
        if i in line:
            ledList[i] = "#"
    if not last: print(f"{ledList[0]}{ledList[1]}{ledList[2]}", end = '  ')
    else: print(f"{ledList[0]}{ledList[1]}{ledList[2]}")
    
def lThreePrinter(n, last):
    
    line = lineThree(n)
    ledList = [" "," "," "]
    for i in range(3):
        if i in line:
            ledList[i] = "#"
    if not last: print(f"{ledList[0]}{ledList[1]}{ledList[2]}", end = '  ')
    else: print(f"{ledList[0]}{ledList[1]}{ledList[2]}")
    
def lFourPrinter(n, last):
    
    line = lineFour(n)
    ledList = [" "," "," "]
    for i in range(3):
        if i in line:
            ledList[i] = "#"
    if not last: print(f"{ledList[0]}{ledList[1]}{ledList[2]}", end = '  ')
    else: print(f"{ledList[0]}{ledList[1]}{ledList[2]}")
    
def lFivePrinter(n, last):
    
    line = lineFive(n)
    ledList = [" "," "," "]
    for i in range(3):
        if i in line:
            ledList[i] = "#"
    if not last: print(f"{ledList[0]}{ledList[1]}{ledList[2]}", end = '  ')
    else: print(f"{ledList[0]}{ledList[1]}{ledList[2]}")
    

       
       
def ledPrint(numb):
    
    for n in range(len(numb)):
        ListLast = False
        if n == len(numb) - 1:
            ListLast = True
        lOnePrinter(numb[n], ListLast)
    
    for n in range(len(numb)):
        ListLast = False
        if n == len(numb) - 1:
            ListLast = True
        lTwoPrinter(numb[n], ListLast)
        
    for n in range(len(numb)):
        ListLast = False
        if n == len(numb) - 1:
            ListLast = True
        lThreePrinter(numb[n], ListLast)
        
    for n in range(len(numb)):
        ListLast = False
        if n == len(numb) - 1:
            ListLast = True
        lFourPrinter(numb[n], ListLast)
        
    for n in range(len(numb)):
        ListLast = False
        if n == len(numb) - 1:
            ListLast = True
        lFivePrinter(numb[n], ListLast)
    
       
        
    
def init():
    numb = input('Type a number: ')
    numb = [int(x) for x in str(numb)]
    ledPrint(numb)
       
    
   
    
init()
       
### 
# #
###  
# #   
### 
        
    
    