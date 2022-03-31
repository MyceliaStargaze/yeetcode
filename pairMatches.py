# With 2 infinite number generators, A and B, we're looking for matching pairs of numbers, given 2 initial values

# Define initial A and B values; 40 million iteration limit; total # of matches
iterationLimit = 40000000
iniA = 420; iniB = 80085
global totMatch; totMatch = 0

# Construct generator A: take #, multiply by 16807, modulo by 2147483647, remainder is returned
def genA(remainderA):
    retA = (remainderA * 16807) % 2147483647
    return retA

# Construct generator B: take #, multiply by 48271, modulo by 2147483647, remainder is returned
def genB(remainderB):
    retB = (remainderB * 48271) % 2147483647
    return retB

# Cast given # in binary 
def binaryMe(numX):
    binaryX = format(numX, 'b')
    return binaryX

# Cast binary representation of nums as strings, compare last 16 'digits', if true, increment totMatch by 1
def isEqual(numA, numB):
    global totMatch
    binaryStringA = str(binaryMe(numA))
    binaryStringB = str(binaryMe(numB))
    truncA = binaryStringA[-16:]
    truncB = binaryStringB[-16:]
    if truncA == truncB:
        totMatch += 1

# do this 40 million times lmao
A1 = iniA; B1 = iniB
for i in range(1, iterationLimit):
    A2 = genA(A1); B2 = genB(B1)
    isEqual(A2, B2)
    #print(A2, '\n', B2)
    A1 = A2; B1 = B2

# Return totMatch
print("The total numer of least significant pair matches is equal to: ", totMatch)
