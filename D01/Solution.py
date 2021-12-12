#file_path = 'D1\\test.txt'
file_path = 'D1\\input.txt'

with open(file_path) as f:
    file = f.read()
depth_list = file.split()
solution = 0 #Number of times i>i-1
for i in range(0,len(depth_list)):
    if i==0:
        pass
    else:
        if int(depth_list[i]) > int(depth_list[i-1]):
            solution += 1
        else:
            pass
print('Question 1: ' + str(solution))



rolling_sum = depth_list[2:] # Bank of Rolling sums for us to use later, ignoring the first 2 of elements intentionally
#when you do this style of rolling sum, you will always lose exactly 2 from the legth of the original list since the rolling sum is not computed until the third element.
for i in range(0,len(depth_list)):
    if i >= 2:
        rolling_sum[i-2] = int(depth_list[i])+int(depth_list[i-1])+int(depth_list[i-2]) 
        #Wasn't sure the best way of setting this, but it works. I dont like assigning it to the i-2th element though, that seems very not straightforward.
    else:
        pass

#List of rolling Sums generated
solution_2 = 0 #Number of times i>i-1
for i in range(0,len(rolling_sum)):
    if i==0:
        pass
    else:
        if rolling_sum[i] > rolling_sum[i-1]:
            solution_2 += 1
        else:
            pass
print('Question 2: ' + str(solution_2))