def simpleAddIndex(input_path,output_path):
    with open(input_path) as f:
        text = f.read().split('\n')

    with open(output_path,"w") as f:
        for i in range(0,len(text)):
            if i == len(text)-1:
                f.write(str(i)+','+str(text[i]))
            else:
                f.write(str(i)+','+str(text[i]) + '\n')



simpleAddIndex(r'D01\test.txt','SQLSetup\D1testsql.txt')
simpleAddIndex(r'D01\input.txt','SQLSetup\D1inputsql.txt')
simpleAddIndex(r'D02\test.txt','SQLSetup\D2testsql.txt')
simpleAddIndex(r'D02\input.txt','SQLSetup\D2inputsql.txt')
simpleAddIndex(r'D03\test.txt','SQLSetup\D3testsql.txt')
simpleAddIndex(r'D03\input.txt','SQLSetup\D3inputsql.txt')