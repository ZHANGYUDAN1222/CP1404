"""
CP1404/CP5632 Practical
Create new directories and Sort extensions
"""
import shutil
import os

def main():
    """Get current working directory"""
    print("Starting directory is: {}".format(os.getcwd()))

    """Change path to directory FilesToSort"""
    os.chdir('FilesToSort')

    """Create dictionary to store different files"""
    all_type = {'txt': [], 'doc': [], 'docx': [], 'xls': [], 'xlsx': [], 'png': [], 'gif': [], 'jpg': []}

    """Sort different files in corresponding list"""
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            all_type = sort_files(filename, all_type)
        else:
            pass
    # test if all_type returns correctly
    # print(all_type)

def sort_files(filename,all_type):
    """Function to sort and append files according to there type"""
    # create a list , split by '.'
    split_name = filename.split('.')
    for k,v in all_type.items():
        if split_name[1] == k:
            v.append(filename)
        else:
            continue
    return all_type


main()