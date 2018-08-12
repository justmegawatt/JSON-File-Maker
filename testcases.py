import unittest
from pathlib import Path
import os
import jsonfilemaker as jfm

class TestWordToJSON(unittest.TestCase):

    def setUp(self):
        pass

    def delete_file(self, filename):
        file_location = Path(filename)
        if (file_location.exists()):
            os.remove(filename)

    def test_create_file(self):
        filename = './testfile.json'
        file = jfm.create_file(filename)
        test_file = Path(filename)
        self.assertTrue(test_file.exists())
        file.close()
        if (test_file.exists()):
            os.remove(filename)

    def test_open_initial_bracket(self):
        filename = "./test.json"
        file = jfm.create_file(filename)
        jfm.open_initial_bracket(file)
        file.close()
        opened_file = open(filename, 'r')
        self.assertEqual("{\n", opened_file.readlines()[-1])
        opened_file.close()
        self.delete_file(filename)

    def test_open_json_section(self):
        filename = "./test.json"
        file = jfm.create_file(filename)
        jfm.open_initial_bracket(file)
        jfm.open_json_section(file, "testvalues")
        file.close()
        opened_file = open(filename, 'r')
        self.assertEqual('    "testvalues": ', opened_file.readlines()[-1])
        opened_file.close()
        self.delete_file(filename)

    def test_add_value(self):
        filename = "./test.json"
        file = jfm.create_file(filename)
        jfm.open_initial_bracket(file)
        jfm.open_json_section(file, "date")
        jfm.add_value(file, "Sunday, August 12th 2018", False)
        file.close()
        opened_file = open(filename, 'r')
        self.assertEqual('    "date": "Sunday, August 12th 2018"\n', opened_file.readlines()[-1])
        opened_file.close()
        self.delete_file(filename)

    def test_open_json_list(self):
        filename = "./test.json"
        file = jfm.create_file(filename)
        jfm.open_initial_bracket(file)
        jfm.open_json_section(file, "testvalues")
        jfm.open_json_list(file)
        file.close()
        opened_file = open(filename, 'r')
        self.assertEqual('    "testvalues": [\n', opened_file.readlines()[-1])
        opened_file.close()
        self.delete_file(filename)

    def test_add_values(self):
        values = ["first", "second", "third"]
        filename = "./test.json"
        file = jfm.create_file(filename)
        jfm.open_initial_bracket(file)
        jfm.open_json_section(file, "testvalues")
        jfm.open_json_list(file)
        jfm.add_values(file, values)
        file.close()
        opened_file = open(filename, "r")
        self.assertEqual(['{\n', '    "testvalues": [\n', '        "first",\n', '        "second",\n', '        "third"\n'], opened_file.readlines())
        opened_file.close()
        self.delete_file(filename)

    def test_close_json_list(self):
        values = ["first", "second", "third"]
        filename = "./test.json"
        file = jfm.create_file(filename)
        jfm.open_initial_bracket(file)
        jfm.open_json_section(file, "testvalues")
        jfm.open_json_list(file)
        jfm.add_values(file, values)
        jfm.close_json_list(file, False)
        file.close()
        opened_file = open(filename, "r")
        self.assertEqual('    ]\n', opened_file.readlines()[-1])
        opened_file.close()
        self.delete_file(filename)

    def test_close_last_bracket(self):
        values = ["first", "second", "third"]
        filename = "./test.json"
        file = jfm.create_file(filename)
        jfm.open_initial_bracket(file)
        jfm.open_json_section(file, "testvalues")
        jfm.open_json_list(file)
        jfm.add_values(file, values)
        jfm.close_json_list(file, False)
        jfm.close_last_bracket(file)
        file.close()
        opened_file = open(filename, "r")
        self.assertEqual('}', opened_file.readlines()[-1])
        opened_file.close()
        self.delete_file(filename)

    def test_full_feature_test(self):
        file = open("./new_file.json", "w")
        jfm.open_initial_bracket(file)
        jfm.open_json_section(file, "date")
        jfm.add_value(file, "Sunday, August 12th 2018", True)
        jfm.open_json_section(file, "paragraphs")
        jfm.open_json_list(file)
        jfm.add_values(file, ["First", "Second", "Third"])
        jfm.close_json_list(file, True)
        jfm.open_json_section(file, "another")
        jfm.close_last_bracket(file)
        file.close()

if __name__ == '__main__':
    unittest.main()