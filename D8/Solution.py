#file_path = 'D8/input.txt'
file_path = 'D8/test.txt'

#0 = length of 6
#1 = length of 2
#2 = length of 5
#3 = length of 5
#4 = length of 4
#5 = length of 5
#6 = length of 6
#7 = length of 3
#8 = length of 7
#9 = length of 6

with open(file_path) as f:
    text = f.read()

data = text.split('\n')

right_side = []
for i in range(0,len(data)):
    right_side.append(data[i].split(' | ')[1].split(' '))

pt1SolutionCounter = 0
for i in range(0,len(right_side)):
    for j in range(0,len(right_side[i])):
        if len(right_side[i][j]) in (2,4,3,7):
            pt1SolutionCounter += 1
        else:
            pass
            #print(right_side[i][j])

print('PT 1 Solution: ' + str(pt1SolutionCounter))


#####################################################################################

def split(word):
    return [char for char in word]

def sortStrings(array):
    for i in range(0,len(array)):
        array[i] = "".join(sorted(array[i]))
    return array


def startCipherKey(line):
    cipherKey = {
        'a': ['a','b','c','d','e','f','g'],
        'b': ['a','b','c','d','e','f','g'],
        'c': ['a','b','c','d','e','f','g'],
        'd': ['a','b','c','d','e','f','g'],
        'e': ['a','b','c','d','e','f','g'],
        'f': ['a','b','c','d','e','f','g'],
        'g': ['a','b','c','d','e','f','g']
    }
    for i in range(0,len(line)):
        if len(line[i]) == 2:
            cipherKey['c'] = split(line[i])
            cipherKey['f'] = split(line[i])
            break
        else:
            pass
    for i in range(0,len(line)):
        if len(line[i]) == 3:
            for j in line[i]:
                if j in cipherKey['c']:
                    pass
                else:
                    cipherKey['a'] = j
            break
        else:
            pass
    for i in range(0,len(line)):
        if len(line[i]) == 4:
            working_list = []
            for j in line[i]:
                if j in cipherKey['c']:
                    pass
                else:
                    working_list.append(j)
            break
        else:
            pass
    cipherKey['b'] = working_list
    cipherKey['d'] = working_list
    working_list = []
    for i in cipherKey['g']:
        if (i in cipherKey['c']) | (i in cipherKey['a']) | (i in cipherKey['b']):
            pass
        else:
            working_list.append(i)
    cipherKey['g'] = working_list
    cipherKey['e'] = working_list
    return cipherKey

def solveEandG(line,cipherKey):
    for i in range(0,len(line)):
        if len(line[i]) == 6: #must be either a 9 or a 6 or a 0
            if (cipherKey['c'][0] in line[i]) & (cipherKey['c'][1] in line[i]) & (cipherKey['d'][0] in line[i]) & (cipherKey['d'][1] in line[i]): 
            # If both options for c exist, as well as only 1 option for d exists, line[i] must be a 9
                for letter in line[i]:
                    if letter not in [cipherKey['a'],cipherKey['b'][0],cipherKey['b'][1],cipherKey['c'][0],cipherKey['c'][1]]:
                        cipherKey['g'] = letter
                    else:
                        pass
            else: # Must be a 6 or 0
                pass
        else:
            pass
    for i in [0,1]:
        if cipherKey['e'][i] == str(cipherKey['g']):
            pass
        else:
            solForE = cipherKey['e'][i]
            cipherKey['e'] = solForE
            break
    return cipherKey

def solveCandF(line,cipherKey):
    return 'Not Implemented'

def solveBandD(line,cipherKey):
    return 'Not Implemented'

data = text.split('\n')

full_data = []
decodedString = []
for i in range(0,len(data)):
    full_data.append(data[i].split(' '))
for i in range(0,len(full_data)):
    full_data[i].remove('|')
    full_data[i] = sortStrings(full_data[i])
    cipherKey = startCipherKey(full_data[i])
    print(solveEandG(full_data[i],cipherKey))

#print(return_data)
