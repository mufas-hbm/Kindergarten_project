from data import kindergartens
from managers_kg import *

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
    if not child_found:
        return None
    child, kindergarten = child_found
    print(f'what school does he go to: {kindergarten["Name"]}')
    print(f'Name: {child["Name"]}')
    print(f'Age: {child["Age"]}')
    print(f'Allergies: {", ".join(child["Allergies"])}')
    print(f'Favorite Activity: {child["FavoriteActivity"]}')
    return child

def list_children(kindergarten):
    """ 
    List all the children in a specified kindergarten. 
    Parameters: 
        kindergarten (str): The name of the kindergarten. 
    Returns: None 
    """
    kg = find_kindergarten(kindergarten)
    if not kg:
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
            print("--------------------------------")

def add_child(kindergarten):
    """ Add a child to a specified kindergarten. 
    Parameters: 
        kindergarten (str): The name of the kindergarten. 
    Returns: 
        None: If the kindergarten is not found or if it is at full capacity. 
        list: The updated list of kindergartens if the child is added successfully. 
    """
    kg = find_kindergarten(kindergarten)
    if not kg:
        return None
    children = kg['Children']
    if kg['Capacity'] - len(children) == 0:
        print("This Kindergarten has no more capacity for new children")
        return None
    else:
        new_child = {}
        #take data from input
        name = input("name: ")
        age = input("Age: ")
        while not age.isdigit(): 
            print("Age must be a number")
            age = input("Age: ")
        age = int(age)
        allergies = []
        favorite_activity = input("Favorite activity: ")
        #add data to dictionary
        new_child['Name'] = name
        new_child['Age'] = age
        new_child['Allergies'] = allergies
        new_child['FavoriteActivity'] = favorite_activity
        #add new cihld to the list of children
        children.append(new_child)
        print("Child was added")
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
    if not child_found:
        return None
    child, kindergarten = child_found
    kindergarten['Children'].remove(child)
    print("Child was succesfully removed")
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
    if not kg:
        return None
    new_kg_name = new_kg['Name']
    children = new_kg['Children']
    if new_kg['Capacity'] - len(children) == 0:
        print("This Kindergarten has no more capacity for new children")
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
    if not child_found:
        return None
    child, kindergarten = child_found
    allergies = child['Allergies']
    #loop runs until break statement comes
    while True:
        allergy = input("Enter one allergy (or press Enter to finish): ")
        if allergy == "":
            break
        elif allergy in allergies:
            print(f'{allergy} already exists')
        else:
            allergies.append(allergy)
    print("allergies added")
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
    if not child_found:
        return None
    child, kindergarten = child_found
    allergies = child['Allergies']
    allergy = input("Enter the allergy to remove: ")
    if allergy in allergies:
        allergies.remove(allergy)
        print("allergy removed")
        return kindergartens
    else:
        print(f'{name} is not allergical to {allergy}')
        return None
    
def update_child_info():
    """ 
    Update any information for any child. Stops if an invalid category is input. 
    Returns: 
        list: The updated list of kindergartens if the child is found and updated. 
        None: If the child is not found in the system. 
    """
    name = input("Enter child name: ")
    child_found = False
    updated_keys = []

    for kg in kindergartens:
        children = kg['Children']
        for child in children:
            if child['Name'] == name:
                categories = '/'.join(child.keys())
                while True:
                    key = input(f'Choose one of the categories ({categories[5:]}):')#avoid changing the name
                    if key not in child:
                        print("invalid category")
                        break
                    if key == 'Age':
                        child[key] = int(input(f'new {key}:'))
                        updated_keys.append(key)
                    elif key == 'Allergies':
                        option = input("you want to add or remove an allergy? (add/remove):")
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