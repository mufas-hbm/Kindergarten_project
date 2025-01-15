from data import kindergartens
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
    print(f'Kindergarten was not found in the system')
    return None

def show_kindergartens():
    """ 
    Print information about all kindergartens. 
    Iterates through the list of kindergartens and prints their names and detailed information. 
    """
    for kg in kindergartens:
        kg_name = kg['Name']
        print("-"*20)
        print(f'Name: {kg["Name"]}')
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
    if kg is None:
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
    if kg is None:
        return None
    location = kg['Location']
    facilities = kg['Facilities']
    capacity = kg['Capacity']
    contact = kg['Contact']
    phone = contact['Phone']
    email = contact['Email']
    children = count_children(kg['Children'])
    open_spots = capacity - children
    print(f'Location: {location}')
    print(f'Capacity: {capacity}')
    print(f'Facilities:')
    unpack_facilities(kg) #calling fucntion to display facilities
    print(f'Contact Information:')
    print(f' - Phone: {phone}')
    print(f' - Email: {email}')
    print(f'Number of enrolled children: {children}')
    print(f'Available enrollment spots: {open_spots}') 

# Lambda function to count the number of children in a kindergarten
count_children = lambda children: len(children)

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
    if kg is None:
        return None
    facilities = kg['Facilities']
    facility = input(f'Enter facility: ')
    facilities.append(facility)
    #loop runs until break statement comes
    while True:
        facility = input(f'Enter facility (or press Enter to finish): ')
        if facility == "":
            break
        elif facility in facilities:
            print(f'{facility} already exists')
        else:
            facilities.append(facility)
    print(f'Facilities added')
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
    if kg is None:
        return None
    facilities = kg['Facilities']
    facility = input(f'Enter facility to remove: ')
    if facility in facilities:
        facilities.remove(facility)
        print(f'Facility removed')
        return kindergartens
    else:
        print(f'{name} doesn\'t have this facility')

def find_child(name):
    """ Search for a child in the system. If the child doesn't exist, return None. 
    Parameters: 
        name (str): The name of the child to search for. 
    Returns:
        tuple: A tuple containing the child's information (dict) and the kindergarten's information (dict) if found. 
        None: If the child is not found in any kindergarten. 
    """
    for kg in kindergartens:
        children = kg['Children']
        for child in children:
            child_name = child['Name']
            if child_name == name:
                return child, kg
    print(f'Child {name} was not found in the system')
    return None

def show_child_information(name):
    """ 
    Search for a child and show their information. 
    Parameters: 
        name (str): The name of the child. 
    Returns: None 
    """
    child_found = find_child(name)
    if child_found is None:
        return None
    child, kindergarten = child_found
    print(f'what school does he go to: {kindergarten["Name"]}')
    print(f'Name: {child["Name"]}')
    print(f'Age: {child["Age"]}')
    print(f'Allergies: {", ".join(child["Allergies"])}')
    print(f'Favorite Activity: {child["FavoriteActivity"]}')


def list_children(kindergarten):
    """ 
    List all the children in a specified kindergarten. 
    Parameters: 
        kindergarten (str): The name of the kindergarten. 
    Returns: None 
    """
    kg = find_kindergarten(kindergarten)
    if kg is None:
        return None
    children = kg['Children']
    if len(children) == 0:
        print (f'{kg['Name']} has no children registered')
    else:       
        for child in children:
            print(f'Name: {child["Name"]}')
            print(f'Age: {child["Age"]}')
            print(f'Allergies: {", ".join(child["Allergies"])}')
            print(f'Favorite Activity: {child["FavoriteActivity"]}')
            print(f'--------------------------------')

def add_child(kindergarten):
    """ Add a child to a specified kindergarten. 
    Parameters: 
        kindergarten (str): The name of the kindergarten. 
    Returns: 
        None: If the kindergarten is not found or if it is at full capacity. 
        list: The updated list of kindergartens if the child is added successfully. 
    """
    kg = find_kindergarten(kindergarten)
    if kg is None:
        return None
    children = kg['Children']
    if kg['Capacity'] - count_children(children) == 0:
        print(f'This Kindergarten has no more capacity for new children')
        return None
    else:
        new_child = {}
        #take data from input
        name = input(f'name: ')
        age = input(f'Age: ')
        while not age.isdigit(): 
            print("Age must be a number")
            age = input("Age: ")
        age = int(age)
        allergies = []
        favorite_activity = input(f'Favorite activity: ')
        #add data to dictionary
        new_child['Name'] = name
        new_child['Age'] = age
        new_child['Allergies'] = allergies
        new_child['FavoriteActivity'] = favorite_activity
        #add new cihld to the list of children
        children.append(new_child)
        print(f'Child was added')
        return kindergartens
        
def remove_child(name):
    """ 
    Remove a child by passing their name. 
    Parameters: 
        name (str): The name of the child to be removed. 
    Returns: 
        list: The updated list of kindergartens if the child is found and removed. 
        None: If the child is not found in the system. 
    """
    child_found = find_child(name)
    if child_found is None:
        return None
    child, kindergarten = child_found
    kindergarten['Children'].remove(child)
    print(f'Child was succesfully removed')
    return kindergartens
    
