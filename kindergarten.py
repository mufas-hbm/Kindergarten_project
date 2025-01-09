import re
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
            {'Name': 'Lena', 'Age': 4, 'Allergies': ['Peanuts'], 'FavoriteActivity': 'Painting'},
            {'Name': 'Max', 'Age': 5, 'Allergies': ['None'], 'FavoriteActivity': 'Building Blocks'}
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
            {'Name': 'Emma', 'Age': 5, 'Allergies': ['None'], 'FavoriteActivity': 'Reading'},
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
            {'Name': 'Lara', 'Age': 4, 'Allergies': ['None'], 'FavoriteActivity': 'Gardening'},
            {'Name': 'Tim', 'Age': 5, 'Allergies': ['Nuts'], 'FavoriteActivity': 'Acting'}
        ]
    }
    
]
'''
Menü function, it runs at the beginning
'''
def main():
    print("---Kindergarten managing System ---\n")
    print("--- Please choose one of the following tasks:\n")
    print("--- 1.  Add Kindergarten ---\n")
    print("--- 2.  Remove Kindergarten ---\n")
    print("--- 3.  See information about one Kindergarten --\n")
    print("--- 4.  Register child in Kindergarten ---\n")
    print("--- 5.  Search for a child ---\n")
    print("--- 6.  List Children of a Kindergarten ---\n")
    print("--- 7.  Unsubscribe child from Kindergarten ---\n")
    print("--- 8.  Move child to another kindergarten ---\n")
    print("--- 9.  Add facilities to a Kindergarten ---\n")
    print("--- 10.  Remove facility from Kindergarten ---\n")
    print("--- 11.  Add child allergies ---\n")
    print("--- 12.  Remove child allergies ---\n")
    print("--- 13.  Show all Kindergartens Information ---\n")
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
            capacity = int(input("How many children are allowed? "))
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
            search_child(name)
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
        else:
            print("this option doesn't exist, try again")
            main()
#Adding Kindergarten
'''
create a new Kindergarten and add to the List of dictionaries
By creating a new one, there are no children (we create key Children but its empty by default)
arguments:
    name: str
    location: str
    capacity: int
'''
def add_kindergarten(name, location, capacity, phone, email):
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
'''
delete a kindergarten passing the name. If doesn't exists, show message
arguments:
    name: str
'''
def remove_kindergarten(name):
    if find_kindergarten(name) == None:
        return
    else:
        kg = find_kindergarten(name)
        kindergartens.remove(kg)
        print(f'Kindergarten {name} was succesfully removed from the system')
        return kindergartens
#See information about one Kindergarten
'''
show all the data about one kindergarten
arguments:
    name: str
'''
def kindergarten_information(name):
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
'''
 unpacking list facilities of one kindergarten to list
 '''
def unpack_facilities(kindergarten):
    for facility in kindergarten['Facilities']:
        print(f' - {facility}')
#add facilities
'''
add facilities to a kindergarten if not already exist.
arguments:
    name: str
return:
    kindergartens: list of dict
'''
def add_facilities(name):
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
'''
remove facilitiy from Kindergarten
arguments:
    name: str
return:
    kindergartens: list of dict
'''
def remove_facility(name):
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
#Child search
'''
search for a child and show data if child exists. if not, show message
arguments:
    name: str
'''  
def search_child(name):
    child_found = False
    for kg in kindergartens:
        children = kg['Children']
        for child in children:
            child_name = child['Name']
            if child_name == name:
                print(f'what school does he go to: {kg['Name']}')
                print(f'Name: {child['Name']}')
                print(f'Age: {child['Age']}')
                print(f'Allergies: {', '.join(child['Allergies'])}')
                print(f'Favorite Activity: {child['FavoriteActivity']}')
                child_found = True
                break
    if not child_found:
        print(f'Child {name} was not found on the system')

#List Children of a kindergarten
'''
passing a kindergarten list all the children
argument:
    kindergarten: str
'''
def list_children(kindergarten):
    if find_kindergarten(kindergarten) == None:
        return
    else:
        kg = find_kindergarten(kindergarten)
        children = kg['Children']
        for child in children:
            print(f'Name: {child['Name']}')
            print(f'Age: {child['Age']}')
            print(f'Allergies: {', '.join(child['Allergies'])}')
            print(f'Favorite Activity: {child['FavoriteActivity']}')
            print(f'--------------------------------')
#add child
'''
add child passing a kindergarten 
arguments:
    kindergarten:str
return:
    None if Kindergarten is already full of children
    kindergartens: list
'''
def add_child(kindergarten):
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
            age = int(input(f'Age: '))
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
'''
remove a child by passing a name
arguments:
    name: str
return:
    kindergartens: list
'''
def remove_child(name):
    child_found = False
    for kg in kindergartens:
        children = kg['Children']
        for child in children:
            child_name = child['Name']
            if child_name == name:
                children.remove(child)
                print(f'Child was succesfully removed')
                return kindergartens
    if not child_found:
        print(f'Child {name} was not found on the system')
#move child from kindergarten to another
'''
move one child from one kindergarten to another
arguments:
    name: str
    kindergarten: dict
return:
    kindergartens
'''
def move_child(name_child, name_kindergarten):
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
'''
add allergies to a child passing a name
arguments:
    name: str
return: kindergartens
'''
def add_allergies(name):
    child_found = False
    for kg in kindergartens:
        children = kg['Children']
        for child in children:
            child_name = child['Name']
            allergies = child['Allergies']
            if child_name == name:
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
    if not child_found:
        print(f'Child {name} was not found on the system')
        return
#Remove child allergy from the system
'''
remove allergy from child passing a name
arguments:
    name: str
return: kindergartens
'''
def remove_allergy(name):
    child_found = False
    for kg in kindergartens:
        children = kg['Children']
        for child in children:
            child_name = child['Name']
            allergies = child['Allergies']
            if child_name == name:
                    allergy = input(f'Enter one allergy: ')
                    if allergy in allergies:
                        allergies.remove(allergy)
                        print(f'allergy removed')
                        return kindergartens
                    else:
                        print(f'{name} is not allergical to {allergy}')
                        return
    if not child_found:
        print(f'Child {name} was not found on the system')
        return

#search for a kindergarten
'''
search for one kindergarten in the list of kindergartens
arguments:
    name: str
return:
    kindergarten: dict if name was found, otherwise return message
'''
def find_kindergarten(name):
    for kg in kindergartens:
         if kg['Name'] == name:
            return kg
    print(f'this Kindergarten was not found')
    return None

#Show all Kindergartens
'''
print all the kindergartens
'''
def show_kindergartens():
    for kg in kindergartens:
        print("-"*20)
        print(f'Name: {kg['Name']}')
        print(f'Location: {kg['Location']}')
        print(f'Capacity: {kg['Capacity']}')
        print(f'Facilities: {kg['Facilities']}')
        print(f'Contact: {kg['Contact']}')
        print(f'Children: {kg['Children']}')
        print("-"*20)
#regex phone validator
'''
validate, if the input phone number are only digits
return False if wrong data
'''
def validate_phone(phone):
    phone_pattern = r'^\+49 \d{2} \d{6}$' 
    return True if re.match(phone_pattern, phone) else False
#eregex mail validator
def validate_email(email):
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return True if re.match(email_pattern, email) else False



'''
Function that asks you, if the programm should go back to the 
menu to try again or go out
'''
def keepOn():
    go_back = "Y"
    answer = ""
    print("Do you want go back to menu? (Y/N)")
    answer = input()
    if (answer == "Y" or answer == "y"):
        main()
    else:
        print("Bye!")
main()