with open('name.txt','w')as f1:
    name=input('Enter your name:')  # ask for name
    f1.write(name)
with open('name.txt','r')as f2:
    f2_name=f2.read()
    print('Your name is {}'.format(f2_name))  # print name
with open('numbers.txt','w')as f3:
    f3.writelines('''17
42
400''')    # store numbers
with open('numbers.txt','r')as f4:
    line=f4.read().split('\n')     # line=['17','42','400']
    print(int(line[0])+int(line[1]))   # sum of first two nums
    total=0
    for i in line:
        total+=int(i)   #total
    print(total)