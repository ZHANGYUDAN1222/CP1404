def main():
    while True:
        total=0
        num_item=int(input('Number of items:'))
        if num_item<0:
            print('Invalid input,please try again.')
        else:
            for i in range(num_item):
                price=float(input('Price of item:'))
                total+=price
            if total>100:
                total=total*0.9
            print('Total price for %i item(s) is %.2f'%(num_item,total))
            break
if __name__=='__main__':
    main()