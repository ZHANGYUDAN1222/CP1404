<<<<<<< HEAD

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def get_password():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    return password

def to_asterisks(password):
    for i in range(len(password)):
        print('*',end='')

def is_valid_password(password):
    # Determine if the provided password is valid.
    if SPECIAL_CHARS_REQUIRED:
        if len(password)>6 or len(password)<2:
            return False
    else:
        if len(password)>6 or len(password)<2:
            return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower+=1
        elif char.isupper():
            count_upper+=1
        elif char.isdigit():
            count_digit+=1

    if count_digit==0 or count_lower==0 or count_upper==0:
        return False
    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if SPECIAL_CHARS_REQUIRED:
        for char in password:
            if char in SPECIAL_CHARACTERS:
                count_special+=1
            elif char.islower():
                count_lower+=1
            elif char.isupper():
                count_upper+=1
            elif char.isdigit():
                count_digit+=1
        if count_digit==0 or count_lower==0 or count_special==0 or count_upper==0:
            return False
        else:
            return True
    # if we get here (without returning False), then the password must be valid
    else:
        return True

def main():
    password=get_password()
    # is_valid_password(password)
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid:".format(len(password)),end='')
    to_asterisks(password)
=======

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def get_password():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    return password

def to_asterisks(password):
    for i in range(len(password)):
        print('*',end='')

def is_valid_password(password):
    # Determine if the provided password is valid.
    if SPECIAL_CHARS_REQUIRED:
        if len(password)>6 or len(password)<2:
            return False
    else:
        if len(password)>6 or len(password)<2:
            return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower+=1
        elif char.isupper():
            count_upper+=1
        elif char.isdigit():
            count_digit+=1

    if count_digit==0 or count_lower==0 or count_upper==0:
        return False
    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if SPECIAL_CHARS_REQUIRED:
        for char in password:
            if char in SPECIAL_CHARACTERS:
                count_special+=1
            elif char.islower():
                count_lower+=1
            elif char.isupper():
                count_upper+=1
            elif char.isdigit():
                count_digit+=1
        if count_digit==0 or count_lower==0 or count_special==0 or count_upper==0:
            return False
        else:
            return True
    # if we get here (without returning False), then the password must be valid
    else:
        return True

def main():
    password=get_password()
    # is_valid_password(password)
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid:".format(len(password)),end='')
    to_asterisks(password)
>>>>>>> da25c61a7f6cf08fca1fde1d3bd1eac9ac249bfa
main()