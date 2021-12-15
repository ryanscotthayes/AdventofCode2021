file_path = 'D15/test.txt'
#file_path = 'D15/input.txt'

with open(file_path) as f:
    text = f.read().split('\n')

print(text)


