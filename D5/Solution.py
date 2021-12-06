from collections import Counter
filePath = 'D5/input.txt'
#filePath = 'D5/test.txt'

with open(filePath) as f:
    text = f.read()


def cleanData():
    '''
    Function automagically resets input data so operations can be done in place as needed.
    '''
    dataRaw = text.split('\n')
    dataString = []
    for i in dataRaw:
        a = i.split(' -> ')
        innerLoopPreserve = []
        for j in a:
            b = j.split(',')
            innerLoopPreserve.append(b)
        dataString.append(innerLoopPreserve)

    data = []
    for i in range(0,len(dataString)):
        outerLoopPreserve = []
        for j in range(0,len(dataString[i])):
            middleLoopPreserve = []
            for k in range(0,len(dataString[i][j])):
                middleLoopPreserve.append(int(dataString[i][j][k]))
            outerLoopPreserve.append(middleLoopPreserve)
        data.append(outerLoopPreserve)
    return data

def isVertical(list):
    if list[0][0] == list[1][0]: #If two x coords match
        return True
    elif list[0][1] == list[1][1]: #If two y coords match
        return False
    else:
        return False

def isHorizontal(list):
    if list[0][0] == list[1][0]: #If two x coords match
        return False
    elif list[0][1] == list[1][1]: #If two y coords match
        return True
    else:
        return False

def isDiagonal(list):
    if list[0][0] == list[1][0]: #If two x coords match
        return False
    elif list[0][1] == list[1][1]: #If two y coords match
        return False
    else:
        return True



data = cleanData()
partOneData = [] ##Same as Data but diagonal lines will be removed
for i in range(0,len(data)):
    if isVertical(data[i]) == True:
        partOneData.append(data[i])   
    elif isHorizontal(data[i]): 
        partOneData.append(data[i]) 
    else:
        pass ## All my homies hate diagonal lines on part 1

pointList = []
for i in range(0,len(partOneData)):
    if isVertical(partOneData[i]) == True:
        for j in range(min(partOneData[i][0][1],partOneData[i][1][1]),max(partOneData[i][0][1],partOneData[i][1][1])+1): #for each j in range of min y to max y
            pointList.append('['+str(partOneData[i][0][0])+','+str(j)+']') ##Dedups points within a line

    if isHorizontal(partOneData[i]) == True:
        for j in range(min(partOneData[i][0][0],partOneData[i][1][0]),max(partOneData[i][0][0],partOneData[i][1][0])+1): #for each j in range of min x to max x
            pointList.append('['+str(j)+','+str(partOneData[i][0][1])+']') ##Dedups points within a line
#print(pointList)
pt1Output = Counter(pointList)
pt1OutputFiltered = {x: count for x, count in pt1Output.items() if count >= 2}
print('Part 1: ' + str(len(pt1OutputFiltered)))