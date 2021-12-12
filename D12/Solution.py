from random import choice
from time import time
file_path = 'D12/input.txt'
#file_path = 'D12/test.txt'
#file_path = 'D12/test2.txt'

with open(file_path) as f:
    text = f.read().split('\n')

def removeDups(data):
    returnList = []
    for i in data:
        if i not in returnList:
            returnList.append(i)
    return returnList

def removeSmallRoomTwice(data):
    returnData = []
    for i in range(0,len(data)):
        appendflag = 1
        lowercaseSeen = []
        returnSublist = []
        for j in range(0,len(data[i])):
            if data[i][j] not in lowercaseSeen:
                returnSublist.append(data[i][j])
                if data[i][j] != data[i][j].upper():
                    lowercaseSeen.append(data[i][j])
            else:
                appendflag = 0
        if appendflag != 0:
            returnData.append(returnSublist)
    return returnData


data = []
for i in text:
    data.append(i.split('-'))


distinctNodes = []

for i in data:
    if i[0] not in distinctNodes:
        distinctNodes.append(i[0])
    if i[1] not in distinctNodes:
        distinctNodes.append(i[1])



nodeDictionary = {}

for i in distinctNodes:
    nodeDictionary[i] = []



for pair in range(0,len(data)):
    nodeDictionary[data[pair][0]].append(data[pair][1])
    nodeDictionary[data[pair][1]].append(data[pair][0])

remove = []
for k in nodeDictionary:
    if 'start' in nodeDictionary[k]:
        nodeDictionary[k].remove('start')
    if len(nodeDictionary[k]) == 1:
        remove.append(k)

nodeDictionary.pop('end')
for i in remove:
    nodeDictionary.pop(i)
    for k in nodeDictionary:
        if i in nodeDictionary[k]:
            nodeDictionary[k].remove(i)


time1 = time()
listOfPaths = []
for i in range(0,10000000): #Arbitrarily large number to make sure random.choice can find all the paths
    path = ['start']
    stringpath = 'start'
    lastItemInPath = path[-1]

    while lastItemInPath != 'end':
        random_choice = choice(nodeDictionary[lastItemInPath])
        path.append(random_choice)
        stringpath += str(','+str(random_choice))
        lastItemInPath = path[-1]
    
    listOfPaths.append(stringpath)

listOfPaths = list(set(listOfPaths))

new_list = []
for i in range(0,len(listOfPaths)):
    new_list.append(listOfPaths[i].split(','))
new_list = removeSmallRoomTwice(new_list)

print('PT1: ',len(new_list))

#print(listOfPaths)
