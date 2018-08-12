# JSON File Maker
Use Python to generate a JSON file

**Example:**

    from jsonfilemaker import json

    my_new_file = json('./my_file.json')
    my_new_file.add_field('name', 'Robert Smithing')
    my_new_file.add_field('dateOfBirth', 'Sunday, August 12th 2018')
    my_new_file.add_field('age', 55)
    my_new_file.add_field('children', ['Alex', 'Sam', 'Lin'])
    my_new_file.add_field('occupation', 'home remodeler')
    my_new_file.close()

**Creates a new file called 'my_file.json' which contains this:**

    {
        "name": "Robert Smithing",
        "dateOfBirth": "Sunday, August 12th 2018",
        "age": 55,
        "children": [
            "Alex",
            "Sam",
            "Lin"
        ],
        "occupation": "home remodeler"
    }