file_path = 'D6/input.txt'
#file_path = 'D6/test.txt'
with open(file_path) as f:
    text = f.read()

data = text.split(',')
for i in range(0,len(data)):
    data[i] = int(data[i])

num_days = 80

for day in range(0,num_days):
    num_fish_created = 0
    for i in range(0,len(data)):
        if data[i] == 0:
            data[i] = 6
            num_fish_created +=1
        else:
            data[i] = data[i]-1
    
    for i in range(0,num_fish_created):
        data.append(8)
    #print('Day : ', day)

print('Part 1: ' + str(len(data)))


#############################################

data = text.split(',')

num_days = 256
agg_list = list(range(0,9))
for i in range(0,len(agg_list)):
    agg_list[i] = [i,0]


for j in range(0,len(data)):
    for k in range(0,len(agg_list)):
        
        if int(data[j]) == agg_list[k][0]:
            agg_list[k][1] +=1




#print(agg_list)
for day in range(0,num_days):
    for i in range(0,len(agg_list)):
        agg_list[i] = [agg_list[i][0]-1,agg_list[i][1]]
    agg_list.append([8,0])
    
    new_agg_list = []
    for i in range(0,len(agg_list)):
        
        if agg_list[i][0] == -1:
            reproduce_count = agg_list[i][1]
        else:
            new_agg_list.append(agg_list[i])

    for i in range(0,len(new_agg_list)):
        if new_agg_list[i][0] == 6:
            new_agg_list[i][1] += reproduce_count
        elif new_agg_list[i][0] == 8:
            new_agg_list[i][1] += reproduce_count
    #print('Day %2d Finished'%(day+1) + ' ', new_agg_list)
    agg_list = new_agg_list

solution = 0
for i in range(0,len(agg_list)):
    solution += agg_list[i][1]

print(agg_list)
print('Part 2: ' + str(solution))

