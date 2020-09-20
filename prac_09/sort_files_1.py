"""
CP1404/CP5632 Practical
Create new directories and Sort extensions
"""

import os

def main():
    """Get current working directory"""
    print("Starting directory is: {}".format(os.getcwd()))
    """Change path to directory FilesToSort"""
    os.chdir('FilesToSort')
    """Create lists to sort different files"""
    txt = []
    doc = []
    docx = []
    xls = []
    xlsx = []
    png = []
    gif = []
    jpg = []
    """Sort different files in corresponding list"""
    for filename in os.listdir('.'):
        txt, doc, docx, xls, xlsx, png, gif, jpg = sort_files(filename,txt, doc, docx, xls, xlsx, png, gif, jpg)
    # Test if the file in the right list
    # print(txt, doc, docx, xls, xlsx, png, gif, jpg)

def sort_files(filename,txt, doc, docx, xls, xlsx, png, gif, jpg):
    """Function to sort and append files according to there type"""
    # create a list , split by '.'
    split_name = filename.split('.')
    if split_name[1] == 'txt':
        txt.append(filename)
    elif split_name[1] == 'doc':
        doc.append(filename)
    elif split_name[1] == 'docx':
        docx.append(filename)
    elif split_name[1] == 'xls':
        xls.append(filename)
    elif split_name[1] == 'xlsx':
        xlsx.append(filename)
    elif split_name[1] == 'png':
        png.append(filename)
    elif split_name[1] == 'gif':
        gif.append(filename)
    elif split_name[1] == 'jpg':
        jpg.append(filename)
    else:
        print('Wrong')
    return txt, doc, docx, xls, xlsx, png, gif, jpg

main()