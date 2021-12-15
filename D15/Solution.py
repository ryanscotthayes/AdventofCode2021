#file_path = 'D15/test.txt'
file_path = 'D15/input.txt'

with open(file_path) as f:
    text = f.read().split('\n')
def cleanData(text):
    '''
    Cleans data and prepares so new Data Set can be used for pt1 vs pt2
    '''
    data = []
    for line in text:
        workingData = []
        for letter in line:
            workingData.append(int(letter))
        data.append(workingData)
    return data


def createCostArray(data):
    '''
    Creates the initial Cost array, with everything except first point set to 99999
    '''
    costArray = []
    for i in range(0,len(data)):
        costArray.append([])
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            if (i == 0) & (j == 0):
                costArray[i].append(0)
            else:
                costArray[i].append(99998)
    return costArray

def findMinNeighborsCost(costArray,xcoord,ycoord):
    costUp = 999999
    costDown = 999999
    costLeft = 999999
    costRight = 999999
    
    if ycoord-1 >=0:
        costUp = costArray[ycoord-1][xcoord]
    if ycoord+1 < len(costArray):
        costDown = costArray[ycoord+1][xcoord]
    if xcoord-1 >=0:
        costLeft = costArray[ycoord][xcoord-1]
    if xcoord+1 < len(costArray[ycoord]):
        costRight = costArray[ycoord][xcoord+1]

    
    return min(costUp,costDown,costLeft,costRight)

data = cleanData(text)
costArray = createCostArray(data)

def Part1(data,costArray):
    working_queue = [[0,0]]
    while len(working_queue) > 0:
        xcoord = working_queue[0][0]
        ycoord = working_queue[0][1]
        if (xcoord == 0) & (ycoord == 0):
            costToGetHere = -1*data[ycoord][xcoord]
        else:
            costToGetHere = findMinNeighborsCost(costArray,xcoord,ycoord)
        costArray[ycoord][xcoord] = costToGetHere + data[ycoord][xcoord]
        try:
            if [xcoord,ycoord+1] not in working_queue:
                if (xcoord <= len(costArray[0])) & (ycoord+1 <= len(costArray)-1):
                    working_queue.append([xcoord,ycoord+1])
        except: pass
        try:
            if [xcoord+1,ycoord] not in working_queue:
                if (xcoord+1 <= len(costArray[0])-1) & (ycoord <= len(costArray)):
                    working_queue.append([xcoord+1,ycoord])
        except: pass
        del working_queue[0]
    return costArray

part1Solution = 0
costArray = Part1(data,costArray)
new_costArray = Part1(data,costArray)
for i in range(0,len(new_costArray)):
    for j in range(0,len(new_costArray[i])):
        if i == len(new_costArray)-1 & j == len(new_costArray[i])-1:
            part1Solution = new_costArray[i][j]

print('Part 1: ',part1Solution)

for i in new_costArray:
    print(i)