def move_child(name_child, name_kindergarten):
    """ Move a child from one kindergarten to another. 
    Parameters: 
        name_child (str): The name of the child to be moved. 
        name_kindergarten (str): The name of the new kindergarten. 
    Returns: 
        list: The updated list of kindergartens. 
        None: If the child or new kindergarten is not found or if the new kindergarten is at full capacity. 
    """
    new_kg = find_kindergarten(name_kindergarten)
    if new_kg is None:
        return None
    new_kg_name = new_kg['Name']
    children = new_kg['Children']
    if new_kg['Capacity'] - count_children(children) == 0:
        print(f'This Kindergarten has no more capacity for new children')
        return None
    
    child_found = False
    for kg in kindergartens:
        children = kg['Children']
        old_kg_name = kg['Name']
        for child in children:
            if child['Name'] == name_child:
                temp = child
                children.remove(child)
                child_found = True
                break
        if child_found:
            break
    if not child_found:
        print(f'Child {name_child} was not found in the system')
        return None
    new_kg['Children'].append(temp)
    print(f'{name_child} was moved from {old_kg_name} to {new_kg_name}')
    return kindergartens

#Add child allergies from the system
def add_allergies(name):
    """ 
    Add allergies to a child by passing their name. 
    Parameters: 
        name (str): The name of the child. 
    Returns: 
        list: The updated list of kindergartens if the child is found. 
        None: If the child is not found in the system. 
    """
    child_found = find_child(name)
    if child_found is None:
        return None
    child, kindergarten = child_found
    allergies = child['Allergies']
    #loop runs until break statement comes
    while True:
        allergy = input(f'Enter one allergy (or press Enter to finish): ')
        if allergy == "":
            break
        elif allergy in allergies:
            print(f'{allergy} already exists')
        else:
            allergies.append(allergy)
    print(f'allergies added')
    return kindergartens
    

def remove_allergy(name):
    """ 
    Remove an allergy from a child by passing their name. 
    Parameters: 
        name (str): The name of the child. 
    Returns: 
        list: The updated list of kindergartens if the child is found and the allergy is removed. 
        None: If the child is not found in the system or if the allergy is not present. 
    """
    child_found = find_child(name)
    if child_found is None:
        return None
    child, kindergarten = child_found
    allergies = child['Allergies']
    allergy = input(f'Enter the allergy to remove: ')
    if allergy in allergies:
        allergies.remove(allergy)
        print(f'allergy removed')
        return kindergartens
    else:
        print(f'{name} is not allergical to {allergy}')
        return None
        
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

def update_info():
    """ 
    Update any information from any Kindergarten or Child.

    Runs update_kindergarten_info if input is 'Kindergarten'. 
    Runs update_child_info if input is 'Children'. 
    Stops if invalid data is input. 

    Returns: None 
    """
    type = input("Which kind of info you want to update(Kindergarten/Children)?")
    while True:
        if type == 'Kindergarten':
            update_kindergarten_info()
        elif type == 'Children':
            update_child_info()
        else:
            print(f'invalid Data')
            break
#update Kindergarten Info
def update_kindergarten_info():
    """ 
    Update any information from any Kindergarten. 
    Stops if an invalid category is input. 

    Returns: list: 
        The updated list of kindergartens. 
        None: If the kindergarten is not found. 
    """
    name = input(f'Enter the Kindergarten name:')
    kg = find_kindergarten(name)
    if kg is None:
        return None
    
    categories = '/'.join(kg.keys())
    updated_keys = []

    while True:
        key = input(f'Choose one of the categories ({categories}):')
        if key not in kg:
            print(f'invalid category')
            break

        if key == 'Capacity':
            kg[key] = int(input(f'new {key}:'))
            updated_keys.append(key)
        elif key in ['Name','Location']:    
            kg[key] = input(f'new {key}:')
            updated_keys.append(key)
        elif key == 'Facilities':
            option = input(f'you want to add or remove a facility? (add/remove)?')
            add_facilities(kg['Name']) if option == 'add' else remove_facility(kg['Name'])
            updated_keys.append(key)
        elif key == 'Contact':
            contact_dict = kg['Contact']
            option = input(f'you want to update Phone or Email?')
            if option == 'Phone':
                #phone number validator
                while True:
                    phone = input("Phone number (format:+49 40 789012):")
                    if validate_phone(phone):
                        contact_dict['Phone'] = phone
                        key = 'Phone'
                        updated_keys.append(key)
                        break 
                    else: print("Invalid phone number. Please try again.")
            elif option == 'Email':
                #email validator
                while True:
                    email = input("Email: ")
                    if validate_email(email): 
                        contact_dict['Email'] = email
                        key = 'Email'
                        updated_keys.append(key)
                        break 
                    else: print("Invalid email format. Please try again.")  
    print(f'Nothing updated')if len(updated_keys) == 0 else print(f'{", ".join(updated_keys)} from {kg["Name"]} updated')
    return kindergartens

def update_child_info():
    """ 
    Update any information for any child. Stops if an invalid category is input. 
    Returns: 
        list: The updated list of kindergartens if the child is found and updated. 
        None: If the child is not found in the system. 
    """
    name = input(f'Enter child name: ')
    child_found = False
    updated_keys = []

    for kg in kindergartens:
        children = kg['Children']
        for child in children:
            child_name = child['Name']
            if child_name == name:
                categories = '/'.join(child.keys())
                while True:
                    key = input(f'Choose one of the categories ({categories[5:]}):')#avoid changing the name
                    if key not in child:
                        print(f'invalid category')
                        break
                    if key == 'Age':
                        child[key] = int(input(f'new {key}:'))
                        updated_keys.append(key)
                    elif key == 'Allergies':
                        option = input(f'you want to add or remove an allergy? (add/remove):')
                        add_allergies(child['Name']) if option == 'add' else remove_allergy(child['Name'])
                        updated_keys.append(key)
                    elif key == 'FavoriteActivity':
                        child[key] = input(f'new {key}:')
                        updated_keys.append(key)
                child_found = True
                print(f'Nothing updated')if not updated_keys else print(f'{", ".join(updated_keys)} from {child["Name"]} updated')
                return kindergartens
    if not child_found:
        print(f'Child {name} was not found on the system')