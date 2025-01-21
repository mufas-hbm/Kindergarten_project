from managers_children import *
from managers_kg import *

def show_menu():
    """ 
    Display the menu options to the user. 

    Prints a list of task options that the user can choose from. 
    """
    menu = ( 
            "==================================================\n" 
            "===        KINDERGARTEN MANAGING SYSTEM        ===\n"
            "==================================================\n" 
            " Please choose one of the following tasks:\n"
            " 1.    Add Kindergarten \n" 
            " 2.    Remove Kindergarten \n" 
            " 3.    See information about one Kindergarten \n" 
            " 4.    Register child in Kindergarten \n" 
            " 5.    See information about child \n" 
            " 6.    List Children of a Kindergarten \n" 
            " 7.    Unsubscribe child from Kindergarten \n" 
            " 8.    Move child to another kindergarten \n" 
            " 9.    Add facilities to a Kindergarten \n" 
            " 10.   Remove facility from Kindergarten \n" 
            " 11.   Add child allergies \n" 
            " 12.   Remove child allergies \n" 
            " 13.   Show all Kindergartens Information \n"
            " 14.   Update any Information\n"
            " 15.   Exit\n"
            "==================================================\n"
    ) 
    print(menu)

def main():
    """ 
    Main function to display the menu and handle user input. 
    
    Continuously displays a menu to the user and processes their input to execute 
    the corresponding tasks. 
    
    Validates that the user input is a number and calls the appropriate functions based on the chosen task number. 
    The loop continues until the user chooses to exit. 
    """
    while True:
        show_menu()
        chosen_number = input("What you want to do? ")

        # Validate if the input is an integer 
        if not chosen_number.isdigit(): 
            print("Error: Please enter only numbers.")
            continue 
        
        # Proceed with the task selection
        chosen_number = int(chosen_number) 

        if chosen_number == 1:
            print("You want to add Kindergarten to the system, please fill the data:\n")
            name = input("Enter a name: ")
            location = input("Enter a location: ")
            capacity = input("How many children are allowed? ")
            while not capacity.isdigit(): 
                print("Capacity must be a number")
                capacity = input("How many children are allowed? ")
            capacity = int(capacity)
            #phone number validator
            while True:
                phone = input("Phone number (format:+49 40 789012):")
                if validate_phone(phone): 
                    break 
                else: print("Invalid phone number. Please try again.")
            #email validator
            while True:
                email = input("Email: ")
                if validate_email(email): 
                    break 
                else: print("Invalid email format. Please try again.")
            add_kindergarten(name, location, capacity, phone, email)
            keepOn()
        elif chosen_number == 2:
            print(f'You want to remove one Kindergarten to the system, please fill the data:\n')
            name = input("Enter a name: ")
            remove_kindergarten(name)
            keepOn()
        elif chosen_number == 3:
            name = input("Enter a name of a Kindergarten to see information about it: ")
            kindergarten_information(name)
            keepOn()
        elif chosen_number == 4:
            name = input("Enter a name of a Kindergarten to add a child: ")
            add_child(name)
            keepOn()
        elif chosen_number == 5:
            name = input("Enter the name of the child to search: ")
            show_child_information(name)
            keepOn()
        elif chosen_number == 6:
            name = input("Enter a name of a Kindergarten: ")
            list_children(name)
            keepOn()
        elif chosen_number == 7:
            name = input("Enter a name of a child: ")
            remove_child(name)
            keepOn()
        elif chosen_number == 8:
            name_child = input("Enter a name of a child: ")
            name_kindergarten = input("in which kinderkarten should be moved: ")
            move_child(name_child, name_kindergarten)
            keepOn()
        elif chosen_number == 9:
            name = input("Enter a name of a Kindergarten: ")
            add_facilities(name)
            keepOn()
        elif chosen_number == 10:
            name = input("Enter a name of a Kindergarten: ")
            remove_facility(name)
            keepOn()
        elif chosen_number == 11:
            name = input("Enter a name of a Child: ")
            add_allergies(name)
            keepOn()
        elif chosen_number == 12:
            name = input("Enter a name of a Child: ")
            remove_allergy(name)
            keepOn()
        elif chosen_number == 13:
            show_kindergartens()
            keepOn()
        elif chosen_number == 14:
            update_info()
            keepOn()
        elif chosen_number == 15:
            print("See you next time")
            break
        else:
            print("this option doesn't exist, try again")

def keepOn(): 
    """ 
    Pause the program to wait for user input to continue. 
    Prompts the user to press Enter to continue. 
    """ 
    input("\nPress Enter to continue...")

#run the programm
main()