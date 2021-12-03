with open('D3\\input.txt') as f:
#with open('D3\\test.txt') as f:
    text = f.read()
num_1 = 0
answer = ''
list = text.split('\n')
for j in range(0,len(list[0])):
    for i in range(0,len(list)):
        num_1 += int(list[i][j])
    
    if num_1 >= len(list)/2:
        answer += '1'
    else:
        answer += '0'
    num_1 = 0

gamma = answer
epsilon = ''

for i in answer:
    if i == '0':
        epsilon +='1'
    else:
        epsilon +='0'

print(gamma)
print(epsilon)
print('Answer 1: ' + str(int(gamma,2)*int(epsilon,2)))


###############################################
## Part 2 #####################################
###############################################


dataset = list

def filter_dataset(dataset, str_filter_condition, num_position):
    filtered = []
    for i in range(0,len(dataset)):
        if dataset[i][num_position] == str_filter_condition:
            filtered.append(dataset[i])
        else:
            pass
    return filtered




counter = 0
counter_array = []
filter_cond = '0'
for j in range(0,len(dataset[0])):
    for i in range(0,len(dataset)):
        counter += int(dataset[i][j])
    counter_array.append(counter)
    if counter >= len(dataset)/2:
        filter_cond = '1'
    else:
        filter_cond = '0'
    dataset = filter_dataset(dataset,filter_cond,j)
    counter = 0
Oxy_Ans = int(dataset[0],2)



##CO2 Starts here


dataset = list
counter = 0
counter_inv = 0
counter_array = []
filter_cond = '0'
for j in range(0,len(dataset[0])):
    if len(dataset) == 1:
        break
    for i in range(0,len(dataset)):
        counter += int(dataset[i][j])
        counter_inv = len(dataset) - counter
    counter_array.append(counter)
    if counter_inv > len(dataset)/2:
        filter_cond = '1'
    else:
        filter_cond = '0'
    dataset = filter_dataset(dataset,filter_cond,j)
    counter = 0
    counter_inv = 0


Co2_ans = int(dataset[0],2)

# print('Oxygen Generator = ' + str(Oxy_Ans))
# print('CO2 scrubber = ' + str(Co2_ans))
# print('Result: '+str(Co2_ans * Oxy_Ans))