with open('D2\\input.txt') as f:
    text = f.read()

direction_list = text.split('\n')

def inter_line (lines):
    result = []
    for i in lines:
        result.append(i.split(' '))
    forward = 0
    depth = 0
    for j in result:
        if j[0] == 'forward':
            forward += int(j[1])
        elif j[0] == 'up':
            #up
            depth -= int(j[1])
        else:
            #down
            depth += int(j[1])
    return forward*depth

print('Question 1: ' + str(inter_line(direction_list)))

def inter_line2_electric_boogaloo (lines):
    result = []
    for i in lines:
        result.append(i.split(' '))
    forward = 0
    depth = 0
    aim = 0
    for j in result:
        if j[0] == 'down':
            aim += int(j[1])
        elif j[0] == 'up':
            #up
            aim -= int(j[1])
        else:
            #forward
            forward += int(j[1])
            depth += aim*int(j[1])
    return forward*depth

print('Question 2: ' + str(inter_line2_electric_boogaloo(direction_list)))