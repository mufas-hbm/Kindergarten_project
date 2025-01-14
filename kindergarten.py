import re

#default data
kindergartens = [
    {
        'Name': 'Sunshine Kindergarten',
        'Location': 'Berlin, Germany',
        'Capacity': 120,
        'Facilities': ['Playground', 'Library', 'Art Room'],
        'Contact': {
            'Phone': '+49 30 123456',
            'Email': 'info@sunshine-kindergarten.de'
        },
        'Children': [
            {'Name': 'Lena', 'Age': 4, 'Allergies': ['Peanuts', 'Tomatoes'], 'FavoriteActivity': 'Painting'},
            {'Name': 'Max', 'Age': 5, 'Allergies': [], 'FavoriteActivity': 'Building Blocks'}
        ]
    },
    {
        'Name': 'Happy Kids Kindergarten',
        'Location': 'Munich, Germany',
        'Capacity': 100,
        'Facilities': ['Outdoor Play Area', 'Music Room', 'Science Lab'],
        'Contact': {
            'Phone': '+49 89 654321',
            'Email': 'info@happykids.de'
        },
        'Children': [
            {'Name': 'Sophia', 'Age': 3, 'Allergies': ['Dairy'], 'FavoriteActivity': 'Singing'},
            {'Name': 'Lucas', 'Age': 4, 'Allergies': ['Gluten'], 'FavoriteActivity': 'Science Experiments'}
        ]
    },
    {
        'Name': 'Rainbow Kindergarten',
        'Location': 'Hamburg, Germany',
        'Capacity': 3,
        'Facilities': ['Swimming Pool', 'Gymnasium', 'Library'],
        'Contact': {
            'Phone': '+49 40 789012',
            'Email': 'info@rainbow-kindergarten.de'
        },
        'Children': [
            {'Name': 'Emma', 'Age': 5, 'Allergies': ['Eggs', 'Nuts', 'Dairy', 'Shellfish', 'Wheat', 'Soy'], 'FavoriteActivity': 'Reading'},
            {'Name': 'Oliver', 'Age': 3, 'Allergies': ['Eggs','Nuts'], 'FavoriteActivity': 'Playing in the Gym'}
        ]
    },
    {
        'Name': 'Little Stars Kindergarten',
        'Location': 'Frankfurt, Germany',
        'Capacity': 90,
        'Facilities': ['Garden', 'Theater Room', 'Art Studio'],
        'Contact': {
            'Phone': '+49 69 345678',
            'Email': 'info@littlestars.de'
        },
        'Children': [
            {'Name': 'Lara', 'Age': 4, 'Allergies': [], 'FavoriteActivity': 'Gardening'},
            {'Name': 'Tim', 'Age': 5, 'Allergies': ['Nuts'], 'FavoriteActivity': 'Acting'}
        ]
    }
    
]
#Menu printing
def show_menu(): 
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
            " 15.   Leave\n"
            "==================================================\n"
    ) 
    print(menu)

#main function, it runs at the beginning
def main():
    show_menu()
    chosen_number = input("Enter a task number: ")
    # Validate if the input is an integer 
    if not chosen_number.isdigit(): 
        print("Error: Please enter only numbers.") 
        main()
    else:
        # Proceed with the task selection
        chosen_number = int(chosen_number) 
        if chosen_number == 1:
            print(f'You want to add Kindergarten to the system, please fill the data:\n')
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
            print(f'See you next time')
        else:
            print("this option doesn't exist, try again")
            main()
#search for a kindergarten
def find_kindergarten(name):
    '''
search for one kindergarten in the list of kindergartens
arguments:
    name: str
return:
    kindergarten: dict if name was found, otherwise return message
    '''
    for kg in kindergartens:
         if kg['Name'] == name:
            return kg
    print(f'this Kindergarten was not found')
    return None

#Show all Kindergartens
def show_kindergartens():
    '''
print all the kindergartens
    '''
    for kg in kindergartens:
        kg_name = kg['Name']
        print("-"*20)
        print(f'Name: {kg['Name']}')
        kindergarten_information(kg_name)
        print("-"*20)

#Adding Kindergarten
def add_kindergarten(name, location, capacity, phone, email):
    '''
create a new Kindergarten and add to the List of dictionaries
By creating a new one, there are no children (we create key Children but its empty by default)
arguments:
    name: str
    location: str
    capacity: int
    '''
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

