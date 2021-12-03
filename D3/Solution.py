with open('D3\\input.txt') as f:
#with open('D3\\test.txt') as f:
    text = f.read()

col_0_cnt = 0
col_1_cnt = 0
col_2_cnt = 0
col_3_cnt = 0
col_4_cnt = 0
col_5_cnt = 0
col_6_cnt = 0
col_7_cnt = 0
col_8_cnt = 0
col_9_cnt = 0
col_10_cnt = 0
col_11_cnt = 0


list = text.split('\n')
for i in range(0,len(list)):
    for j in range(0,len(list[0])):
        if j == 0:
            col_0_cnt += int(list[i][j])
        elif j == 1:
            col_1_cnt += int(list[i][j])
        elif j == 2:
            col_2_cnt += int(list[i][j])
        elif j == 3:
            col_3_cnt += int(list[i][j])
        elif j == 4:
            col_4_cnt += int(list[i][j])
        elif j == 5:
            col_5_cnt += int(list[i][j])
        elif j == 6:
            col_6_cnt += int(list[i][j])
        elif j == 7:
            col_7_cnt += int(list[i][j])
        elif j == 8:
            col_8_cnt += int(list[i][j])
        elif j == 9:
            col_9_cnt += int(list[i][j])
        elif j == 10:
            col_10_cnt += int(list[i][j])
        else:
            col_11_cnt += int(list[i][j])
       
        
def compute(number,length):
    if number > length/2:
        return 1
    else:
        return 0

result_0 = str(compute(col_0_cnt,len(list)))
result_1 = str(compute(col_1_cnt,len(list)))
result_2 = str(compute(col_2_cnt,len(list)))
result_3 = str(compute(col_3_cnt,len(list)))
result_4 = str(compute(col_4_cnt,len(list)))
result_5 = str(compute(col_5_cnt,len(list)))
result_6 = str(compute(col_6_cnt,len(list)))
result_7 = str(compute(col_7_cnt,len(list)))
result_8 = str(compute(col_8_cnt,len(list)))
result_9 = str(compute(col_9_cnt,len(list)))
result_10 = str(compute(col_10_cnt,len(list)))
result_11 = str(compute(col_11_cnt,len(list)))


final_result = result_0+result_1+result_2+result_3+result_4+result_5+result_6+result_7+result_8+result_9+result_10+result_11
inv_final_result = ''

for i in range(0,len(final_result)):
    if int(final_result[i]) == 0:
        inv_final_result += '1'
    else:  
        inv_final_result += '0'

#print(int(final_result,2))
#print(int(inv_final_result,2))
#print('Result = ' + str(int(final_result,2)*int(inv_final_result,2)))



# REFACTOR ALL THIS BULLSHIT^^^^^^




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
print('Oxygen Generator = ' + str(Oxy_Ans))


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
print('CO2 scrubber = ' + str(Co2_ans))
print('Result: '+str(Co2_ans * Oxy_Ans))