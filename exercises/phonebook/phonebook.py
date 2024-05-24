#!/usr/bin/env python3

"""Phone book exercise"""

# Write a program that implements a simple phone book.
#
# The program should prompt the user for a name and return
# the corresponding contact information.
#
# The user can type index to get a list of all names in the
# phone book, and can type quit to exit the program.
#
# The phone book should be stored in a file called phonebook.txt
# (provided in the exercise folder)

# Learning objectives:
#   - input and output
#   - functions
#   - if statements
#   - read files
#   - for and while loops
#   - dictionaries
#   - error handling
#   - list comprehensions

def load_phonebook(filename: str) -> dict:
    """Loads a phone book from a file.

    Args:
        filename (str): The name of the file to load.

    Returns:
        dict: A dictionary containing the phone book.
    """
    
    contacts = {}

    f = open(filename, "r")
    content = f.readlines()
    contact = {}
    for line in content:
        line = line.strip()
        if line != "":
            field, data = line.split(": ")
            contact[field] = data
        else:
            contacts[contact["Name"].lower()] = contact
            contact = {}
    if contact != {}:
        contacts[contact["Name"].lower()] = contact
    f.close()

    return contacts

def create_index(phonebook: dict) -> list:
    """Creates an index of names in the phone book.

    Args:
        phonebook (dict): The phone book to index.

    Returns:
        list: A list of names in the phone book.
    """    

    # index = []
    # for name in phonebook:
    #     index.append(phonebook[name]["Name"])
    # return index

    return [phonebook[name]["Name"] for name in phonebook]

def print_contact(contact: dict) -> None:
    """Prints a contact.

    Args:
        contact (dict): The contact to print.
    """
    
    print("\n------------------------")
    for field in contact:
        print(f"{field.capitalize()}: {contact[field]}")
    print("------------------------\n")

def print_index(index: list) -> None:
    """Prints an index of names.

    Args:
        index (list): The index to print.
    """
    print("\n------------------------")
    print("\n".join(index))
    print("------------------------\n")

if __name__ == "__main__":
    contacts = load_phonebook("phonebook.txt")
    index = create_index(contacts)

    name = ""
    while name != "quit":
        try:
            name = input("Enter a name: ").lower()
            print_contact(contacts[name])
        except KeyError:
            if name == "index":
                # print(list(contacts.keys()))
                print_index(index)
            elif name != "quit":
                print("\nSorry, that name is not in the phone book.\n")
