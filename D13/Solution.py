#file_path = 'D13/test.txt'
file_path = 'D13/input.txt'

with open(file_path) as f:
    splitInstructions = f.read().split('\n\n')

#print(splitInstructions)
def cleanData(text):
    dataArray = splitInstructions[0].split('\n')
    instructionArray = splitInstructions[1].split('\n')
    for i in range(0,len(dataArray)):
        dataArray[i] = dataArray[i].split(',')
    for i in range(0,len(dataArray)):
        for j in range(0,len(dataArray[i])):
            dataArray[i][j] = int(dataArray[i][j])
    foldList = []
    for i in range(0,len(instructionArray)):
        foldList.append(instructionArray[i][11:])
    return dataArray,foldList


dataArray,foldList = cleanData(splitInstructions)
maxX = 0
maxY = 0

for n in range(0,len(dataArray)):
    if dataArray[n][0] > maxX:
        maxX = dataArray[n][0]
    if dataArray[n][1] > maxY:
        maxY = dataArray[n][1]
for n in range(0,len(foldList)):
    if foldList[n][0] == 'x':
        if int(foldList[n][2:])*2 > maxX:
            maxX = int(foldList[n][2:])*2
    else:
        if int(foldList[n][2:])*2 > maxY:
            maxY = int(foldList[n][2:])*2
    

plotArray = [] # Holds point grid
for i in range(0,maxY+1):
    plotArray.append([])
    for j in range(0,maxX+1):
        plotArray[i].append(' ')

for k in range(0,len(dataArray)): #Initial Plotting happening here
    plotArray[dataArray[k][1]][dataArray[k][0]] = '█'

for i in range(0,len(foldList)):
    if foldList[i][0] == 'x':
        #Vertical Line
        value = int(foldList[i][2:])
        for j in range(0,len(plotArray)):
            plotArray[j][value] = '='

        for k in range(0,len(plotArray)):
            for q in range(0,len(plotArray[k])):
                if plotArray[k][q] == '█':
                    plotArray[k][len(plotArray[k])-q-1] = '█'
        
        new_plotArray = []
        for p in range(0,len(plotArray)): ##Drop used side of fold
            new_plotArray.append(plotArray[p][0:value])
        plotArray = new_plotArray

    if foldList[i][0] == 'y':
        #Horizontal Line
        value = int(foldList[i][2:])
        for j in range(0,len(plotArray[value])):
            plotArray[value][j] = '='
        
        for k in range(value,len(plotArray)): ##Fold step and rewrite
            for q in range(0,len(plotArray[k])):
                if plotArray[k][q] == '█':
                    plotArray[len(plotArray)-k-1][q] = '█'
        new_plotArray = []
        for k in range(0,value): ##Drop used side of fold
            new_plotArray.append(plotArray[k])
        plotArray = new_plotArray

        pass
    if i == 0:
        solution = 0
        for row in range(0,len(plotArray)):
            for column in range(0,len(plotArray[row])):
                if plotArray[row][column] =='█':
                    solution += 1
        print('Part 1: ', solution)
        


print('Part 2: ')
for k in plotArray:
    print("".join(k))

