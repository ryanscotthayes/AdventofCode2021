#file_path = 'D14/test.txt'
file_path = 'D14/input.txt'

with open(file_path) as f:
    text = f.read().split('\n\n')
def CleanData(text):
    startingPosition = text[0]

    for i in text[1].split('\n'):
        rawInstructions = text[1].split('\n')

    instructions = []
    for j in rawInstructions:
        instructions.append(j.split(' -> '))

    instructionTranslator = {
    }

    for i in range(0,len(instructions)):
        instructionTranslator[instructions[i][0]] = instructions[i][1]
    return instructionTranslator,startingPosition


def insertCharacter (string,position,character):
    return string[0:position] + character + string[position:]


def runIterations(text,numIterations):
    instructionTranslator,startingPosition = CleanData(text)
    for iter in range(0,numIterations):
        toAdd = []
        for character in range(0,len(startingPosition)):
            if character != len(startingPosition)-1:
                if ((startingPosition[character] + startingPosition[character+1]) in instructionTranslator):
                    toAdd.append([character+1,instructionTranslator[startingPosition[character] + startingPosition[character+1]]])

        for i in range(0,len(toAdd)):
            startingPosition = insertCharacter(startingPosition,toAdd[i][0]+i,toAdd[i][1])
        
    result = Counter(startingPosition)
    return result

def runIterationsBetter (text,numIterations):

    rules,data = CleanData(text)
    pairCounts = {}
    for i in range(len(data)-1):
        pair = data[i:i+2]
        
        if not pair in pairCounts:
            pairCounts[pair] = 0
        pairCounts[pair] += 1
  
    for _iteration in range(numIterations):
        newPairCounts = {}
        for pair in pairCounts:
            
            out = rules[pair]
            first = pair[0]+out
            second = out+pair[1]

            if not first in newPairCounts:
                newPairCounts[first] = 0
            if not second in newPairCounts:
                newPairCounts[second] = 0
    
            newPairCounts[first] += pairCounts[pair]
            newPairCounts[second] += pairCounts[pair]
    
        pairCounts = newPairCounts
    
    letterCounts = {}
    for p in pairCounts.keys():
        x = p[0]
        y = p[1]
        v = pairCounts[p]
        
        if not x in letterCounts:
            letterCounts[x] = 0
        if not y in letterCounts:
            letterCounts[y] = 0
        letterCounts[x]+=v
        letterCounts[y]+=v
    
    letterCounts[data[0]]+=1
    letterCounts[data[-1]]+=1

    values = letterCounts.values()
    return int((max(values)-min(values))/2)


result = runIterations(text,10)

print('Pt1: ',max(result.values())-min(result.values()))

print('PT2: ' , runIterationsBetter(text,40))