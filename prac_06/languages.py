"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class."""

from prac_06.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    """Test if the function is working properly"""
    print(ruby)
    print(python)
    print(visual_basic)

    """Create a list to store the three objects"""
    languages=[ruby,python,visual_basic]

    """loop through and print the names of all languages with dynamic typing"""
    print('The dynamically typed languages are:')
    for lang in languages:
        if lang.reflection==True:
            print(lang.name)

main()