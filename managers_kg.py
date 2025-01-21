from data import kindergartens
from managers_children import *
import re

def find_kindergarten(name):
    """ 
    Search for a kindergarten in the list of kindergartens. 
    Parameters: 
        name (str): The name of the kindergarten to search for. 
    Returns: 
        dict: The kindergarten's information if found. 
        None: If the kindergarten is not found, prints a message and returns None. 
    """
    for kg in kindergartens:
         if kg['Name'] == name:
            return kg
    print("Kindergarten was not found in the system")
    return None

def show_kindergartens():
    """ 
    Print information about all kindergartens. 
    Iterates through the list of kindergartens and prints their names and detailed information. 
    """
    for kg in kindergartens:
        kg_name = kg['Name']
        print("-"*20)
        print(f'Name: {kg_name}')
        kindergarten_information(kg_name)
        print("-"*20)

def add_kindergarten(name, location, capacity, phone, email):
    """ Create a new kindergarten and add it to the list of kindergartens. 
    The new kindergarten will have an empty list of children by default. 
    Parameters: 
        name (str): The name of the kindergarten. 
        location (str): The location of the kindergarten. 
        capacity (int): The maximum number of children allowed. 
        phone (str): The phone number of the kindergarten. 
        email (str): The email address of the kindergarten. 
    Returns: 
        list: The updated list of kindergartens. 
    """
    new_kindergarten = {
        'Name': name,
        'Location': location,
        'Capacity': capacity,
        'Facilities': [],
        'Contact': {
            'Phone': phone,
            'Email': email,
        },
        'Children': []
    }
    kindergartens.append(new_kindergarten)
    print(f'Kindergarten {name} was added to the system')
    return kindergartens

def remove_kindergarten(name):
    """ 
    Delete a kindergarten by name. If it doesn't exist, show a message. 
    Parameters: 
        name (str): The name of the kindergarten to be removed. 
    Returns: 
        list: The updated list of kindergartens if the removal was successful. 
        None: If the kindergarten was not found. 
    """
    kg = find_kindergarten(name)
    if not kg:
        return None
    kindergartens.remove(kg)
    print(f'Kindergarten {name} was succesfully removed from the system')
    return kindergartens
    

def kindergarten_information(name):
    """ 
    Show all the data about a specific kindergarten. 
    Parameters: 
        name (str): The name of the kindergarten to search for.
    Returns: None
    """
    kg = find_kindergarten(name)
    if not kg:
        return None
    location = kg['Location']
    capacity = kg['Capacity']
    contact = kg['Contact']
    phone = contact['Phone']
    email = contact['Email']
    children = len(kg['Children'])
    open_spots = capacity - children
    print(f'Location: {location}')
    print(f'Capacity: {capacity}')
    print("Facilities:")
    unpack_facilities(kg) #calling function to display facilities
    print(f'Contact Information:')
    print(f' - Phone: {phone}')
    print(f' - Email: {email}')
    print(f'Number of enrolled children: {children}')
    print(f'Available enrollment spots: {open_spots}') 

def unpack_facilities(kindergarten):
    """ 
    Unpack and print the list of facilities of a kindergarten. 
    Parameters: 
        kindergarten (dict): The dictionary containing kindergarten details. 
    Returns: None 
    """
    for facility in kindergarten['Facilities']:
        print(f' - {facility}')


def add_facilities(name):
    """ 
    Add facilities to a kindergarten if they do not already exist. 
    Parameters: 
        name (str): The name of the kindergarten to which facilities will be added. 
    Returns: 
        list: The updated list of kindergartens if the kindergarten is found. 
        None if the kindergarten is not found. 
        """
    kg = find_kindergarten(name)
    if not kg:
        return None
    facilities = kg['Facilities']
    #loop runs until break statement comes
    while True:
        facility = input("Enter facility (or press Enter to finish): ")
        if not facility:
            break
        elif facility in facilities:
            print(f'{facility} already exists')
        else:
            facilities.append(facility)
    print("Facilities added")
    return kindergartens

def remove_facility(name):
    """ 
    Remove a facility from a kindergarten. 
    Parameters: 
        name (str): The name of the kindergarten from which the facility will be removed. 
    Returns: 
        list: The updated list of kindergartens if the kindergarten is found and the facility is removed. 
        None: If the kindergarten or the facility is not found. 
    """
    kg = find_kindergarten(name)
    if not kg:
        return None
    facilities = kg['Facilities']
    facility = input("Enter facility to remove: ")
    if facility in facilities:
        facilities.remove(facility)
        print("Facility removed")
    else:
        print(f'{name} doesn\'t have this facility')
    return kindergartens

def update_info():
    """ 
    Update any information from any Kindergarten or Child.

    Runs update_kindergarten_info if input is 'Kindergarten'. 
    Runs update_child_info if input is 'Children'. 
    Stops if invalid data is input. 

    Returns: None 
    """
    type = input("Which kind of info you want to update(Kindergarten/Children)?")
    if type == 'Kindergarten':
         update_kindergarten_info()
    elif type == 'Children':
        update_child_info()
    else:
        print("invalid Data")
        return None
#update Kindergarten Info
def update_kindergarten_info():
    """ 
    Update any information from any Kindergarten. 
    Stops if an invalid category is input. 

    Returns: list: 
        The updated list of kindergartens. 
        None: If the kindergarten is not found. 
    """
    name = input("Enter the Kindergarten name:")
    kg = find_kindergarten(name)
    if not kg:
        return None
    
    categories = '/'.join(kg.keys())
    updated_keys = []

    while True:
        key = input(f'Choose one of the categories ({categories}):')
        if key not in kg:
            print("invalid category")
            break
    
        new_value = input(f'Enter new value for {key}:')

        if key == 'Capacity':
            kg[key] = int(new_value)
        elif key in ['Name','Location']:    
            kg[key] = new_value
        elif key == 'Facilities':
            option = input("you want to add or remove a facility? (add/remove)?")
            if option == 'add': 
                add_facilities(kg['Name']) 
            elif option == 'remove': 
                remove_facility(kg['Name'])
        elif key == 'Contact': 
            contact_type = input("Update Phone or Email? ")
            if contact_type == 'phone': 
                while not validate_phone(new_value): 
                    new_value = input("Invalid phone number. Enter again (format: +49 40 789012): ") 
                kg['Contact']['Phone'] = new_value 
            elif contact_type == 'email': 
                while not validate_email(new_value): 
                    new_value = input("Invalid email format. Enter again: ") 
                kg['Contact']['Email'] = new_value 
            updated_keys.append(contact_type)
        else:
            continue

        updated_keys.append(key)
    if updated_keys: 
        print(f'{", ".join(updated_keys)} from {kg["Name"]} updated') 
    else: 
        print("Nothing updated")
    return kindergartens

def validate_phone(phone):
    """ 
    Validate if the input phone number matches the required format. The required format is: +49 XX XXXXXX 
    Parameters: 
        phone (str): The phone number to validate. 
    Returns: 
        bool: True if the phone number matches the format, False otherwise. 
    """
    phone_pattern = r'^\+49 \d{2} \d{6}$' 
    return bool(re.match(phone_pattern, phone))

def validate_email(email):
    """ 
    Validate if the input email address matches the required format. 
    Parameters: 
        email (str): The email address to validate.
    Returns: 
        bool: True if the email address matches the format, False otherwise. 
    """
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(email_pattern, email))