#Delete Kindergarten
def remove_kindergarten(name):
    '''
delete a kindergarten passing the name. If doesn't exists, show message
arguments:
    name: str
    '''
    if find_kindergarten(name) == None:
        return
    else:
        kg = find_kindergarten(name)
        kindergartens.remove(kg)
        print(f'Kindergarten {name} was succesfully removed from the system')
        return kindergartens
    
#See information about one Kindergarten
def kindergarten_information(name):
    '''
show all the data about one kindergarten
arguments:
    name: str
    '''
    if find_kindergarten(name) == None:
        return
    else:
        kg = find_kindergarten(name)
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
        print(f'Number of enrolled infants: {children}')
        print(f'Available enrollment spots: {open_spots}') 

#lambda function returns number of children in a kindergarten 
count_children = lambda children: len(children)

#unpack facilities
def unpack_facilities(kindergarten):
    '''
unpacking list facilities of one kindergarten to list
    '''
    for facility in kindergarten['Facilities']:
        print(f' - {facility}')

#add facilities
def add_facilities(name):
    '''
add facilities to a kindergarten if not already exist.
arguments:
    name: str
return:
    kindergartens: list of dict
    '''
    if find_kindergarten(name) == None:
        return
    else:
        kg = find_kindergarten(name)
        facilities = kg['Facilities']
        facility = input(f'Enter facility: ')
        facilities.append(facility)
        #loop runs until break statement comes
        while True:
            facility = input(f'Enter facility: ')
            if facility == "":
                break
            elif facility in facilities:
                print(f'{facility} already exists')
            else:
                facilities.append(facility)
        print(f'Facilities added')
        return kindergartens

#remove facility
def remove_facility(name):
    '''
remove facilitiy from Kindergarten
arguments:
    name: str
return:
    kindergartens: list of dict
    '''
    if find_kindergarten(name) == None:
            return
    else:
        kg = find_kindergarten(name)
        facilities = kg['Facilities']
        facility = input(f'Enter facility: ')
        if facility in facilities:
            facilities.remove(facility)
            print(f'Facility removed')
            return kindergartens
        else:
            print(f'{name} doesn\'t have this facility')

#find child
def find_child(name):
    '''
search for a child in system. if child doesn't exists returns None
arguments:
    name: str
return:
    child: dict
    kg: dict
    '''
    for kg in kindergartens:
        children = kg['Children']
        for child in children:
            child_name = child['Name']
            if child_name == name:
                return child, kg
    print(f'Child {name} was not found on the system')
    return None

#List child information 
def show_child_information(name):
    '''
search for a child and show information
arguments:
    name: str
    ''' 
    if find_child(name) == None:
        return
    else:
        child, kindergarten = find_child(name)
        print(f'what school does he go to: {kindergarten['Name']}')
        print(f'Name: {child['Name']}')
        print(f'Age: {child['Age']}')
        print(f'Allergies: {', '.join(child['Allergies'])}')
        print(f'Favorite Activity: {child['FavoriteActivity']}')

#List Children of a kindergarten
def list_children(kindergarten):
    '''
passing a kindergarten list all the children
argument:
    kindergarten: str
    '''
    if find_kindergarten(kindergarten) == None:
        return
    else:
        kg = find_kindergarten(kindergarten)
        children = kg['Children']
        if len(children) == 0:
            print (f'{kg['Name']} has no children registered')
        else:       
            for child in children:
                print(f'Name: {child['Name']}')
                print(f'Age: {child['Age']}')
                print(f'Allergies: {', '.join(child['Allergies'])}')
                print(f'Favorite Activity: {child['FavoriteActivity']}')
                print(f'--------------------------------')

#add child
def add_child(kindergarten):
    '''
add child passing a kindergarten 
arguments:
    kindergarten:str
return:
    None if Kindergarten is already full of children
    kindergartens: list
    '''
    if find_kindergarten(kindergarten) == None:
        return
    else:
        kg = find_kindergarten(kindergarten)
        children = kg['Children']
        if kg['Capacity'] - count_children(children) == 0:
            print(f'This Kindergarten has no more children register capacity')
            return 
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
        
#remove child
def remove_child(name):
    '''
remove a child by passing a name
arguments:
    name: str
return:
    kindergartens: list
    '''
    if find_child(name) == None:
        return
    else:
        child, kindergarten = find_child(name)
        kindergarten['Children'].remove(child)
        print(f'Child was succesfully removed')
        return kindergartens
    
