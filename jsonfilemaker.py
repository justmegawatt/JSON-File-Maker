def create_file(filename):
    file = open(filename, "w")
    return file

def open_initial_bracket(file):
    file.write("{\n")

def open_json_section(file, section_name):
    file.write('    "' + section_name + '": ')

def add_value(file, value, add_comma):
    file.write('"{}"'.format(value))
    if (add_comma):
        file.write(',')
    file.write('\n')

def open_json_list(file):
    file.write("[\n")

def add_values(file, values):
    for index, value in enumerate(values):
        if (index != len(values)-1):
            file.write('        "{}",\n'.format(value))
        elif (index == len(values)-1):
            file.write('        "{}"\n'.format(value))

def close_json_list(file, add_comma):
    file.write('    ]')
    if (add_comma):
        file.write(',')
    file.write('\n')

def close_last_bracket(file):
    file.write('}')