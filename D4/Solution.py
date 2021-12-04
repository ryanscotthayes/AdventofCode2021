import numpy as np
filePath = 'D4/input.txt'
#filePath = 'D4/test.txt'

with open(filePath) as f:
    text = f.read()


###########################################
## Data Cleaning
###########################################


data = text.split('\n\n')

bingoCallOrderList = data[0].split(',')

def cleanSlateBingoCards():
    '''
    I do a lot of operations in place, and instead of figuring out a better way to do 
    this, I'm just gonna reset the bingo cards from the text after Part 1, before Part 2.
     “¯\_(ツ)_/¯“
    '''

    bingoCardsRaw = data[1:]
    bingoCardRowList = []
    for i in range(0, len(bingoCardsRaw)):
        bingoCardRowList.append(bingoCardsRaw[i].split('\n'))

    bingoCards = []
    for j in range(0,len(bingoCardRowList)):
        workingRowList = []
        for k in range(0,len(bingoCardRowList[j])):
            workingRowList.append(bingoCardRowList[j][k].split(' '))
        bingoCards.append(workingRowList)

    #At this step, there are empty string subarrays that still exist, removing them below

    for i in range(0,len(bingoCards)):
        for j in range(0,len(bingoCards[i])):
            for k in bingoCards[i][j]:
                if k == '':
                    bingoCards[i][j].remove(k)
    return bingoCards

bingoCards = cleanSlateBingoCards() #Initially infile Bingo Card Data


###########################################
## Defining Functions
###########################################

def markBingoCard(card,numberCalled,numberToMark):
    for row in card:
        for i in range(0,len(row)):
            if row[i] == numberCalled:
                row[i] = numberToMark
    #No Return Value, do the operation in place

def validateHorizontal(card):
    for row in card:
        row_counter = 0
        for item in row:
            if item == '-1':
                row_counter += 1
        if row_counter == len(row):
            return True
        else:
            pass
    return False

def validateVertical(card):
    transposedCard = np.transpose(card)
    for row in transposedCard: # LOL copied this exact thing from the horizontal portion just with a transposed card.Ezpz.
        row_counter = 0
        for item in row:
            if item == '-1':
                row_counter += 1
        if row_counter == len(row):
            return True
        else:
            pass
    return False

def validateBingoCard(card):
    horizontalVal = validateHorizontal(card)
    verticalVal = validateVertical(card)
    if horizontalVal == True or verticalVal == True: ##Somewhat superfluous but easier to read
        return 1 #Break, card has won
    else:
        return 0




###########################################
## Main Loop for Part 1
###########################################
breakCode = 0 # Break out of outer loops and store value called when broken

for a in range(0,len(bingoCallOrderList)): ##For each number that is called in the list
    for i in range(0,len(bingoCards)): ##For each card that's playing
        if breakCode != 0: #Winning number found
            break

        markBingoCard(bingoCards[i],bingoCallOrderList[a],'-1')
        if validateBingoCard(bingoCards[i]) == 1:
            solution = bingoCards[i]
            breakCode = bingoCallOrderList[a] #Set value of winning number to break code to get out of outer loops & store
            break
    

markBingoCard(solution,'-1','0') ## Now set the marked parts of the solution card to 0's to prep for summing.
sumOfCard = 0
for row in solution:
    for item in row:
        sumOfCard += int(item)

print('Solution 1: '+ str(int(sumOfCard) * int(breakCode)))


###########################################
## Main Loop for Part 2
###########################################



bingoCards = cleanSlateBingoCards() #Reset Bingo Card Data

numberSolved = 0
for a in range(0,len(bingoCallOrderList)): ##For each number that is called in the list

    numberSolved = 0 #Reset amount of Solved because we validate every card every time
     
    for i in range(0,len(bingoCards)): ##For each card that's playing
        markBingoCard(bingoCards[i],bingoCallOrderList[a],'-1')
        if validateBingoCard(bingoCards[i]) == 1:
            numberSolved += 1
    if len(bingoCards) - numberSolved == 0: #Number of remaining puzzles <= 1
        breakCode = bingoCallOrderList[a] #There was a bug here wher e I set 'breakCode = a' instead of the actual number called. 
                                    #In the sample file the bug didn't show up but in the real file it did. Wasted 1.5 hours here
        break

bingoCards = cleanSlateBingoCards() #A bug not doing this down here wasted me an hour

for a in range(0,len(bingoCallOrderList)):
    if bingoCallOrderList[a] == breakCode:
        break
    for i in range(0,len(bingoCards)): #Do initial loop again up until break code ##For each card that's playing
        markBingoCard(bingoCards[i],bingoCallOrderList[a],'-1')

#Now to find that bad card
for i in range(0,len(bingoCards)):
    if validateBingoCard(bingoCards[i]) != 1:
        PT2SOLUTIONCARD = bingoCards[i]



markBingoCard(PT2SOLUTIONCARD,breakCode,'0') # We had to find the card by looking for the last. Then you have to do one more iteration as per the prompt

markBingoCard(PT2SOLUTIONCARD,'-1','0')
sumOfCard = 0
for row in PT2SOLUTIONCARD:
    for item in row:
        sumOfCard += int(item)
print('Solution 2: '+ str(int(sumOfCard) * int(breakCode)))