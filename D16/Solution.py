#file_path = 'D16/input.txt'
file_path = 'D16/test1.txt'
#file_path = 'D16/test2.txt'
#file_path = 'D16/test3.txt'
#file_path = 'D16/test4.txt'

with open(file_path) as f:
    text = f.read()

print(text)