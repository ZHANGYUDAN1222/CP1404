"""
CP1404/CP5632 Practical
Create new directories and Sort extensions
"""

import os

def main():
    """Get current working directory"""
    print("Starting directory is: {}".format(os.getcwd()))

def sort_files(filename,txt, doc, docx, xls, xlsx, png, gif, jpg):
    split_name = filename.split('.')
    if split_name[1] == '.txt':
        txt.append(filename)
    elif split_name[1] == '.doc':
        doc.append(filename)
    elif split_name[1] == '.docx':
        docx.append(filename)
    elif split_name[1] == '.xls':
        xls.append(filename)
    elif split_name[1] == '.xlsx':
        xlsx.append(filename)
    elif split_name[1] == '.png':
        png.append(filename)
    elif split_name[1] == '.gif':
        gif.append(filename)
    elif split_name[1] == '.jpg':
        jpg.append(filename)
    return txt, doc, docx, xls, xlsx, png, gif, jpg