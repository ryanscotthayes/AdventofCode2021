file_path = 'D11/input.txt'
#file_path = 'D11/test.txt'

with open(file_path) as f:
    text = f.read().split('\n')

def reset_data(text):
    data = []
    for i in range(0,len(text)):
        working_list = []
        for j in range(0,len(text[i])):
            working_list.append(int(text[i][j]))
        data.append(working_list)
    return data

def checkForGT9(data):
    greatestNumber = 0
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            if data[i][j] > greatestNumber:
                greatestNumber = data[i][j]
    
    if greatestNumber > 9:
        return True
    else:
        return False


def gameLoopFlashing(data, nrSteps):
    numFlashList = []
    for k in range(0,nrSteps):

        #Increment 1
        for l in range(0,len(data)):
            for q in range(0,len(data[l])):
                data[l][q] += 1

        #9's and flashes loop while checkForGT9(data) == True:
        while (checkForGT9(data) == True):
            for i in range(0,len(data)):
                for j in range(0,len(data[i])):
                    if data[i][j] > 9:
                        if i-1 != -1: 
                            data[i-1][j] += 1
                        if j-1 != -1:    
                            data[i][j-1] += 1
                        if i+1 != 10:
                            data[i+1][j] += 1
                        if j+1 != 10:
                            data[i][j+1] += 1
                        if (i+1 != 10) & (j+1 != 10): #Diagonals
                            data[i+1][j+1] += 1
                        if (i-1 != -1) & (j+1 != 10):
                            data[i-1][j+1] += 1
                        if (i+1 != 10) & (j-1 != -1):
                            data[i+1][j-1] += 1
                        if (i-1 != -1) & (j-1 != -1):
                            data[i-1][j-1] += 1

                        data[i][j] = -1000

        total_flashes = 0
        for row in range(0,len(data)):
            for column in range(0,len(data[row])):
                if data[row][column] < 0:
                    total_flashes +=1
                    data[row][column] = 0
        numFlashList.append(total_flashes)
        
    return numFlashList

data = reset_data(text)
numFlashList = gameLoopFlashing(data,100)
print('Part 1: ',sum(numFlashList))



counter = 1
answer_found = False
while answer_found == False:
    counter +=1
    data = reset_data(text)
    numFlashList = gameLoopFlashing(data,counter)
    if numFlashList[-1] == 100:
        answer_found = True

print('Part 2: ',len(numFlashList))