# Kindergarten managing system
-  This Python program is designed to help you manage all the important information about kindergartens, like their locations, facilities, and contact details. It also keeps track of the children enrolled, including their allergies and favorite activities. With this program, you can easily add, remove, and update kindergarten details, making the management process smooth and efficient.

## Data Type
    The `kindergartens` variable is a list of dictionaries that keep various types of information such as strings, integers, lists, and dictionaries.
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
- Data validation: phone and email with regex
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
            {'Name': 'Max', 'Age': 5, 'Allergies': ['None'], 'FavoriteActivity': 'Building Blocks'}
        ]
    },  
]