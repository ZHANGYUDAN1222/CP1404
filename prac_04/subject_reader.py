"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    subject_detail()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME,"r")
    lists=[]
    for line in input_file:
        line=line.strip()
        lists.append((line.split(',')))
    input_file.close()
    return lists

def subject_detail():
    line_list=get_data()
    for list in line_list:
        print('%s is taught by %-12s and has %-3s students'%(list[0],list[1],list[2]))


main()