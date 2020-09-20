"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics')
    for subdirectory in os.listdir('.'):
        print(subdirectory)
        if os.path.isdir(subdirectory):
            os.chdir(subdirectory)
            print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
            for filename in os.listdir('.'):
                # print(filename)
                new_name= get_fix_name(filename)
            os.chdir("..")
        else:
            print('{}, It is not a directory'.format(subdirectory))

def get_fix_name(filename):
    """Return a 'fixed' version of filename."""
    pernalist = filename.split()
    capital_name = ''
    for i in pernalist:
        i = i[0].upper() + i[1:]
        capital_name += i
    dash_name = capital_name[:-4]
    new_name = ''
    for i, char in enumerate(dash_name):
        if dash_name[i-1] == '(':
            char = char.upper()
        elif char.isupper():
            char = "_" + char
        else:
            char = char
        new_name += char
    new_name = new_name[1:] + '.txt'
    print(new_name)

        


    # for file in filename:



    # Loop through each file in the (current) directory
    #     for filename in os.listdir('.'):
    #         Ignore directories, just process files
    #         if os.path.isdir(filename):
    #             continue

        # new_name = get_fixed_filename(filename)
        # print("Renaming {} to {}".format(filename, new_name))



def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

main()
# demo_walk()