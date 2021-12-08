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


def decodeCipher(input):
    cipherKey = []
    print(input)
    return 'Not Implemented'



data = text.split('\n')


full_data = []
decodedString = []
for i in range(0,len(data)):
    full_data.append(data[i].split(' '))
for i in range(0,len(full_data)):
    full_data[i].remove('|')
    decodeCipher(full_data[i])


#print(return_data)