def simpleAddIndex(input_path,output_path):
    with open(input_path) as f:
        text = f.read().split('\n')

    with open(output_path,"w") as f:
        for i in range(0,len(text)):
            if i == len(text)-1:
                f.write(str(i)+','+str(text[i]))
            else:
                f.write(str(i)+','+str(text[i]) + '\n')

def D4(input_path,output_path):
    with open(input_path) as f:
        text = f.read().split('\n')

    with open(output_path,"w") as f:
        for i in range(0,len(text)):
            if i == 0:
                for j in range(0,len(text[0].split(','))):
                    f.write(str(i)+',' + str(j)+',' + text[0].split(',')[j] + '\n')
            elif i == len(text)-1:
                try:
                    if str(text[i]).replace('  ',' ')[0] == ' ':
                        text_to_write = str(text[i]).replace('  ',' ')[1:]
                        f.write(str(i)+',' + text_to_write.replace(' ',','))
                    else:
                        text_to_write = str(text[i]).replace('  ',' ')
                        f.write(str(i)+',' + text_to_write.replace(' ',','))
                except:
                    f.write(str(i))

            else:
                try:
                    if str(text[i]).replace('  ',' ')[0] == ' ':
                        text_to_write = str(text[i]).replace('  ',' ')[1:]
                        f.write(str(i)+','+ text_to_write.replace(' ',',') + '\n')
                    else:
                        text_to_write = str(text[i]).replace('  ',' ')
                        f.write(str(i)+','+ text_to_write.replace(' ',',') + '\n')
                except:
                    f.write(str(i)+'\n')




simpleAddIndex(r'D01\test.txt','SQLSetup\D1testsql.txt')
simpleAddIndex(r'D01\input.txt','SQLSetup\D1inputsql.txt')
simpleAddIndex(r'D02\test.txt','SQLSetup\D2testsql.txt')
simpleAddIndex(r'D02\input.txt','SQLSetup\D2inputsql.txt')
simpleAddIndex(r'D03\test.txt','SQLSetup\D3testsql.txt')
simpleAddIndex(r'D03\input.txt','SQLSetup\D3inputsql.txt')
D4(r'D04\test.txt','SQLSetup\D4testsql.txt')
D4(r'D04\input.txt','SQLSetup\D4inputsql.txt')