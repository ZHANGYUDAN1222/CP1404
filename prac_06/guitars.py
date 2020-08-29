"""CP1404/CP5632 Practical - Client code to use the Guitar class."""
from prac_06.guitar import Guitar

def get_name(guitars):
    """To get name, year, cost through while loop"""
    loop=True
    while loop:
        name=input('Name: ')
        if name=='' or name==' ':
            """break the whole loop if the name is empty"""
            loop=False
        else:
            year_l=True

        while year_l:
            """set loop in case the input is not digit"""
            try:
                year=int(input('Year: '))
                year_l=False
                cost_l=True
            except ValueError:
                year_l=True

        while cost_l:
            """set loop in case the input is not digit"""
            try:
                cost=float(input('Cost: '))
                cost_l=False
                guitars.append(Guitar(name,year,cost))
            except ValueError:
                cost_l=True
    return guitars

def show_detail(guitars):
    """Present final output"""
    num=1
    for i in guitars:
        if i.is_vintage():
            vintage_sting='(vintage)'
        else:
            vintage_sting=''
        print('Guitar %i: %s (%i), worth $ %.2f %s' % (num, i.name, i.year, i.cost,vintage_sting))
        num+=1


def main():
    """Create list and call two functions above"""
    guitars = []
    print('My guitars!')
    guitars = get_name(guitars)
    show_detail(guitars)


main()