def celsius_to_fahrenheit(celsius):                                                                       
	return celsius * 1.8 + 32.0
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32.0)/1.8
def main():
    choice=int(input('1 for celsius to fahrenheit\n2 for fahrenheit to celsius\nenter your choice:'))
    if choice==1:
        celsius=float(input('Enter celsius temperature:'))
        print('%s celsius is %.2f fahrenheit'%(celsius,celsius_to_fahrenheit(celsius)))
    else:
        fahrenheit=float(input('Enter fahrenheit temperature:'))        
        print('%s celsius is %.2f fahrenheit'%(fahrenheit,fahrenheit_to_celsius(fahrenheit)))
if __name__=="__main__":
    main()