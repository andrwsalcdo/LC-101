def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    #trim whitespace of user input 
    _fullname = fullname.strip()
    # split full name by ' ' --> [name1, name2, name3, etc]
    names = split_string(_fullname, ' ')
    # accumulate initials here
    initials = ''
    for name in names:
        # find index of name in list of names
        i = names.index(name)
        initials += names[i][0].upper()
    return initials
    
def split_string(og_str, sep):
    split_str= og_str.split(sep)
    return split_str


def main():
    # some more code here (input and print statements)
    user_name = input("What is your full name?")
    user_initials = get_initials(user_name)
    print(user_initials)

if __name__ == '__main__':
    main()