#move child from kindergarten to another
def move_child(name_child, name_kindergarten):
    '''
move one child from one kindergarten to another
arguments:
    name: str
    kindergarten: dict
return:
    kindergartens
    '''
    if find_kindergarten(name_kindergarten) == None:
        return
    else:
        new_kg = find_kindergarten(name_kindergarten)
        new_kg_name = new_kg['Name']
        children = new_kg['Children']
        if new_kg['Capacity'] - count_children(children) == 0:
            print(f'This Kindergarten has no more children register capacity')
            return
    child_found = False
    for kg in kindergartens:
        children = kg['Children']
        old_kg_name = kg['Name']
        for child in children:
            child_name = child['Name']
            if child_name == name_child:
                temp = child
                children.remove(child)
                child_found = True
                break
    if not child_found:
        print(f'Child {name_child} was not found on the system')
        return
    new_kg['Children'].append(temp)
    print(f'{name_child} was moved from {old_kg_name} to {new_kg_name}')
    return kindergartens

#Add child allergies from the system
def add_allergies(name):
    '''
add allergies to a child passing a name
arguments:
    name: str
return: kindergartens
    '''
    if find_child(name) == None:
        return
    else:
        child, kindergarten = find_child(name)
        allergies = child['Allergies']
        #loop runs until break statement comes
        while True:
            allergy = input(f'Enter one allergy: ')
            if allergy == "":
                break
            elif allergy in allergies:
                print(f'{allergy} already exists')
            else:
                allergies.append(allergy)
        print(f'allergies added')
        return kindergartens
    
#Remove child allergy from the system
def remove_allergy(name):
    '''
remove allergy from child passing a name
arguments:
    name: str
return: kindergartens
    '''
    if find_child(name) == None:
        return
    else:
        child, kindergarten = find_child(name)
        allergies = child['Allergies']
        allergy = input(f'Enter one allergy: ')
        if allergy in allergies:
            allergies.remove(allergy)
            print(f'allergy removed')
            return kindergartens
        else:
            print(f'{name} is not allergical to {allergy}')
            return
        
#regex phone validator
def validate_phone(phone):
    '''
validate, if the input phone number are only digits
return False if wrong data
    '''
    phone_pattern = r'^\+49 \d{2} \d{6}$' 
    return True if re.match(phone_pattern, phone) else False
#regex mail validator
def validate_email(email):
    '''
validate, if the input email format is right
return False if wrong data
    '''
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return True if re.match(email_pattern, email) else False


#update Info

def update_info():
    '''
update any Infomation from any Kindergarten. stop runs, if you input wrong data
runs update_kindergarten_info if input = Kindergarten. Runs update_child_info if input = Children
    '''
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
    '''
update any Infomation from any Kindergarten. stop runs, if you input wrong category
    '''
    name = input(f'Enter the Kindergarten name:')
    if find_kindergarten(name) is None:
        return
    else:
        kg = find_kindergarten(name)
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
                option = input(f'you want to add or remove?')
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
        print(f'Nothing updated')if len(updated_keys) == 0 else print(f'{' and '.join(updated_keys)} from {kg['Name']} updated')
    return kindergartens
#update child Information
def update_child_info():
    '''
update any Infomation from any Child. stop runs, if you input wrong category
    '''
    name = input(f'Enter child name: ')
    child_found = False
    for kg in kindergartens:
        children = kg['Children']
        for child in children:
            child_name = child['Name']
            if child_name == name:
                categories = '/'.join(child.keys())
                updated_keys = []
                while True:
                    key = input(f'Choose one of the categories ({categories[5:]}):')#we avoid to change the name
                    if key not in child:
                        print(f'invalid category')
                        break
                    if key == 'Age':
                        child[key] = int(input(f'new {key}:'))
                        updated_keys.append(key)
                    elif key == 'Allergies':
                        option = input(f'you want to add or remove?')
                        add_allergies(child['Name']) if option == 'add' else remove_allergy(child['Name'])
                        updated_keys.append(key)
                    elif key == 'FavoriteActivity':
                        child[key] = input(f'new {key}:')
                        updated_keys.append(key)
                child_found = True
                print(f'Nothing updated')if len(updated_keys) == 0 else print(f'{' and '.join(updated_keys)} from {child['Name']} updated')
                return kindergartens
    if not child_found:
        print(f'Child {name} was not found on the system')

#stay in the programm
def keepOn():
    '''
asks you, if the programm keeps runing going again to the 
menu to try again or go out
    '''
    go_back = "Y"
    answer = ""
    print(f'*'*20)
    print("Do you want go back to menu? (Y/N)")
    answer = input()
    if (answer == "Y" or answer == "y"):
        main()
    else:
        print("Bye!")

#run the programm
main()