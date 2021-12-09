file_path = 'D9/input.txt'
#file_path = 'D9/test.txt'

with open(file_path) as f:
    text = f.read()

def getAdjacentPoints(x_pos,y_pos,full_data):
    return_array = []
    if y_pos-1 != -1: 
        return_array.append(int(full_data[y_pos-1][x_pos]))
    if y_pos+1 < len(full_data): 
        return_array.append(int(full_data[y_pos+1][x_pos]))
    if x_pos-1 != -1: 
        return_array.append(int(full_data[y_pos][x_pos-1]))
    if x_pos+1 < len(full_data[y_pos]): 
        return_array.append(int(full_data[y_pos][x_pos+1]))
    return return_array

data = text.split('\n')
cumbersome = 0
for y_pos in range(0,len(data)):
    for x_pos in range(0,len(data[y_pos])):
        return_array = getAdjacentPoints(x_pos,y_pos,data)
        if int(data[y_pos][x_pos]) < min(return_array):
            cumbersome += int(data[y_pos][x_pos])+1
print('Pt1: ',cumbersome)



###################################################################
###################################################################
###################################################################

def getAdjacentPointCoords(x_pos,y_pos,full_data):
    point_array = []
    if y_pos-1 != -1: 
        point_array.append([x_pos,y_pos-1])
    if y_pos+1 < len(full_data): 
        point_array.append([x_pos,y_pos+1])
    if x_pos-1 != -1: 
        point_array.append([x_pos-1,y_pos])
    if x_pos+1 < len(full_data[y_pos]): 
        point_array.append([x_pos+1,y_pos])
    return point_array

data = text.split('\n')
low_points = []
for y_pos in range(0,len(data)):
    for x_pos in range(0,len(data[y_pos])):
        return_array = getAdjacentPoints(x_pos,y_pos,data)
        if int(data[y_pos][x_pos]) < min(return_array):
            low_points.append([x_pos,y_pos])

bastionPoints = []
for i in range(0,len(low_points)):
    new_point_array = []
    bastion_existing_points = []
    bastion_existing_points.append(low_points[i])
    point_array = getAdjacentPointCoords(low_points[i][0],low_points[i][1],data)
    for i in range(0,len(point_array)):
        if data[point_array[i][1]][point_array[i][0]] == '9':
            pass
        else:
            new_point_array.append(point_array[i])
    for i in new_point_array:
        bastion_existing_points.append(i)
    bastionPoints.append(bastion_existing_points)

prev_max_bastion_size = 0 
for i in bastionPoints:
    if len(i)> prev_max_bastion_size:
        prev_max_bastion_size = len(i)

max_bastion_size = prev_max_bastion_size + 1 # This is just to start the loop
while max_bastion_size > prev_max_bastion_size:
    prev_max_bastion_size = max_bastion_size
    for i in range(0,len(bastionPoints)):
        for j in range(0,len(bastionPoints[i])):
            next_point_array = getAdjacentPointCoords(bastionPoints[i][j][0],bastionPoints[i][j][1],data)
            # print(bastionPoints[i])
            for k in next_point_array:
                if k in bastionPoints[i]:
                    pass
                else:
                    if data[k[1]][k[0]] != '9':
                        bastionPoints[i].append(k)
                    else: pass
    max_bastion_size = prev_max_bastion_size
    for i in bastionPoints:
        if len(i)> max_bastion_size:
            max_bastion_size = len(i)

bastion_sizes = []
for i in range(0,len(bastionPoints)):
    bastion_sizes.append(len(bastionPoints[i]))

solution = 1
for i in sorted(bastion_sizes)[-3:]:
    solution *= i
print('Pt2: ', solution)
