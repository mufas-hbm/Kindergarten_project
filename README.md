# Kindergarten managing system
- This Python program is designed to help you manage all the important information about kindergartens, like their locations, facilities, and contact details. It also keeps track of the children enrolled, including their allergies and favorite activities. With this program, you can easily add, remove, and update kindergarten details, making the management process smooth and efficient.

## Data Type
- The `kindergartens` variable is a list of dictionaries that keep various types of information such as strings, integers, lists, and dictionaries.

### Format: 
- **Name**: `str` - The name of the kindergarten 
- **Location**: `str` - The location of the kindergarten 
- **Capacity**: `int` - The capacity of the kindergarten 
- **Facilities**: `list` - A list of facilities available at the kindergarten 
- **Contact**: `dict` 
- **Phone**: `str` - Phone number (validated with regex in format ´+49 30 123456´) 
- **Email**: `str` - Email address (validated with regex) 
- **Children**: `list` of `dict` 
- **Name**: `str` - The child's name 
- **Age**: `int` - The child's age 
- **Allergies**: `list` - List of allergies the child has 
- **FavoriteActivity**: `str` - The child's favorite activity  

## Functionalities
### 1. Kindergartens
#### 1.1. Add Kindergarten
- Pass name, location, capacity, and contact information. 
- Facilities and children are empty by default. 
- Data regex validation: phone and email
#### 1.2. Remove Kindergarten 
- Pass the name of the kindergarten to remove
#### 1.3. Show Information about one Kindergarten 
- Pass the name of the kindergarten to get its details
#### 1.4. Print the complet list of kindergartens
- Displays the list format, no data agreement.
#### 1.5. Add Facilities to a kindergarten
- Pass the name of the kindergarten. 
- Only add if the facility does not already exist.
#### 1.6. Remove facility from kindergarten
- Pass the name of the kindergarten.
### 2. Children
#### 2.1. Add Child to Kindergarten 
- Pass the name of the kindergarten. 
- A child cannot be added if the kindergarten is at full capacity.
#### 2.2 Remove child from Kindergarten
- Pass the child's name
#### 2.3 Search for a child 
- Pass the name of the child to show their information.
#### 2.4. List the children that are going to a kindergarten 
- Pass the name of the kindergarten.
#### 2.5. Move child from one kindergarten to another
- Pass the child's name and the new kindergarten's name. 
- Not possible if the new kindergarten is at full capacity
#### 2.6. Add allergies 
- Pass the child's name. 
- Cannot add if the allergy already
#### 2.7. Remove allergy
- Pass the child's name.
### 3. Update Information
#### Change any information you want from system
- Choose between Kindergarten or Children and update any Info you need

## Example Kindergartens Data
```python
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
            {'Name': 'Max', 'Age': 5, 'Allergies': ['Eggs', 'Nuts', 'Dairy'], 'FavoriteActivity': 'Building Blocks'}
        ]
    },  
]
```
## Example Terminal Output
### Menu
```bash
==================================================
===        KINDERGARTEN MANAGING SYSTEM        ===
==================================================
 Please choose one of the following tasks:
 1.    Add Kindergarten 
 2.    Remove Kindergarten 
 3.    See information about one Kindergarten 
 4.    Register child in Kindergarten 
 5.    See information about child  
 6.    List Children of a Kindergarten 
 7.    Unsubscribe child from Kindergarten 
 8.    Move child to another kindergarten 
 9.    Add facilities to a Kindergarten 
 10.   Remove facility from Kindergarten 
 11.   Add child allergies 
 12.   Remove child allergies 
 13.   Show all Kindergartens Information
 14.   update any Information
 15.   Leave
==================================================

Enter a task number: 
```
### Listing children from kindergarten
```bash
Enter a task number: 6
Enter a name of a Kindergarten: Little Stars Kindergarten
Name: Lara
Age: 4
Allergies:
Favorite Activity: Gardening
--------------------------------
Name: Tim
Age: 5
Allergies: Nuts
Favorite Activity: Acting
--------------------------------
```
### Add allergies to a child
```bash
Enter a task number: 11
Enter a name of a Child: Lara
Enter one allergy: Soy
Enter one allergy: Eggs
Enter one allergy: Shellfish
Enter one allergy: 
allergies added
Do you want go back to menu? (Y/N)
y
```
### List all kindergarten
```bash
Enter a task number: 13
--------------------
Name: Sunshine Kindergarten
Location: Berlin, Germany
Capacity: 120
Facilities:
 - Playground
 - Library
 - Art Room
Contact Information:
 - Phone: +49 30 123456
 - Email: info@sunshine-kindergarten.de
Number of enrolled infants: 2
Available enrollment spots: 118
--------------------
--------------------
Name: Happy Kids Kindergarten
Location: Munich, Germany
Capacity: 100
Facilities:
 - Outdoor Play Area
 - Music Room
 - Science Lab
Contact Information:
 - Phone: +49 89 654321
 - Email: info@happykids.de
Number of enrolled infants: 2
Available enrollment spots: 98
--------------------
--------------------
Name: Rainbow Kindergarten
Location: Hamburg, Germany
Capacity: 3
Facilities:
 - Swimming Pool
 - Gymnasium
 - Library
Contact Information:
 - Phone: +49 40 789012
 - Email: info@rainbow-kindergarten.de
Number of enrolled infants: 2
Available enrollment spots: 1
--------------------
--------------------
Name: Little Stars Kindergarten
Location: Frankfurt, Germany
Capacity: 90
Facilities:
 - Garden
 - Theater Room
 - Art Studio
Contact Information:
 - Phone: +49 69 345678
 - Email: info@littlestars.de
Number of enrolled infants: 2
Available enrollment spots: 88
--------------------
Do you want go back to menu? (Y/N)
n
Bye!
```