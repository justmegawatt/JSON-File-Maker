class json:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "w")
        self.open_initial_bracket()

    def open_initial_bracket(self):
        self.file.write("{\n")

    def open_json_section(self, section_name):
        self.file.write('    "' + section_name + '": ')

    def add_value(self, value):
        if type(value) == str:
            value = self.format_text(value)
            self.file.write('"{}"'.format(value) + ',')
        elif type(value) == int or type(value) == float:
            self.file.write('{}'.format(value) + ',')
        self.file.write('\n')

    def open_json_list(self):
        self.file.write("[\n")

    def add_values(self, values):
        for index, value in enumerate(values):
            if (index != len(values)-1):
                if (type(value) == str):
                    value = self.format_text(value)
                    self.file.write('        "{}",\n'.format(value))
                elif (type(value) == int or type(value) == float):
                    self.file.write('        {},\n'.format(value))
            elif (index == len(values)-1):
                if (type(value) == str):
                    value = self.format_text(value)
                    self.file.write('        "{}"\n'.format(value))
                elif (type(value) == int or type(value) == float):
                    self.file.write('        {}\n'.format(value))

    def close_json_list(self):
        self.file.write('    ],\n')

    def close_last_bracket(self):
        self.file.write('}')

    def add_field(self, field_name, value):
        self.open_json_section(field_name)
        if (type(value) == str or type(value) == float or type(value) == int):
            self.add_value(value)
        elif type(value) == list:
            self.open_json_list()
            self.add_values(value)
            self.close_json_list()

    def update_file_with_new_content(self, content):
        file = open(self.filename, 'w')
        for line in content:
            file.write(line)
        file.close()

    def remove_last_comma(self):
        temp_read_file = open(self.filename, 'r')
        content = temp_read_file.readlines()
        temp_read_file.close()
        if (content[-2][-2] == ','): # If the last field has a comma at the end
            content[-2] = content[-2][0:-2] + '\n' # Gets the 2nd to last item which is the last field, and then gets rid of the last character which is a comma, also adds a newline break
        self.update_file_with_new_content(content)

    def close(self):
        self.close_last_bracket()
        self.file.close()
        self.remove_last_comma()

    def format_text(self, text):
        text = text.replace("\"", "\\\"")
        text = text.replace("\n", "\\n")
        return text