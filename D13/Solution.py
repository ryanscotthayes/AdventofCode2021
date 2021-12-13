file_path = 'D13/test.txt'
#file_path = 'D13/input.txt'

with open(file_path) as f:
    splitInstructions = f.read().split('\n\n')

#print(splitInstructions)

dataArray = splitInstructions[0].split('\n')
instructionArray = splitInstructions[1].split('\n')

print(dataArray)
print(instructionArray)


