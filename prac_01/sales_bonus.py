"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""
def main():
    sales=float(input('Please enter the price:'))
    while (sales<0):
        print('Invalid input, please enter a positive figure.')
        sales=float(input('Please enter the price:'))
    if sales<1000:
        bonus=sales*0.1
    else:
        bonus=sales*0.15
    print('Your bonus is: $%.2f'%bonus)
if __name__=='__main__':
    main()