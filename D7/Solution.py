input_file = 'D7/input.txt'
#input_file = 'D7/test.txt'

with open(input_file) as f:
    text = f.read()

data = text.split(',')
for i in range(0,len(data)):
    data[i] = int(data[i])

diff_list = []
for attempt in range(min(data),max(data)+1):
    try_list = []
    for j in range(0,len(data)):
        try_list.append(abs(data[j]-attempt))
    diff_list.append(try_list)

solution_list = []
for i in diff_list:
    solution_list.append(sum(i))

print('Part 1: ' + str(min(solution_list)))





data = text.split(',')
for i in range(0,len(data)):
    data[i] = int(data[i])

diff_list = []
for attempt in range(min(data),max(data)+1):
    try_list = []
    for j in range(0,len(data)):
        movement = abs(data[j]-attempt)
        move_penalty = 0
        for diff in range(1,movement+1):
            move_penalty += diff
        try_list.append(move_penalty)
    diff_list.append(try_list)

solution_list = []
for i in diff_list:
    solution_list.append(sum(i))

print('Part 2: ' + str(min(solution_list)))