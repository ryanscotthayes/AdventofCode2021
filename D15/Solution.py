#file_path = 'D15/test.txt'
file_path = 'D15/input.txt'
from math import floor

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

    part2data = []
    for num in range(0,5):
        for i in range(0,len(data)):
            part2data.append(data[i]+data[i]+data[i]+data[i]+data[i])

    for i in range(0,len(part2data)):
        for j in range(0,len(part2data[i])):
            if part2data[i][j] + floor(j/10) < 10:
                part2data[i][j] += floor(j/10)
            else:
                part2data[i][j] = part2data[i][j] + floor(j/10) - 9

            if part2data[i][j] + floor(i/10) < 10:
                part2data[i][j] += floor(i/10)
            else:
                part2data[i][j] = part2data[i][j] + floor(i/10) - 9
    return part2data

def Solver(data,costArray):
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

def prepPt2Data(data):
    n, m = len(data), len(data[0])
    part2data = [[0] * (5 * m) for _ in range(5 * n)]
    for row in range(5):
        for col in range(5):
            for r in range(n):
                for c in range(m):
                    nr, nc = n * row + r, m * col + c
                    part2data[nr][nc] = data[r][c] + row + col
                    if part2data[nr][nc] > 9:
                        part2data[nr][nc] -= 9
    return part2data

#######################################################

data = cleanData(text)
costArray = createCostArray(data)

part1Solution = 0
for i in range(0,20): 
    '''
    This helps the map settle in since we search from top left to bottom right diagonally. 
    Running it enough times gives the correct answer. Not sure how to programatically determine when to stop.
    So I'll just go overboard I guess. Part 1 settled out after 3 tries
    '''
    costArray = Solver(data,costArray)


for i in range(0,len(costArray)):
    for j in range(0,len(costArray[i])):
        if i == len(costArray)-1 & j == len(costArray[i])-1:
            part1Solution = costArray[i][j]


print('Part 1: ',part1Solution)

#######################################################

data = cleanData(text)
part2data = prepPt2Data(data)

# for i in range(0,len(part2data)):
#     if i%10 == 0:
#         print('-----------------------------------------------')
#     print(part2data[i])
costArray = createCostArray(part2data)

part2Solution = 0
for i in range(0,15): 
    '''
    This helps the map settle in since we search from top left to bottom right diagonally. 
    Running it enough times gives the correct answer. Not sure how to programatically determine when to stop.
    So I'll just go overboard I guess. Part 1 settled out after 3 tries
    '''
    costArray = Solver(part2data,costArray)


for i in range(0,len(costArray)):
    for j in range(0,len(costArray[i])):
        if i == len(costArray)-1 & j == len(costArray[i])-1:
            part2Solution = costArray[i][j]

print('Part 2: ',part2Solution)
