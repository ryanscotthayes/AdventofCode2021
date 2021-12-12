file_path = 'D12/input.txt'
#file_path = 'D12/test.txt'
#file_path = 'D12/test2.txt'

with open(file_path) as f:
    text = f.read().split('\n')

def reset(text):
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


    

    visitedList = [[]]
    return nodeDictionary, data, visitedList, distinctNodes



def Pt1ElectricBungalung(nodeDictionary, currentVertex, visited, visitedlc):
    visited.append(currentVertex)
    if currentVertex.upper() != currentVertex:
        visitedlc.append(currentVertex)
    for vertex in nodeDictionary[currentVertex]:
        if vertex not in visitedlc:
            Pt1ElectricBungalung(nodeDictionary, vertex, visited.copy(), visitedlc.copy())
    visitedList.append(visited)


def Pt2ElectricBoogaloo(nodeDictionary,positionArray,trialNode):
    if positionArray[-1]=="end":
        pt2ReturnArray.add(tuple(positionArray))
        return pt2ReturnArray
    for dictItem in nodeDictionary[positionArray[-1]]:
        if dictItem.upper()!=dictItem:
            if trialNode== "" and dictItem!= "start":
                Pt2ElectricBoogaloo(nodeDictionary,positionArray+[dictItem],dictItem)
                if not dictItem in positionArray:
                    Pt2ElectricBoogaloo(nodeDictionary,positionArray+[dictItem],"")
            elif trialNode==dictItem:
                if positionArray.count(dictItem)==1: 
                        Pt2ElectricBoogaloo(nodeDictionary,positionArray+[dictItem],dictItem)
            else:
                if dictItem not in positionArray:
                    Pt2ElectricBoogaloo(nodeDictionary,positionArray+[dictItem],trialNode)
        else:
            Pt2ElectricBoogaloo(nodeDictionary,positionArray+[dictItem],trialNode)
    return pt2ReturnArray





###################################
# Part 1 
###################################

nodeDictionary,data,visitedList,distinctNodes = reset(text)

Pt1ElectricBungalung(nodeDictionary, 'start', [], [])

visitedList.remove([])
solutionList = []
for i in range(0,len(visitedList)):
    if visitedList[i][-1] == 'end':
        solutionList.append(visitedList[i])
print('Part 1: ', len(solutionList))


###################################
# Part 2 
###################################

nodeDictionary,data,visitedList,distinctNodes = reset(text)

pt2ReturnArray = set()
resultArray = Pt2ElectricBoogaloo(nodeDictionary,["start"],"")

print('Part 2: ', len(resultArray))