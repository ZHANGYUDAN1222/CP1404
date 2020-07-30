""" for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0,110,10):
    print(i,end=' ')
print()
# b
for i in range(20,0,-1):
    print(i,end=' ')
print()
# c
while True:
    num=int(input('Please enter an positive integer:'))
    if num<0:
        print('Invalid input, please try again.')
    else:
        print('Number of stars:',num)
        for i in range(num):
            print('*',end='')
        break
# d
while True:
    num=int(input('Please enter a positive integer:'))
    if num<0:
        print('Invalid input, please try again.')
    else:
        print('Number of stars:',num)
        for i in range(1,num+1):
            for z in range(i):
                print('*',end='')
            print()
        break """


print(5 //2)