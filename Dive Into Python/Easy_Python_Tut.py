# Programma che mostra un menu
def print_menu():
    print '1. Print Phone Numbers'
    print '2. Add a Phone Number'
    print '3. Remove a Phone Number'
    print '4. Lookup a Phone Number'
    print '5. Quit'


numbers = {}
menu_choice = 0
print_menu()

while menu_choice != 5:
    menu_choice = input("Type in a number (1-5):")
    if menu_choice == 1:
        print "Telephone Numbers:"
        for x in numbers.keys():
            print "Name: ", x, " \tNumber: ", numbers[x]
            print

    elif menu_choice == 2:
        print "Add Name and Number"
        name = raw_input("Name:")
        phone = raw_input("Number:")
        numbers[name] = phone

    elif menu_choice == 3:
        print "Remove Name and Number"
        name = raw_input("Name:")
        if numbers.has_key(name):
            del numbers[name]
        else:
            print name, " was not found"

    elif menu_choice == 4:
        print "Lookup Number"
        name = raw_input("Name:")
        if numbers.has_key(name):
            print "The number is", numbers[name]
        else:
            print name, " was not found"

    elif menu_choice != 5:
        print_menu()
