def lineOne(n):
    if n == 1:
        lux = [2]
        return lux
    elif n == 2 or n == 3 or n == 5 or n == 6 or n == 7 or n == 8 or n == 9 or n == 0:
        lux = [0, 1, 2]
        return lux
    elif n == 4:
        lux = [0, 2]
        return lux
def lineTwo(n):
    if n == 1 or n == 2 or n == 3 or n == 7:
        lux = [2]
        return lux
    elif n == 4 or n == 8 or n == 9 or n == 0:
        lux = [0, 2]
        return lux
    elif n == 6 or n == 5: 
        lux = [0]
        return lux
def lineThree(n):
    if n == 1 or n == 7:
        lux = [2]
        return lux
    elif n == 2 or n == 3 or n == 4 or n == 5 or n == 6 or n == 8 or n == 9:
        lux = [0, 1, 2]
        return lux
    elif n == 0:
        lux = [0, 2]
        return lux
def lineFour(n):
    if n == 1 or n == 3 or n == 4 or n == 5 or n == 7 or n == 9:
        lux = [2]
        return lux
    elif n == 2:
        lux = [0]
        return lux
    elif n == 6 or n == 8 or n == 0: 
        lux = [0, 2]
        return lux
def lineFive(n):
    if n == 1 or n == 4 or n == 7:
        lux = [2]
        return lux
    elif n == 2 or n == 3 or n == 5 or n == 6 or n == 8 or n == 9 or n == 0:
        lux = [0, 1, 2]
        return lux
    