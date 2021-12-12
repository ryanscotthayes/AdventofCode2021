file_path = 'D8/input.txt'
#file_path = 'D8/test.txt'

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

def solveBandD(line,cipherKey):
    for i in range(0,len(line)):
        if len(line[i]) == 5: #must be either a 2 or a 3 or a 5
            if (cipherKey['c'][0] in line[i]) & (cipherKey['c'][1] in line[i]): # Now must be a 3
                for letter in line[i]:
                    if letter in cipherKey['d']:
                        cipherKey['d'] = letter
                        break
                    else: 
                        pass
            else:
                pass
    for i in cipherKey['b']:
        if i == cipherKey['d']:
            pass
        else:
            cipherKey['b'] = i
            break

    return cipherKey


def solveCandF(line,cipherKey):
    for i in range(0,len(line)):
        if len(line[i]) == 5: #must be either a 2 or a 3 or a 5
            if cipherKey['b'] in line[i]: # must be a 5
                for letter in line[i]:
                    if letter in cipherKey['f']:
                        cipherKey['f'] = letter
                        break
                    else: 
                        pass
            else:
                pass
    for i in cipherKey['c']:
        if i == cipherKey['f']:
            pass
        else:
            cipherKey['c'] = i
            break
    return cipherKey

def Decode(cipherKey:dict, text:str):
    new_string = ''
    for letter in range(0,len(text)):
        if text[letter] == cipherKey['a']:
            new_string += 'a'
        elif text[letter] == cipherKey['b']:
            new_string += 'b'
        elif text[letter] == cipherKey['c']:
            new_string += 'c'
        elif text[letter] == cipherKey['d']:
            new_string += 'd'
        elif text[letter] == cipherKey['e']:
            new_string += 'e'
        elif text[letter] == cipherKey['f']:
            new_string += 'f'
        elif text[letter] == cipherKey['g']:
            new_string += 'g'
        else:
            new_string += 'z'
   
    return new_string

def signalToAscii(text:str):
    if text == 'abcefg':
        ascii = '0'
    elif text == 'cf':
        ascii = '1'
    elif text == 'acdeg':
        ascii = '2'
    elif text == 'acdfg':
        ascii = '3'
    elif text == 'bcdf':
        ascii = '4'
    elif text == 'abdfg':
        ascii = '5'
    elif text == 'abdefg':
        ascii = '6'
    elif text == 'acf':
        ascii = '7'
    elif text == 'abcdefg':
        ascii = '8'
    elif text == 'abcdfg':
        ascii = '9'
    else: 
        ascii = '-1'
    return ascii

data = text.split('\n')

right_side = []
for i in range(0,len(data)):
    right_side.append(data[i].split(' | ')[1].split(' '))

full_data = []
decodedString = []
list_of_solutions = []
for i in range(0,len(data)):
    full_data.append(data[i].split(' '))
for i in range(0,len(full_data)):
    solution = ''
    full_data[i].remove('|')
    full_data[i] = sortStrings(full_data[i])
    cipherKey = startCipherKey(full_data[i])
    cipherKey = solveEandG(full_data[i],cipherKey)
    cipherKey = solveBandD(full_data[i],cipherKey)
    cipherKey = solveCandF(full_data[i],cipherKey)
    for j in range(0,len(right_side[i])):
        right_side[i][j] = Decode(cipherKey,right_side[i][j])
    right_side[i] = sortStrings(right_side[i])
    for k in range(0,len(right_side[i])):
        solution += signalToAscii(right_side[i][k])
    list_of_solutions.append(int(solution))

pt2_answer = 0
for i in list_of_solutions:
    pt2_answer += i
        
print('Part 2 answer: ' , pt2_answer)

