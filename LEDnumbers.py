def ledCreate(n):
    if n == 1:
        lux = [2, 4, 7, 9, 12]
        return lux
    elif n == 2:
        lux = [0, 1, 2, 4, 5, 6, 7, 8, 10, 11, 12]
        return lux
    elif n == 3:
        lux = [0, 1, 2, 4, 5, 6, 7, 9, 10, 11, 12]
        return lux
    elif n == 4:
        lux = [0, 2, 3, 4, 5, 6, 7, 9, 12]
        return lux
    elif n == 5:
        lux = [0, 1, 2, 3, 5, 6, 7, 9, 10, 11, 12]
        return lux
    elif n == 6: 
        lux = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]
        return lux
    elif n == 7:
        lux = [0, 1, 2, 4, 7, 9, 12]
        return lux
    elif n == 8:
        lux = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        return lux
    elif n == 9:
        lux = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]
        return lux
    elif n == 0:
        lux = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]
        return lux
    else:
        lux = []
        return lux
    
def ledConstructor(ledList, ledLux):
    for i in range(len(ledList)):
        if i in ledLux:
            ledList[i] = "#"
    print(f"""
          {ledList[0]}{ledList[1]}{ledList[2]}
          {ledList[3]} {ledList[4]}
          {ledList[5]}{ledList[6]}{ledList[7]}
          {ledList[8]} {ledList[9]}
          {ledList[10]}{ledList[11]}{ledList[12]}""") 
       
def ledPrint(n):
    ledList = [" "," "," "," "," "," "," "," "," "," "," "," "," "]
    ledLux = ledCreate(n)
    ledConstructor(ledList, ledLux)
    
def init():
    numb = input('Type a number: ')
    numb = [int(x) for x in str(numb)]
    for n in range(len(numb)):
       ledPrint(numb[n])
    
    
    
init()
       
### 
# #
###  
# #   
### 
        
    
    