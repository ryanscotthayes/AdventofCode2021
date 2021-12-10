file_path = 'D10/input.txt'
#file_path = 'D10/test.txt'

with open(file_path) as f:
    text = f.read()



translator = {
    '(': 'A',
    ')': 'a',
    '[': 'B',
    ']': 'b',
    '{': 'E',
    '}': 'e',
    '<': 'G',
    '>': 'g'
}

asciiToPoint = {
    'a': 3,
    'b': 57,
    'e': 1197,
    'g': 25137
    }


def translate(string_arr):
    new_array = []
    for i in range(0,len(string_arr)):
        new_string = ''
        for j in range(0,len(string_arr[i])):
            new_string += translator[string_arr[i][j]]
        new_array.append(new_string)
    return new_array
        

fault_list = []
data = text.split('\n')
data = translate(data)
for i in range(0,len(data)):
    work_directory = []
    for j in range(0,len(data[i])):
        if data[i][j] == data[i][j].upper(): # Uppercase element
            work_directory.append(data[i][j])
        elif data[i][j].upper() == work_directory[-1]: #implied lowercase and correct orientation
            work_directory.pop()
        else: ## This is corruption
            fault_list.append(data[i][j])
            break

cum_sum = 0
for i in fault_list:
    for j in i:
        cum_sum += asciiToPoint[j]

print('Part 1: ',cum_sum)
            
###########################################################################################
###########################################################################################
###########################################################################################

data = text.split('\n')
data = translate(data)
new_data = data.copy()
solution_bank = []
for i in range(0,len(data)):
    work_directory = []
    for j in range(0,len(data[i])):
        if data[i][j] == data[i][j].upper(): # Uppercase element
            work_directory.append(data[i][j])
        elif data[i][j].upper() == work_directory[-1]: #implied lowercase and correct orientation
            work_directory.pop()
        else: ## This is corruption
            new_data.remove(data[i])
            work_directory.clear()
            break
    solution_bank.append(work_directory)


while [] in solution_bank:
    solution_bank.remove([])

new_bank = []
for i in range(0,len(solution_bank)):
    solution_bank[i].reverse()


newAsciiToPoint = {
    'a': 1,
    'b': 2,
    'e': 3,
    'g': 4
    }


answer = []
for i in solution_bank:
    total_score = 0
    for j in i:
        total_score =  total_score*5 + newAsciiToPoint[j.lower()]
    answer.append(total_score)

answer.sort()
print('Pt2: ',answer[int((len(answer)-1)/2)])
