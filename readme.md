# JSON File Maker
Use Python to generate a JSON file

---

#### Creating a new JSON Object
 
    from jsonfilemaker import json
    
    my_file = json('my_file.json')
    # do stuff here
    my_file.close() # Don't forget to close it!

**Result:** Creates a new file in current directory called 'my_file.json'


---
#### Adding Single Value Fields

    my_file.add_field('name', 'Robert Smithing')
    my_file.add_field('dateOfBirth', 'Sunday, August 12th 2018')
    my_file.add_field('age', 55)
    my_file.add_field('preciseAge', 55.5312)
    
**Result:**

    {
        "name": "Robert Smithing",
        "dateOfBirth": "Sunday, August 12th 2018",
        "age": 55,
        "preciseAge": 55.5312
    }

---

#### Adding List/Array Fields

    my_file.add_field('children', ['Alex', 'Sam', 'Lin'])
    
**Result:**

    {
        "children": [
            "Alex",
            "Sam",
            "Lin"
        ]
    }

---

#### Putting it all together

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